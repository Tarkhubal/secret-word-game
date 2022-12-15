from random import *
import sys

# Les variables :
# - input_user_word : Le mot entré par l'utilisateur
# - random_word : Le mot choisi aléatoirement par le programme
# - user_score : Le score de l'utilisateur
# - userword_lettering_list : La liste des caractères du mot de l'utilisateur
# - final_user_score : Le score final de l'utilisateur (avec les lettres trouvées et les lettres non trouvées (remplacées par des "#"))


class ansi():
    def color(bg, fg, style):
        return "\33[{bg};{fg};{style}m".format(bg=bg, fg=fg, style=style)


def exe(input_user_word):       # Fonction principale d'exécution
    assert type(input_user_word) == str, "Votre valeur doit être un mot (string) ! (only_string)"
    assert not(" " in input_user_word), "Votre valeur ne doit pas contenir d'espace ! (no_space_in_input)"
    assert len(input_user_word) == 7, "Le mot doit contenir 7 lettres. (only_7_letters)"

    random_word = ["Abandon", "Abattre", "Envoyer", "Discord", "Appuyer", "Estimer", "Bazooka", "Balayer", "Cyclope", "Culture", "Crouton", "Croquer", "Cristal", "Carotte",
                   "Anglais", "Abricot", "Drakkar", "Anxieux", "Achever", "Grizzly", "Whiskey", "Aileron", "Aboyeur", "Abeille", "Italien", "Laitage", "Polluer", "Records",
                   "Ottoman", "Moroses"][randint(0, 29)]  # Génère une lise de mots et en choisit un aléatoirement

    ### >>> DEV DEBUG <<< ###
    # random_word = ["Polluer", "Polluer"][randint(0, 1)]
    ### >>> END DEBUG <<< ###

    input_user_word = input_user_word.lower()                                                   # | On met les mots en minuscule
    random_word = random_word.lower()                                                           # |
    
    if input_user_word in random_word:                                                          # Si le mot de l'utilisateur est exactement le mot du programme
        return ansi.color(7, 49, 32) + "Bravo vous avez trouvé le mot!" + ansi.color(0, 49, 39) # On retourne un message de félicitation
    else:                                                                                       # Sinon
        userword_lettering_list = []                                                            # Création d'une liste vide
        for i in range(len(input_user_word)):                                                   # Pour chaque lettre du mot de l'utilisateur
            userword_lettering_list.append(input_user_word[i])                                  # On ajoute la lettre à la liste

        user_score = [""] * 7                                                                   # Création d'une liste de 7 cases vides
        for i in range(len(userword_lettering_list)):                                           # Pour chaque lettre du mot de l'utilisateur
            if input_user_word[i] == random_word[i]:                                            # Si la lettre est égale à la lettre du mot du programme qui est à la même position dans le mot
                user_score[i] = ansi.color(0, 49, 32) + random_word[i] + ansi.color(0,49,39)    # Alors on ajoute la lettre du mot du programme à la liste
            else:                                                                               # Sinon
                user_score[i] = ansi.color(5, 49, 31) + "#" + ansi.color(0, 49, 39)             # On ajoute un "#" à la liste (à la place de la lettre du mot du programme)

        final_user_score = ""                                       # Création d'une variable vide pour le score final de l'utilisateur
        for eachletter in range(len(user_score)):                   # Pour chaque lettre de la liste du résultat du score de l'utilisateur
            final_user_score += user_score[eachletter]              # On assemble les lettres de la liste dans la variable en un string

    return "User word : " + str(input_user_word.capitalize()) + "\nWord of the program : " + str(random_word.capitalize()) + "\nCorrected answer : " + str(final_user_score)
    # On retourne le mot de l'utilisateur, le mot du programme et le résultat du score de l'utilisateur


# On appelle la fonction avec le mot de l'utilisateur en argument
sys.stdout.write(exe("IZFHN PZOGJZ"))

# [Non nécessaire] On attend que l'utilisateur appuie sur Entrée pour fermer le programme
exit = input("\nPress Enter to exit.")
