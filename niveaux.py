#Ces fonctions contiennent les questions, les options ainsi que la lettre de la bonne réponse.

from principe import ask_question

def level_1():
    questions = [
        ("Quelle est la capitale du Maroc ?", ["A. Berlin", "B. Istanbul", "C. Rabat", "D. Islamabad"], "C"),
        ("Quelle est la monnaie utilisée au Royaume-Uni ?", ["A. L'Euro", "B. Le Yen", "C. Le Riyal", "D. La Livre sterling"], "D"),
        ("Qui a écrit 'Les misérables' ?", ["A. Guy de Maupassant", "B. Victor Hugo", "C. Honoré de Balzac", "D. Albert Camus"], "B"),
        ("Laquelle parmi ces propositions est une ville ?", ["A. Pékin", "B. Japon", "C. Mozambique", "D. Islande"], "A"),
        ("Quelle planète est surnommée 'La planète rouge' ?", ["A. Mars", "B. La Terre", "C. Neptune", "D. Mercure"], "A"),
        ("Combien de joueurs y a-t-il dans une équipe de football ?", ["A. 7", "B. 8", "C. 10", "D. 11"], "D"),
        ("En quelle année a débuté la seconde guerre mondiale ?", ["A. 1945", "B. 1936", "C. 1939", "D. 1914"], "C"),
        ("Comment s'appelle le tournoi populaire de tennis se déroulant fin-Printemps à Paris ?", ["A. Martin-Garrix", "B. Rolland-Garros", "C. Paris Tour", "D. Wimbledon"], "B"),
        ("Quelle est la couleur du rubis ?", ["A. Vert", "B. Jaune", "C. Bleu", "D. Rouge"], "D"),
        ("Quelle spécialité n'est pas française ?", ["A. Le croissant", "B. Le fromage", "C. Les sushis", "D. Le vin"], "C")
    ]
    correct_count = 0
    for question, options, answer in questions:
        if ask_question(question, options, answer):
            correct_count += 1
    return correct_count


def level_2():
    questions = [
        ("En quelle année Christophe Colomb a-t-il découvert l'Amérique ?", ["A. 1592", "B. 1378", "C. 1492", "D. 1678"], "C"),
        ("Quelle est la capitale des Etats-Unis ?", ["A. Washington DC", "B. New York", "C. Los Angeles", "D. Miami"], "A"),
        ("En quelle année l'Union soviétique s'est-elle dissoute ?", ["A. 1989", "B. 1990", "C. 1991", "D. 1992"], "C"),
        ("Quel physicien est célèbre pour sa théorie de la relativité ?", ["A. Archimède", "B. Isaac Newton", "C. André-Marie Ampère", "D. Albert Einstein"], "D"),
        ("Quelle planète est la plus proche de la Terre ?", ["A. Mars", "B. La Terre", "C. Neptune", "D. Mercure"], "D"),
        ("Combien de coupes du monde le Brésil a-t-il gagné ?", ["A. 3", "B. 5", "C. 7", "D. 8"], "B"),
        ("Comment s'appelle l'étoile la plus brillante ?", ["A. Sirius", "B. Capella", "C. Arcturus", "D. Véga"], "A"),
        ("Quelle est la langue officiel du Mexique ?", ["A. L'arabe", "B. L'anglais", "C. L'espagnol", "D. Le portugais"], "C"),
        ("Quelle est la couleur des émeraudes ?", ["A. Vert", "B. Jaune", "C. Bleu", "D. Blanc"], "A"),
        ("Combien y a-t-il de jours dans une année bissextile ?", ["A. 365", "B. 366", "C. 367", "D. 364"], "B")
    ]
    correct_count = 0
    for question, options, answer in questions:
        if ask_question(question, options, answer):
            correct_count += 1
    return correct_count