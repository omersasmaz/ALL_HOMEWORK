async function getQuote() {
    try {
        const response = await fetch('https://api.quotable.io/random');
        const data = await response.json();
        console.log(`${data.content} - ${data.author}`);
    } catch (error) {
        console.error("Veri çekilirken hata oluştu:", error);
    }
}
