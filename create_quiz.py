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

    while True:
        try:
            choice = int(input("Enter subject number: "))
            select_subject = subjects[choice - 1]

        except (ValueError, IndexError):
            print("Invalid input! Please choose a valid subject number.")
    
menu()
