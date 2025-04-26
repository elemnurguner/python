from flask import Flask, render_template, request, redirect, url_for, flash, session
import pyodbc

app = Flask(__name__)
app.secret_key = '1a6c951e47cf990a69281a519fb7e3b39a74a7022b219694'  # Oturum için gerekli

# SQL Server bağlantı dizesi
conn_str = (
    "DRIVER={SQL Server};"
    "SERVER=DESKTOP-F2T2PJU;"
    "DATABASE=TestDB;"
)

# Ana sayfa
@app.route('/')
def home():
    return render_template('home.html')

# Kullanıcı girişi
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("SELECT UserID, FirstName, LastName FROM Users WHERE Email = ? AND Password = ?", (email, password))
        user = cursor.fetchone()
        
        if user:
            session['logged_in'] = True
            session['user_id'] = user.UserID
            session['first_name'] = user.FirstName  # Kullanıcının adını session'a ekle
            session['last_name'] = user.LastName    # Kullanıcının soyadını session'a ekle
            flash("Giriş başarılı!")
            return redirect(url_for('dashboard'))
        else:
            flash("Geçersiz e-posta veya şifre!")
    
    return render_template('login.html')

# Kullanıcı çıkışı
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    session.pop('first_name', None)  # Kullanıcı adını session'dan sil
    session.pop('last_name', None)   # Kullanıcı soyadını session'dan sil
    flash("Çıkış yapıldı!")
    return redirect(url_for('home'))

# Dashboard
@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        flash("Lütfen giriş yapın!")
        return redirect(url_for('login'))
    
    user_id = session.get('user_id')
    
    # Ürünleri veritabanından çek
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    
    return render_template('dashboard.html', user_id=user_id, products=products)

# Ürün ekleme
@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if not session.get('logged_in'):
        flash("Lütfen giriş yapın!")
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        product_name = request.form['product_name']
        price = float(request.form['price'])
        stock = int(request.form['stock'])
        
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Products (ProductName, Price, Stock) VALUES (?, ?, ?)", (product_name, price, stock))
        conn.commit()
        
        flash("Ürün başarıyla eklendi!")
        return redirect(url_for('dashboard'))
    
    return render_template('add_product.html')

# Sepete ürün ekleme
@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    if not session.get('logged_in'):
        flash("Lütfen giriş yapın!")
        return redirect(url_for('login'))
    
    quantity = int(request.form['quantity'])
    user_id = session.get('user_id')
    
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    
    # Stok kontrolü
    cursor.execute("SELECT Stock FROM Products WHERE ProductID = ?", (product_id,))
    stock = cursor.fetchone()[0]
    
    if stock >= quantity:
        # Sepette aynı ürün var mı kontrol et
        cursor.execute("SELECT Quantity FROM Cart WHERE UserID = ? AND ProductID = ?", (user_id, product_id))
        existing_item = cursor.fetchone()
        
        if existing_item:
            # Eğer ürün sepette varsa, miktarını artır
            new_quantity = existing_item.Quantity + quantity#benim existing_item gelen Quantity değerimin üstüne sessinda gelen yeni değeri ekle
            cursor.execute("UPDATE Cart SET Quantity = ? WHERE UserID = ? AND ProductID = ?", (new_quantity, user_id, product_id))
        else:
            # Eğer ürün sepette yoksa, yeni kayıt ekle
            cursor.execute("INSERT INTO Cart (UserID, ProductID, Quantity) VALUES (?, ?, ?)", (user_id, product_id, quantity))
        
        # Stok güncelleme
        cursor.execute("UPDATE Products SET Stock = Stock - ? WHERE ProductID = ?", (quantity, product_id))
 #Sepete yeni ürün eklendiği için, stoktan bu yeni miktar kadar düşülmesi gerekiyor. Bu nedenle stok güncelleme işlemi yapılıyor:       
        conn.commit()
        flash("Ürün sepete eklendi!")
    else:
        flash("Yeterli stok yok!")
    
    return redirect(url_for('dashboard'))

#sepetten ürün çıkarma silme işlemi 
@app.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
# Kullanıcının oturum açıp açmadığını kontrol eder.
# Eğer kullanıcı giriş yapmamışsa, giriş sayfasına yönlendirilir.
    if not session.get('logged_in'):
        flash("Lütfen giriş yapın!")
        return redirect(url_for('login'))
    
    user_id = session.get('user_id')
    
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    
    # Sepetteki ürünün miktarını al
    cursor.execute("SELECT Quantity FROM Cart WHERE UserID = ? AND ProductID = ?", (user_id, product_id))
    item = cursor.fetchone()
    
    if item:
        quantity = item.Quantity
        
        # Ürünü sepetten sil
        cursor.execute("DELETE FROM Cart WHERE UserID = ? AND ProductID = ?", (user_id, product_id))
        
        # silinen  sepetteki urunu stoga eklemem  gerekecek 
        # Bu sorgu, ürünün stok miktarını, sepetten çıkarılan miktar kadar artırır.
        #Stock + ?: Stok miktarına, sepetteki ürün miktarı (quantity) eklenir.
        cursor.execute("UPDATE Products SET Stock = Stock + ? WHERE ProductID = ?", (quantity, product_id))
        
        conn.commit()
        flash("Ürün sepetten çıkarıldı!")
    else:
        flash("Ürün bulunamadı!")
    
    return redirect(url_for('cart'))


# Sepeti görüntüleme işlemi için route tanımlanıyor.
# Bu route, kullanıcının sepetindeki ürünleri listeler.
@app.route('/cart')
def cart():
    if not session.get('logged_in'):
        flash("Lütfen giriş yapın!")
        return redirect(url_for('login'))
    
    user_id = session.get('user_id')
    
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    
## Sepetteki ürünleri getirmek için bir SQL sorgusu çalıştırılır.
    # Bu sorgu, Cart (Sepet) tablosu ile Products (Ürünler) tablosunu birleştirir (JOIN).
    # Aşağıdaki bilgileri getirir:
    # - Ürün ID'si (ProductID)
    # - Ürün adı (ProductName)
    # - Sepetteki miktar (Quantity)
    # - Ürün fiyatı (Price)
    # Sorgu, yalnızca belirli bir kullanıcıya (user_id) ait sepet kayıtlarını getirir.
    cursor.execute("""
        SELECT Products.ProductID, Products.ProductName, Cart.Quantity, Products.Price 
        FROM Cart 
        JOIN Products ON Cart.ProductID = Products.ProductID 
        WHERE Cart.UserID = ?
    """, (user_id,))
    cart_items = cursor.fetchall()
    
    return render_template('cart.html', cart_items=cart_items)

if __name__ == '__main__':
    app.run(debug=True)