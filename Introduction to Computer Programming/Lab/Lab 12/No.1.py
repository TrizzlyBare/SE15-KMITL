phonebook = {}

while True:
    def add_contact():
        name = input("Enter name: ")
        number = input("Enter number: ")
        phonebook[name] = number

    def delete_contact():
        name = input("Enter name: ")
        if name in phonebook:
            del phonebook[name]
        else:
            print("Contact not found")
        
    def search_contact():
        name = input("Enter name: ")
        if name in phonebook:
            print(name, ":", phonebook[name])
        else:
            print("Contact not found")
        
    def print_all_contacts():
        for name, number in phonebook.items():
            print(name, ":", number)

    def quit():
        print("Goodbye")
        exit()

    def main():
        print("+. Add contact")
        print("-. Delete contact")
        print("f. Search contact")
        print("p. Print all contacts")
        print("q. Quit")
        choice = input("Enter your choice: ")
        if choice == "+":
            add_contact()
        elif choice == "-":
            delete_contact()
        elif choice == "f":
            search_contact()
        elif choice == "p":
            print_all_contacts()
        elif choice == "q":
            quit()
        else:
            print("Invalid choice")
        
    main()