# =============================================================
# 🖨️ LA FONCTION PRINT() EN PYTHON
# =============================================================

# --- 1. AFFICHAGE DE BASE ---
print("Bonjour tout le monde !")
print(12345)

# --- 2. LE FORMATAGE F-STRING (Le meilleur) ---
# Permet d'insérer des variables directement dans du texte
nom = "Hamza"
score = 95
print(f"L'élève {nom} a obtenu un score de {score}%.")

# --- 3. UTILISER LES VIRGULES ---
# Python ajoute automatiquement un espace entre les éléments
print("Le résultat est", 50, "points.")

# --- 4. LE PARAMÈTRE 'SEP' (SÉPARATEUR) ---
# Modifie ce qui sépare les mots (par défaut c'est un espace)
print("06", "11", "22", "33", "44", sep="-") # Résultat: 06-11-22-33-44

# --- 5. LE PARAMÈTRE 'END' (FIN DE LIGNE) ---
# Empêche le saut de ligne à la fin du print
print("Chargement en cours", end="... ")
print("Terminé !")

# --- 6. CARACTÈRES SPÉCIAUX ---
print("Ligne 1\nLigne 2")       # \n pour sauter une ligne
print("Colonne 1\tColonne 2")   # \t pour une tabulation
print("J'aime le \"Python\"")   # \" pour afficher des guillemets
