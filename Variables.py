# =============================================================
# 📚 LES TYPES DE VARIABLES EN PYTHON
# =============================================================

# --- 1. TYPES NUMÉRIQUES ---
age = 25                        # int (entier)
prix = 19.99                    # float (nombre à virgule)
z = 2 + 3j                      # complex (nombre complexe)

# --- 2. CHAÎNES DE CARACTÈRES ---
nom = "Hamza"                   # str (texte)
message = 'Bienvenue !'
multi = """Texte sur
plusieurs lignes"""

# --- 3. BOOLÉENS (LOGIQUE) ---
est_valide = True               # bool (Vrai)
est_erreur = False              # bool (Faux)

# --- 4. COLLECTIONS (VRAIE PUISSANCE DE PYTHON) ---

# Liste : Ordonnée, modifiable, avec doublons
fruits = ["pomme", "banane", "pomme"] 

# Tuple : Ordonné, NON modifiable (fixe)
coordonnees = (48.8, 2.3)

# Dictionnaire : Clé -> Valeur (comme un annuaire)
eleve = {
    "nom": "Alice",
    "note": 18,
    "cours": "Python"
}

# Set : Non ordonné, SANS doublons
nombres_uniques = {1, 2, 3, 3, 2} # Résultat : {1, 2, 3}

# --- 5. TYPE SPÉCIAL ---
resultat = None                 # Absence de valeur (vide)

# --- VÉRIFICATION ---
print(f"Variable 'age' est de type : {type(age)}")
print(f"Variable 'fruits' est de type : {type(fruits)}")
print(f"Variable 'eleve' est de type : {type(eleve)}")
