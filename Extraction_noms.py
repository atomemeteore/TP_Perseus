

liste = ["Rotamase","cell cycle", "cell division", "macromolecule biosynthetic process", "cellular macromolecule biosynthetic process", "cellular macromolecule metabolic process","macromolecule metabolic process", "Oxidoreductase","Antibioticbiosynthesis"]
with open ("G:\Mon Drive\CCB4\Analyse de données en sciences omiques\TP_NAPLAS\Results Stats sur Log\Matrice_finale.txt","r") as file :
    with open("G:\Mon Drive\CCB4\Analyse de données en sciences omiques\TP_NAPLAS\Results Stats sur Log\output.txt","w") as outputFile:
        for line in file and i in liste:
            if i in line : 
                outputFile.write(line)

