// SHA-256 ile şifre hash'leme fonksiyonu
async function hashPassword(password) {
    const encoder = new TextEncoder(); // Metni byte dizisine çevir
    const data = encoder.encode(password); // Şifreyi byte dizisine dönüştür
    const hashBuffer = await crypto.subtle.digest('SHA-256', data); // SHA-256 ile hash'le
    const hashArray = Array.from(new Uint8Array(hashBuffer)); // Byte dizisini array'e çevir
    const hashHex = hashArray.map(byte => byte.toString(16).padStart(2, '0')).join(''); // Hex formatına dönüştür
    return hashHex; // Hash'lenmiş şifreyi döndür
}

// Kayıt olma işlemi
document.getElementById('registerForm').addEventListener('submit', async function(event) {
    event.preventDefault(); // Formun varsayılan gönderimini engelle

    const regUsername = document.getElementById('regUsername').value;
    const regPassword = document.getElementById('regPassword').value;

    // Şifreyi hash'le
    const hashedPassword = await hashPassword(regPassword);

    // Kullanıcı adı daha önce kaydedilmiş mi kontrol et
    if (localStorage.getItem(regUsername)) {
        document.getElementById('message').textContent = 'Bu kullanıcı adı zaten kayıtlı!';
    } else {
        // Kullanıcı adı ve hash'lenmiş şifreyi Local Storage'a kaydet
        localStorage.setItem(regUsername, hashedPassword);
        document.getElementById('message').textContent = 'Kayıt başarılı! Giriş yapabilirsiniz.';
    }
});

// Giriş yapma işlemi
document.getElementById('loginForm').addEventListener('submit', async function(event) {
    event.preventDefault(); // Formun varsayılan gönderimini engelle

    const loginUsername = document.getElementById('loginUsername').value;
    const loginPassword = document.getElementById('loginPassword').value;

    // Kullanıcı adı kayıtlı mı kontrol et
    const savedHashedPassword = localStorage.getItem(loginUsername);

    if (savedHashedPassword) {
        // Giriş yapılan şifreyi hash'le
        const hashedLoginPassword = await hashPassword(loginPassword);

        // Hash'lenmiş şifreleri karşılaştır
        if (savedHashedPassword === hashedLoginPassword) {
            document.getElementById('message').textContent = 'Giriş başarılı!';
            localStorage.setItem('currentUser', loginUsername); // Oturum bilgisini kaydet
            window.location.href = 'dashboard.html'; // Dashboard'a yönlendir
        } else {
            document.getElementById('message').textContent = 'Kullanıcı adı veya şifre hatalı!';
        }
    } else {
        document.getElementById('message').textContent = 'Kullanıcı adı bulunamadı!';
    }
});