# --- Les Variables en Python ---

# 1. Les types numériques
entier = 10                  # int (entier)
decimal = 10.5               # float (nombre à virgule)
complexe = 2 + 3j            # complex (nombre complexe)

print(f"Entier: {entier} (Type: {type(entier)})")
print(f"Décimal: {decimal} (Type: {type(decimal)})")
print(f"Complexe: {complexe} (Type: {type(complexe)})")

# 2. Les chaînes de caractères
nom = "Alice"                # str (chaîne de caractères)
message = 'Bonjour tout le monde'
multiligne = """Ceci est une chaîne
sur plusieurs lignes."""

print(f"Chaîne: {nom} (Type: {type(nom)})")

# 3. Les booléens
est_vrai = True               # bool (Vrai ou Faux)
est_faux = False

print(f"Booléen: {est_vrai} (Type: {type(est_vrai)})")

# 4. Les types de données séquentiels (Collections)

# Liste (ordonnée, modifiable)
fruits = ["pomme", "banane", "orange"] # list
print(f"Liste: {fruits} (Type: {type(fruits)})")

# Tuple (ordonné, non modifiable)
coordonnees = (10, 20)        # tuple
print(f"Tuple: {coordonnees} (Type: {type(coordonnees)})")

# 5. Les types de mapping

# Dictionnaire (clé: valeur)
personne = {
    "nom": "Jean",
    "age": 25,
    "ville": "Casablanca"
}                             # dict
print(f"Dictionnaire: {personne} (Type: {type(personne)})")

# 6. Les types d'ensemble

# Set (collection non ordonnée, éléments uniques)
couleurs = {"rouge", "vert", "bleu", "rouge"} # set (le doublon sera supprimé)
print(f"Set: {couleurs} (Type: {type(couleurs)})")

# 7. Type None
vide = None                  # NoneType (absence de valeur)
print(f"None: {vide} (Type: {type(vide)})")

# --- Règles de nommage des variables ---
# - Doit commencer par une lettre ou un underscore (_).
# - Ne peut pas commencer par un chiffre.
# - Ne peut contenir que des caractères alphanumériques et des underscores (A-z, 0-9, et _).
# - Sensible à la casse (majuscules/minuscules).
# - Ne peut pas être un mot-clé réservé (ex: if, while, print).
