# Liste des mots-clés à rechercher
keywords = [
    "Rotamase", "cell cycle", "cell division", 
    "macromolecule biosynthetic process", "cellular macromolecule biosynthetic process", 
    "cellular macromolecule metabolic process", "macromolecule metabolic process", 
    "Oxidoreductase", "Antibioticbiosynthesis"
]

# Chemin des fichiers d'entrée et de sortie
input_file_path = "/home/nguyeho3/Documents/TP_Naplas/Matrice_finale.txt"
output_file_path = "/home/nguyeho3/Documents/TP_Naplas/output.txt"

# Lecture et écriture des fichiers
with open(input_file_path, "r", encoding="utf-8") as file, open(output_file_path, "w", encoding="utf-8") as output_file:
    for line in file:
        # Vérifie si un des mots-clés est présent dans la ligne
        if any(keyword in line for keyword in keywords):
            output_file.write(line)
