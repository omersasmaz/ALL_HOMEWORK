// DOM elemanlarını seçelim
const btn = document.querySelector('#btn');
const msg = document.querySelector('#msg');

// Olay dinleyicisi ekleyelim
btn.addEventListener('click', function() {
    msg.textContent = "JavaScript başarıyla çalıştı! Sayfa artık interaktif.";
    msg.style.color = "green";
    btn.style.display = "none"; // Butonu gizle
});
