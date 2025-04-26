import os
from flask import Flask, render_template, redirect, url_for, request, flash
from werkzeug.utils import secure_filename
from models import db, User, Post, initialize_db
from forms import PostForm, UserForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/uploads'  # Dosyaların kaydedileceği klasör


# Dosya yükleme için izin verilen uzantılar
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# Veritabanını başlat
initialize_db()

@app.route('/')
def index():
    posts = Post.select()
    return render_template('index.html', posts=posts)




@app.route('/post/<int:post_id>')
def show_post(post_id):
    post = Post.get_or_none(Post.id == post_id)
    if post:
        return render_template('post.html', post=post)
    flash('Gönderi bulunamadı!', 'danger')
    return redirect(url_for('index'))

@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        try:
            # İlk kullanıcıyı al veya varsayılan bir kullanıcı oluştur
            author = User.get(User.id == 1)
        except User.DoesNotExist:
            author = User.create(username="default", email="default@example.com", password="password123")

        post = Post(title=form.title.data, content=form.content.data, author=author)
        post.save()
        flash('Gönderi başarıyla oluşturuldu!', 'success')
        return redirect(url_for('index'))
    return render_template('create_post.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = UserForm()
    if form.validate_on_submit():
        # Dosya yükleme işlemi
        file = form.profile_picture.data
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            profile_picture = filename  # Dosya adını veritabanına kaydet
        else:
            profile_picture = None  # Dosya yoksa veya geçersizse

        user = User(username=form.username.data, email=form.email.data, password=form.password.data, profile_picture=profile_picture)
        user.save()
        flash('Kullanıcı başarıyla kaydedildi!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', form=form)

@app.route('/admin/')
def admin_dashboard():
    users = User.select()
    return render_template('admin/dashboard.html', users=users)

@app.route('/admin/edit_user/<int:user_id>', methods=['GET', 'POST'])
def admin_edit_user(user_id):
    user = User.get_or_none(User.id == user_id)
    if not user:
        flash('Kullanıcı bulunamadı!', 'danger')
        return redirect(url_for('admin_dashboard'))

    form = UserForm(obj=user)
    if form.validate_on_submit():
        # Dosya yükleme işlemi
        file = form.profile_picture.data
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            user.profile_picture = filename  # Dosya adını veritabanına kaydet
        elif not file:
            # Dosya yüklenmemişse, mevcut resmi koru
            pass

        user.username = form.username.data
        user.email = form.email.data
        user.password = form.password.data
        user.save()
        flash('Kullanıcı başarıyla güncellendi!', 'success')
        return redirect(url_for('admin_dashboard'))
    return render_template('admin/edit_user.html', form=form, user=user)


@app.route('/admin/create_post', methods=['GET', 'POST'])
def admin_create_post():
    form = PostForm()
    if form.validate_on_submit():
        try:
            # İlk kullanıcıyı al veya varsayılan bir kullanıcı oluştur
            author = User.get(User.id == 1)
        except User.DoesNotExist:
            author = User.create(username="admin", email="admin@example.com", password="admin123")

        post = Post(title=form.title.data, content=form.content.data, author=author)
        post.save()
        flash('Gönderi başarıyla oluşturuldu!', 'success')
        return redirect(url_for('admin_dashboard'))
    return render_template('admin/create_post.html', form=form)

@app.route('/admin/edit_post/<int:post_id>', methods=['GET', 'POST'])
def admin_edit_post(post_id):
    post = Post.get_or_none(Post.id == post_id)
    if not post:
        flash('Gönderi bulunamadı!', 'danger')
        return redirect(url_for('admin_dashboard'))

    form = PostForm(obj=post)
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.save()
        flash('Gönderi başarıyla güncellendi!', 'success')
        return redirect(url_for('admin_dashboard'))
    return render_template('admin/edit_post.html', form=form, post=post)

@app.route('/admin/delete_post/<int:post_id>')
def admin_delete_post(post_id):
    post = Post.get_or_none(Post.id == post_id)
    if post:
        post.delete_instance()
        flash('Gönderi başarıyla silindi!', 'success')
    else:
        flash('Gönderi bulunamadı!', 'danger')
    return redirect(url_for('admin_dashboard'))

if __name__ == '__main__':
    # Uploads klasörünü oluştur
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)