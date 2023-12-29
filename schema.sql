DROP TABLE IF EXISTS articles;

CREATE TABLE articles (
    id INTEGER PRIMARY KEY,
    title TEXT,
    subtitle TEXT,
    date TEXT,
    body TEXT,
    author TEXT,
    img_url TEXT,
    song_url TEXT
);