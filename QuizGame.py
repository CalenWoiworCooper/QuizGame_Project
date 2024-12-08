def quiz_game():
    # List of questions and answers
    questions = [
      {
            "question": "Which year Liberia was founded?",
            "options": ["A) 1944", "B) 1872", "C) 1822", "D) R2024"],
            "answer": "C"
        },
        {
            "question": "Who is Liberia current President?",
            "options": ["A) George Weah", "B) Prince Johnson", "C) Charles Taylor", "D) Joseph Boikai"],
            "answer": "D"
        },
        {
            "question": "What is the name of your current math instructor'?",
            "options": ["A) James Lee", "B) Emmanuel Dolokele", "C) Cooper George", "D) Calen Cooper"],
            "answer": "D"
        },
        {
             "question": "Where is the Starz University Located'?",
            "options": ["A) Coffe Town", "B) Old road", "C) Airfield", "D) Gsa road"],
            "answer": "C"
        }
    ] 

    score = 0

    print("Welcome to the Quiz Game!")
    print("Answer the following questions:")

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        answer = input("Your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}.")

    print(f"\nYour final score is {score} out of {len(questions)}.")


# Start the game
quiz_game()
 
