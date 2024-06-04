from principe import ask_question
from niveaux import level_1, level_2

def main():
    print("Bienvenue dans ce quiz élaboré par Abdessamad." "\nVous devez avoir au moins 6 bonnes réponses pour passer au niveau suivant." "\nJe vous souhaite alors bonne chance !")

    print("\nNiveau 1 :" "\n------------------------")
    score_level1 = level_1()
    if score_level1 >= 6:
        print(f"Félicitations ! Tu as passé le niveau 1 avec {score_level1} bonnes réponses !")
        print("\nNiveau 2 :" "\n------------------------")
        score_level2 = level_2()
        if score_level2 >= 6:
            print(f"Félicitations encore! Tu as passé le niveau 2 avec {score_level2} bonnes réponses !")
        else:
            print(f"Désolé, tu n'as pas réussi à passer le niveau 2. Tu as eu seulement {score_level2} bonnes réponses.")
    else:
        print(f"Désolé, tu n'as pas réussi à passer le niveau 1. Tu as eu seulement {score_level1} bonnes réponses.")
    







if __name__ == "__main__":
    main()