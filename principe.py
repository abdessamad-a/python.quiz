#Cette fonction affiche la question et les options, et demande à l'utilisateur d'entrer la lettre qui correspond à la bonne réponse.

def ask_question(question, options, correct_answer):
    print(question)
    for option in options:
        print(option)
    answer = input("Enter (A, B, C, D): ").upper()
    if answer == correct_answer:
        print("\nBonne réponse !" "\n-----------------------")
        return True
    else:
        print("\nFaux ! La réponse est : ", correct_answer, "\n-----------------------")
        return False
    



