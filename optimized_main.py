from random import *

# Les variables :
# - input_user_word : Le mot entré par l'utilisateur
# - random_word : Le mot choisi aléatoirement par le programme
# - user_score : Le score de l'utilisateur
# - userword_lettering_list : La liste des caractères du mot de l'utilisateur
# - final_user_score : Le score final de l'utilisateur (avec les lettres trouvées et les lettres non trouvées (remplacées par des "_"))


def exe(input_user_word):       # Fonction principale

    # Vérifie si le mot fait 7 lettres sinon affiche une erreur
    assert len(input_user_word) == 7, "Le mot doit contenir 7 lettres."

    random_word = ["Abandon", "Abattre", "Envoyer", "Discord", "Appuyer", "Estimer", "Bazooka", "Balayer", "Cyclope", "Culture", "Crouton", "Croquer", "Cristal", "Carotte",
                   "Anglais", "Abricot", "Drakkar", "Anxieux", "Achever", "Grizzly", "Whiskey", "Aileron", "Aboyeur", "Abeille", "Italien", "Laitage", "Polluer", "Records",
                   "Ottoman", "Moroses"][randint(0, 29)]  # Génère une lise de mots et en choisit un aléatoirement

    ### >>> DEV DEBUG <<< ###
    # random_word = ["Polluer", "Polluer"][randint(0, 1)]
    ### >>> END DEBUG <<< ###

    input_user_word = input_user_word.lower()                       # | On met les mots en minuscule
    random_word = random_word.lower()                               # |
    
    if input_user_word in random_word:                              # Si le mot de l'utilisateur est exactement le mot du programme
        return "Bravo, vous avez trouvé le mot!"                    # On retourne un message de félicitation
    else:                                                           # Sinon
        userword_lettering_list = []                                # Création d'une liste vide
        for i in range(len(input_user_word)):                       # Pour chaque lettre du mot de l'utilisateur
            userword_lettering_list.append(input_user_word[i])      # On ajoute la lettre à la liste

        user_score = [""] * 7                                       # Création d'une liste de 7 cases vides
        for i in range(len(userword_lettering_list)):               # Pour chaque lettre du mot de l'utilisateur
            if input_user_word[i] == random_word[i]:                # Si la lettre est égale à la lettre du mot du programme qui est à la même position dans le mot
                user_score[i] = random_word[i]                      # Alors on ajoute la lettre du mot du programme à la liste
            else:                                                   # Sinon
                user_score[i] = "_"                                 # On ajoute un "_" à la liste (à la place de la lettre du mot du programme)

        final_user_score = ""                                       # Création d'une variable vide pour le score final de l'utilisateur
        for eachletter in range(len(user_score)):                   # Pour chaque lettre de la liste du résultat du score de l'utilisateur
            final_user_score += user_score[eachletter]              # On assemble les lettres de la liste dans la variable en un string

    return "User word : " + str(input_user_word) + "\nWord of the program : " + str(random_word) + "\nCorrected answer : " + str(final_user_score)
    # On retourne le mot de l'utilisateur, le mot du programme et le résultat du score de l'utilisateur


# On appelle la fonction avec le mot de l'utilisateur en argument
print(exe("PopluAR"))

# [Non nécessaire] On attend que l'utilisateur appuie sur Entrée pour fermer le programme
exit = input("Press Enter to exit.")
