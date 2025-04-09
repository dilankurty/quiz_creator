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

    print("Choose a subject for the quiz:")
    for index, subject in enumerate(subjects, 1):
        print(f"{index}. {subject}")

    # subject selection
    while True:
        try:
            choice = int(input("Enter subject number: "))
            select_subject = subjects[choice - 1]

        except (ValueError, IndexError):
            print("Invalid input! Please choose a valid subject number.")
    
        file = f"{select_subject}_quiz.txt"

        print(f"\nCreating a quiz for {select_subject}...")

        while True:
            # Input question and choices
            question = input("Enter the question: ")

            with open(file, "a") as f:
                f.write(f"Question: {question}\n")

            letters = ['A', 'B', 'C', 'D']
            for letter in letters:
                choices = input(f"{letter}: ")
                with open(file, "a") as f:
                    f.write(f"{letter}: {choices}\n")
        
            while True:
                # Input correct answer
                answer = input("Enter the correct answer: ").upper()
                if answer in letters:
                    with open(file, "a") as f:
                        f.write(f"Correct Answer: {answer}\n")
                    break
                else:
                    print("Invalid input! Please enter A, B, C, or D.")

            print(f"Question for {select_subject} created successfully!")

            cont = input("Do you want to add another question? (y/n): ").lower()
            if cont != 'y':
                pass
            elif cont == 'n':
                break
        

menu()
