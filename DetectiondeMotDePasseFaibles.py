def verifierMotDePasse(mdp):
    caracteresSpeciaux = "@;,._*&#"
    
    if not mdp: 
        return "Vous devez entrer un mot de passe."
    
    if len(mdp) < 12 or len(mdp) > 64:
        return "Votre mot de passe doit être entre 12 et 64 caractères."

    maj, min, chiffre, special = 0, 0, 0, 0

    for c in mdp:
        if c in caracteresSpeciaux:
            special += 1
        elif 'A' <= c <= 'Z':
            maj += 1
        elif 'a' <= c <= 'z':
            min += 1
        elif '0' <= c <= '9':
            chiffre += 1

    manquants = ""

    if maj == 0:
        manquants += "une majuscule, "
    if min == 0:
        manquants += "une minuscule, "
    if chiffre == 0:
        manquants += "un chiffre, "
    if special == 0:
        manquants += "un caractère spécial (@ ; , . _ * & #), "

    if manquants:
        return "Il manque " + manquants[:-2] + "."

    types_present = 0
    if maj > 0:
        types_present += 1
    if min > 0:
        types_present += 1
    if chiffre > 0:
        types_present += 1
    if special > 0:
        types_present += 1

    if types_present == 1:
        return "Le mot de passe est trop simple. Il doit contenir au moins deux types de caractères (majuscules, minuscules, chiffres, caractères spéciaux)."

    return "Mot de passe valide et sécurisé !"

print(verifierMotDePasse(input("Veuillez entrer votre mot de passe : ")))
