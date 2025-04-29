// Sayfa yüklendiğinde çalışır
window.addEventListener('load', function() {
    const savedUsername = localStorage.getItem('currentUser'); // Oturum bilgisini al
    if (savedUsername) {
        document.getElementById('username').textContent = savedUsername; // Kullanıcı adını göster
    } else {
        window.location.href = 'index.html'; // Oturum yoksa giriş sayfasına yönlendir
    }
});

// Çıkış yapma işlemi
document.getElementById('logoutButton').addEventListener('click', function() {
    localStorage.removeItem('currentUser'); // Oturum bilgisini sil
    window.location.href = 'index.html'; // Giriş sayfasına yönlendir
});