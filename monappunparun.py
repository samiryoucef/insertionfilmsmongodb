import random
import time
from pymongo import MongoClient

# --- Connexion à MongoDB ---
client = MongoClient("mongodb://localhost:27017/")
db = client["ma_base_films"]
collection = db["films"]

# --- Listes de données pour la génération ---
titres = [
    "La Nuit Rouge", "Les Portes du Vent", "Le Dernier Voyage",
    "L'Ombre du Temps", "Rêves Perdus", "L'Homme Silencieux"
]

genres = ["Action", "Comédie", "Drame", "Horreur", "Science-Fiction", "Aventure"]

realisateurs = [
    "Samir Y.", "Claude G.", "Francois C.", "Pascal U.", "Thomas K.", "Nadia Z."
]

print("Insertion film par film en cours...")

start = time.time()

# --- Bi-boucle : 1 000 000 films ---
for i in range(1000):
    for j in range(1000):
        film = {
            "titre": random.choice(titres),
            "genre": random.choice(genres),
            "année": random.randint(1980, 2025),
            "réalisateur": random.choice(realisateurs),
            "durée_minutes": random.randint(80, 180)
        }

        # insertion *un seul document* à la fois
        collection.insert_one(film)

end = time.time()

print(f"✔ Insertion terminée. Temps total : {end - start:.2f} secondes.")

