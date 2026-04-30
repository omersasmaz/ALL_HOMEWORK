-- Christopher Nolan'ın yönettiği tüm filmleri getir
-- movies ve directors tablolarını 'id' üzerinden birleştiriyoruz
SELECT movies.title 
FROM movies 
JOIN directors ON movies.id = directors.movie_id 
JOIN people ON directors.person_id = people.id 
WHERE people.name = 'Christopher Nolan';
cat << 'EOF' > week8/design/stats.sql
-- Her yıl kaç film çekildiğini hesapla
SELECT year, COUNT(title) 
FROM movies 
GROUP BY year 
ORDER BY year DESC;

-- Filmlerin ortalama puanını hesapla
SELECT AVG(rating) FROM ratings;
