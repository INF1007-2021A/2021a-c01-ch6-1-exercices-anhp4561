#!/usr/bin/env python
# -*- coding: utf-8 -*-

def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        liste = []
        for i in range (0,10,1):
            valeur = input ("Entrez une valeur : ")
            liste.append(valeur)
    liste.sort()
    print (liste)
    return liste


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        mot1 = input("Entrez votre premier mot :")
        mot2 = input("Entrez votre deuxième mot :")
    is_ana = False
    word1 =[]
    word2 =[]
    for i in mot1:
        word1.append(i)
    for i in mot2:
        word2.append(i)
    word1.sort()
    word2.sort()
    if (word1 ==word2):
        is_ana = True
    print (is_ana)
    return is_ana


def contains_doubles(items: list) -> bool:
    list_to_set = set()
    for i in items:
        list_to_set.add(i)
    doubles = False
    for i in list_to_set:
        if len (list_to_set) != len (items):
            doubles = True
    return doubles


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    for student in student_grades:
        grades = student_grades[student]
        average = sum(grades)/len(grades)
        student_grades[student] = average
    all_grades = student_grades.values()
    max_grade = max(all_grades)
    max_student = {}
    for student in student_grades:
        if student_grades[student] == max_grade:
            max_student[student] = max_grade
    return max_student


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    dict_list = {}
    for lettre in alphabet:
        counter = 0
        for letter in sentence :
            if letter == lettre:
                counter += 1
        dict_list[lettre] = counter
    print(dict_list)
    frequency = 5
    dict_ord = {}
    for i in dict_list:
        if dict_list[i] >= frequency:
            dict_ord[i] = dict_list[i]
    print(dict_ord)
    sorted_values = sorted(dict_ord.values(), reverse=True)
    dict_ord2 = {}
    for i in sorted_values:
        for k in dict_ord.keys():
            if dict_ord[k] == i:
                dict_ord2[k] = dict_ord[k]
                break
    print(dict_ord2)


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    print("Are both words anagrams of each other ? ",anagrams())

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
