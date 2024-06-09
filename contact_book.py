class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number, email):
        self.contacts[name] = {'number': number, 'email': email}
        print(f"Contact {name} added successfully!")

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} removed successfully!")
        else:
            print(f"Contact {name} not found!")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"Name: {name}, Number: {self.contacts[name]['number']}, Email: {self.contacts[name]['email']}")
        else:
            print(f"Contact {name} not found!")

    def display_contacts(self):
        if self.contacts:
            print("Contacts:")
            for name, info in self.contacts.items():
                print(f"Name: {name}, Number: {info['number']}, Email: {info['email']}")
        else:
            print("Contact book is empty!")

def main():
    contact_book = ContactBook()

    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Search Contact")
        print("4. Display Contacts")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter contact name: ")
            number = input("Enter contact number: ")
            email = input("Enter contact email: ")
            contact_book.add_contact(name, number, email)
        elif choice == "2":
            name = input("Enter contact name to remove: ")
            contact_book.remove_contact(name)
        elif choice == "3":
            name = input("Enter contact name to search: ")
            contact_book.search_contact(name)
        elif choice == "4":
            contact_book.display_contacts()
        elif choice == "5":
            print("Exiting contact book.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
