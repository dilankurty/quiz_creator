import os
import json
import random
import platform

# clear the console screen based on the OS
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# main menu system
def menu():
    while True:
        print("\nWelcome to Quizard!")
        print("[1] Create a quiz")
        print("[2] Take a quiz")
        print("[3] Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            create_quiz()
        elif choice == "2":
            print("Coming soon...")
        elif choice == "3":
            print("Thank you for using Quizard! See you next time!")
            exit()
        else:
            print("Invalid input! Please choose between 1 - 3.")

# create a quiz system
def create_quiz():
    subjects = ["Science", "Math", "History", "Values", "General Knowledge"]

    while True:  # Loop to allow re-selecting categories
        print("Choose a subject for the quiz:")
        for index, subject in enumerate(subjects, 1):
            print(f"{index}. {subject}")

        # Subject selection
        while True:
            try:
                choice = int(input("Enter subject number: "))
                select_subject = subjects[choice - 1]
                break
            except (ValueError, IndexError):
                print("Invalid input! Please choose a valid subject number.")

        file = f"{select_subject.lower()}_quiz.json"

        # Check if the file exists, if not create it
        if os.path.exists(file):
            with open(file, "r") as f:
                quiz_data = json.load(f)

        else:
            quiz_data = []
                

        print(f"\nCreating a quiz for {select_subject}...")

        while True:
            # Input question and choices
            question = input("Enter the question: ")
            letters = ['A', 'B', 'C', 'D']
            choices = {}

            for letter in letters:
                choices[letter] = input(f"Enter choice {letter}: ")

            while True:
                # Input correct answer
                answer = input("Enter the correct answer (A, B, C, or D): ").upper()
                if answer in letters:
                    break
                else:
                    print("Invalid input! Please enter A, B, C, or D.")

            new_question = {
                "question": question,
                "choices": choices,
                "answer": answer
            }

            quiz_data.append(new_question)

            with open(file, "w") as f:
                json.dump(quiz_data, f, indent=4)

            print(f"Question for {select_subject} created successfully to {file}!")

            # Ask if the user wants to continue, go back to the menu, or select another category
            while True:
                cont = input("\nDo you want to: \n[1] Add another question \n[2] Go back to the menu \n[3] Select another category\nEnter your choice: ")
                if cont == '1':
                    break  # Add another question
                elif cont == '2':
                    return  # Go back to the main menu
                elif cont == '3':
                    break  # Break out of the inner loop to re-select category
                else:
                    print("Invalid choice! Please enter 1, 2, or 3.")

            if cont == '3':
                break  # Break out of the outer loop to re-select category
        
# take a quiz system
def take_quiz():
    # list of available quizzes
    quiz_files = [file for file in os.listdir() if file.endswith("_quiz.json")]
    if not quiz_files:
        print("No quizzes available. Please create one first.")
        return
    
    print("\nAvailable quizzes:")
    for index, file in enumerate(quiz_files, 1):
        subject = file.replace("_quiz.json", "")
        print(f"[{index}] {subject.title()}")

    while True:
        try:
            choice = int(input("Select a quiz by number: "))
            quiz_file = quiz_files[choice - 1]
            subject = quiz_file.replace("_quiz.json", "").title()
            break
        except (ValueError, IndexError):
            print("Invalid input! Please choose a valid quiz number.")

    # Load the shuffled questions from the selected quiz file
    with open(quiz_file, "r") as f:
        questions = json.load(f)
    if not questions:
        print("No questions available in this quiz.")
        return
    
    random.shuffle(questions)

    # start the quiz
    print(f"\nStarting the {subject.title()} quiz...\n")
    score = 0
    total = len(questions)

    for index, question in enumerate(questions, 1):
        print(f"\nQ{index}: {question['question']}")
        for key, value in question['choices'].items():
            print(f"{key}: {value}")

    while True:
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        if answer in ['A', 'B', 'C', 'D']:
            break
        else:
            print("Invalid input! Please enter A, B, C, or D.")

    if answer == question['answer']:
        print("Correct!")
        score += 1
    else:
        correct_answer = question['choices'][question['answer']]
        print(f"Wrong! The correct answer is {question['answer']}: {correct_answer}")

    # display the score
    print(f"\nYou got {score}/{total} correct. Your score: {round(score/total*100, 2)}%")

    # ask user for their name and save the score to the leaderboard
    name = input("Enter your name for the leaderboard: ").strip()
    leaderboard_file = "leaderboard.json"

    if os.path.exists(leaderboard_file):
        with open(leaderboard_file, "r") as f:
            leaderboards = json.load(f)

    else:
        leaderboards = {}

    if subject not in leaderboards:
        leaderboards[subject] = []

    leaderboards[subject].append({"name": name, "score": score, "total": total})
    # arrange the leaderboard in ascending order
    leaderboards[subject].sort(key=lambda x: x['score'], reverse=True)
    
    with open(leaderboard_file, "w") as f:
        json.dump(leaderboards, f, indent=4)

    # show the top 5 for the specific subject
    print(f"\n🏆 {subject.title()} Quiz Leaderboard:")
    for index, entry in enumerate(all_leaderboards[subject][:5], 1):
        print(f"{index}. {entry['name']} - {entry['score']}/{entry['total']}")

    print("\nThank you for taking the quiz!")
    input("\nPress Enter to return to menu...")

menu()
