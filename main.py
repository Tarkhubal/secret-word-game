from random import *


# La liste des mots dans laquelle l'ordinateur devra en choisir un pour que l'utilisateur le trouve
def words_list():
    global var_words_lst
    var_words_lst = ["Abandon", "Abattre", "Envoyer", "Discord", "Appuyer", "Estimer", "Bazooka", "Balayer", "Cyclope", "Culture", "Crouton", "Croquer", "Cristal", "Carotte",
                     "Anglais", "Abricot", "Drakkar", "Anxieux", "Achever", "Grizzly", "Whiskey", "Aileron", "Aboyeur", "Abeille", "Italien", "Laitage", "Polluer", "Records", "Ottoman", "Moroses"]
    return var_words_lst


# Décompose le mot que l'utilisateur a entré en une liste de caractères
def decomposer(user_word):
    var_caracteres_list = []
    for i in range(len(user_word)):
        var_caracteres_list.append(user_word[i])
    return var_caracteres_list


# On convertit les lettres en mot
def assembler(var_caracteres_list):
    global var_composed_word
    var_composed_word = var_caracteres_list[0] + var_caracteres_list[1] + var_caracteres_list[2] + \
        var_caracteres_list[3] + var_caracteres_list[4] + \
        var_caracteres_list[5] + var_caracteres_list[6]
    return str(var_composed_word)


# Je ne comprends plus ce qu'il a fait
def exe(input_user_word):
    varMain_user_score = [""] * 7

    words_list()
    varMain_user_word = input_user_word
    assert len(varMain_user_word) < 7 or len(
        varMain_user_word) > 7, "Le mot doit contenir 7 lettres."
    varMain_random_word = ["Abandon", "Abattre", "Envoyer", "Discord", "Appuyer", "Estimer", "Bazooka", "Balayer", "Cyclope", "Culture", "Crouton", "Croquer", "Cristal", "Carotte",
                           "Anglais", "Abricot", "Drakkar", "Anxieux", "Achever", "Grizzly", "Whiskey", "Aileron", "Aboyeur", "Abeille", "Italien", "Laitage", "Polluer", "Records", "Ottoman", "Moroses"][randint(0, 29)]  # L'ordinateur choisi un mot aléatoire dans la liste de 30 mots

    # -dev- # print(varMain_random_word)
    # -dev- # varMain_user_word = input("Entrez un mot : ")

    varMain_user_word.lower()
    varMain_random_word.lower()
    if varMain_user_word in varMain_random_word:
        return "Bravo, vous avez trouvé le mot!"
    else:
        varMain_userword_caracteres_list = decomposer(
            varMain_user_word)
        # -dev- # print(varMain_userword_caracteres_list)
        varMain_randomword_caracteres_list = decomposer(
            varMain_random_word)
        # -dev- # print(varMain_randomword_caracteres_list)
        for i in range(len(varMain_userword_caracteres_list)):
            if varMain_user_word[i].lower() == varMain_random_word[i].lower():
                varMain_user_score[i] = varMain_random_word[i]
                # -dev- # print("correct letter" + str(i))
            else:
                varMain_user_score[i] = "_"
                # -dev- # print("incorrect letter" + str(i))

        varMain_user_score = assembler(varMain_user_score)

    return "User word : " + str(varMain_user_word) + "\nWord of the program : " + str(varMain_random_word) + "\nCorrected answer : " + str(varMain_user_score)


print(exe("Pomme"))

# Les Fonctions :
# - words_list()
# - decomposer(user_word: String)
# - assembler(var_caracteres_list: List (String))
# - exe(input_user_word: String)

# Les Variables :
# - var_words_lst
# - var_result_word
# - var_caracteres_list
# - var_composed_word
# - varMain_words_lst
# - varMain_user_word
# - varMain_random_word
