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

        file = f"{select_subject}_quiz.txt"

        print(f"\nCreating a quiz for {select_subject}...")
        
        while True:
            # Input question and choices
            question = input("Enter the question: ")
            letters = ['A', 'B', 'C', 'D']

            with open(file, "a") as f:
                f.write(f"Question: {question}\n")
                for letter in letters:
                    choices = input(f"{letter}: ")
                    f.write(f"{letter}: {choices}\n")

                while True:
                    # Input correct answer
                    answer = input("Enter the correct answer (A, B, C, or D): ").upper()
                    if answer in letters:
                        f.write(f"Correct Answer: {answer}\n")
                        f.write("----------\n")
                        break
                    else:
                        print("Invalid input! Please enter A, B, C, or D.")

            print(f"Question for {select_subject} created successfully!")

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
        
menu()
