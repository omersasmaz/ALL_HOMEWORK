-- 2023 yılında çıkan filmlerin isimlerini seç
SELECT title FROM movies WHERE year = 2023;

-- İsmi 'Harry Potter' ile başlayan filmleri alfabetik sırala
SELECT title FROM movies 
WHERE title LIKE 'Harry Potter%' 
ORDER BY title ASC;

-- En yüksek puanlı 10 filmi getir
SELECT title, rating FROM movies 
ORDER BY rating DESC 
LIMIT 10;
