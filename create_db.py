import sqlite3

connection = sqlite3.connect("articles.sqlite")


with open("schema.sql") as file:
    connection.executescript(file.read())

cur = connection.cursor()

cur.execute(
    "INSERT INTO articles (id, title, subtitle, date, body, author, img_url, song_url) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
    (
        1,
        "Why does Saturn have rings?",
        "Just because.",
        "December 4, 2023",
        "Have you ever wondered why Saturn has rings? Well, you're not alone. Scientists have been puzzled by this question for centuries, and they still don't have a definitive answer. But they have some pretty good guesses, and some of them are hilarious. Here are some of the most amusing theories on why Saturn has rings.Saturn is a hoarder. It likes to collect stuff from the solar system, like rocks, dust, ice, and even moons. It can't get enough of them, so it keeps them in orbit around itself. Some of these objects collide and break apart, forming the rings we see today. Saturn is basically the ultimate pack rat of the planets. Saturn is a fashionista. It wants to stand out from the crowd and look fabulous. It knows that rings are a great accessory, so it decided to make some for itself. It used its gravity to pull in material from nearby asteroids and comets, and shaped them into elegant circles. Saturn is the most stylish planet in the solar system. Saturn is a rebel. It doesn't like to follow the rules and do what other planets do. It wants to be different and unique. It knows that most planets don't have rings, so it decided to have some just to be contrary. It used its powerful magnetic field to capture and hold onto debris from its surroundings, and arranged them into chaotic bands. Saturn is the most rebellious planet in the solar system. Saturn is a prankster. It likes to mess with other planets and make them jealous. It knows that rings are a rare and coveted feature, so it decided to have some just to show off. It used its massive size and rotation to fling material from its surface and atmosphere into orbit, and formed them into dazzling rings. Saturn is the most playful planet in the solar system. Saturn is a mystery. It has secrets that no one can fully understand. It knows that rings are a fascinating and mysterious phenomenon, so it decided to have some just to intrigue us. It used its ancient history and evolution to create and maintain its rings over billions of years, and hid the details from us. Saturn is the most mysterious planet in the solar system.",
        "Arihant",
        "https://images.unsplash.com/photo-1701542182020-6355e2c059a1?q=80&w=3087&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "https://open.spotify.com/embed/track/3ntrdR24dLkKrzSGRv1FlH?utm_source=generator",
    ),
)

cur.execute(
    "INSERT INTO articles (id, title, subtitle, date, body, author, img_url, song_url) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
    (
        2,
        "On Indie Music",
        "Indie music is nice!",
        "December 5, 2023",
        "Indie music is a genre of music that is independent from the mainstream music industry. It is often creative, original and diverse, reflecting the personal vision of the artists. Indie music can be a source of inspiration, enjoyment and discovery for listeners who appreciate its uniqueness and authenticity.",
        "ira",
        "https://images.unsplash.com/photo-1701456449854-c4933aade45b?q=80&w=3087&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "https://open.spotify.com/embed/track/5UVBumEwdUnzvqxrXOYLFA?utm_source=generator",
    ),
)
connection.commit()
connection.close()
