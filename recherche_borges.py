from pathlib import Path
from tkinter.filedialog import askopenfilename

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# 1. Fonction pour rechercher les trois passages les plus proches
def rechercher(requete):
    vecteur_requete = vectoriseur.transform([requete])
    scores = cosine_similarity(vecteur_requete, matrice)[0]
    indices = scores.argsort()[::-1][:3]

    if scores.max() == 0:
        print("Aucun mot de la recherche retrouvé.")
        return

    for i in indices:
        if scores[i] > 0:
            print("\nPassage", i)
            print("Score :", round(float(scores[i]), 3))
            print(passages[i])


# 2. Choisir le fichier contenant le récit
chemin = askopenfilename(
    title="Choisis le fichier texte de Borges",
    filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")]
)

if chemin:
    # 3. Charger le texte
    texte = Path(chemin).read_text(encoding="utf-8")

    # 4. Découper le texte en passages de 100 mots
    mots = texte.split()

    passages = [
        " ".join(mots[i:i + 100])
        for i in range(0, len(mots), 100)
    ]

    if passages:
        # 5. Transformer les passages en nombres
        vectoriseur = TfidfVectorizer()
        matrice = vectoriseur.fit_transform(passages)

        print("Nombre de mots :", len(mots))
        print("Nombre de passages :", len(passages))

        # 6. Lancer une première recherche
        rechercher("escribir el Quijote")

    else:
        print("Le fichier est vide.")

else:
    print("Aucun fichier sélectionné.")
