from model.contact import Contact

class ContactUI:
    def __init__(self):
        print("Welcome to the Contact Book application!")
        self.contacts = []

    def run(self):
        while True:
            self.display_menu()
            selection = int(input("What would you like to do? "))
        
            if selection == 1:
                new_contact = self.create_contact()
                self.contacts.append(new_contact)
                print(f"{new_contact.get_full_name()} has been created and added to the contact book")
                continue
            elif selection == 2:
                self.display_contacts()
                continue
            elif selection == 3:
                self.update_contact()
                continue                
            elif selection == 4:
                self.delete_contact()
                continue
            elif selection == 5:
                print("Thank you for using the application! Goodbye!")
                break
            else:
                print("That is not a valid selection. Please try again")

    def display_menu(self):
        print("\n1 - Create contact")
        print("2 - Display contacts")
        print("3 - Update contact")
        print("4 - Delete contact")
        print("5 - Exit")

    def create_contact(self):
        print("\n~~~ Create Contact ~~~")
        first = input("First name: ").strip()
        last = input("Last name: ").strip()
        primary_phone = input("Primary phone number: ").strip()
        secondary_phone = input("Secondary phone number (optional): ").strip()
        email = input("Email address: ").strip()
        address = input("Address line (#### Example Road): ").strip()
        city = input("Address city: ").strip()
        state = input("Address state: ").strip()
        zip_code = input("Address zip code: ").strip()
        myContact = Contact(first, last, primary_phone, email, address, city, state, zip_code, secondary_phone)
        
        return myContact
    
    def display_contacts(self):
        if len(self.contacts) > 0:
            print("\nContacts:")
            for contact in self.contacts:
                print(contact.to_string())
        else:
            print("There are no contacts to display")
    
    def get_contact(self, first, last):
        for contact in self.contacts:
            if contact.first_name.lower() == first.lower() and contact.last_name.lower() == last.lower():
                return contact
        return False
    
    def delete_contact(self):
        if len(self.contacts) > 0:
            print("\n~~~ Delete Contact ~~~")
            first = input("Contact first name: ").strip()
            last = input("Contact last name: ").strip()
            my_contact = self.get_contact(first, last)
            if my_contact == False:
                print("That contact is not in the contact book")                
            else:
                self.contacts.remove(my_contact)
                print(f"{first} {last} has been removed")
        else:
            print("There are no contacts to delete")

    def update_contact(self):
        if len(self.contacts) > 0:
            print("\n~~~ Update Contact ~~~")
            first = input("Contact first name: ").strip()
            last = input("Contact last name: ").strip()
            my_contact = self.get_contact(first, last)
            if my_contact == False:
                print("That contact is not in the contact book")                
            else:
                # Update Contact here
                index = self.contacts.index(my_contact)
                self.contacts.remove(my_contact)  
                new_contact = self.create_contact()              
                self.contacts.insert(index, new_contact)
                print(f"{new_contact.first_name} {new_contact.last_name} has been updated")
        else:
            print("There are no contacts to update")