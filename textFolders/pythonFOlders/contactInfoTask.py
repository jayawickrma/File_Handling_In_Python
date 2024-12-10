# create a programme that stores an manage contact.txt each contact every should into name,mobilNumber and email
#FEATURES TO IMPLEMENT
    #add a new contact
        #appent a contact into the file
        #read and display all the contacts in the file
        #exit the programme


def addContact():
    with open("textFolders/contact.txt",'a')as file:
        name =input("Enter name :")
        mobile=input("Enter your mobile number :")
        email=input("Enter your Email Address :")

        file.write(f"{name},{mobile},{email}\n")

def viewContacts():
    with open("textFolders/contact.txt",'r')as file:
        contacts =file.read()
        print(contacts)
  
        
        # if contacts:
        #     print("Here the all values \n\n")
        #     for contact in contacts:
        #         name,mobile,email =contact.strip().split(",")
        #         print("Name:{name} \n Contact :{mobile}\n Email :{email}")

        #     else:
        #         print("Empty sheet !! There are no contacts")

        # else:
        #     print("Couldnt find the Contact.txt file")

while True:
    print("\n--- Contact Manager ---")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Exit")

    try:
        press = int(input("Enter your choice: "))
        if press == 1:
            addContact()
        elif press == 2:
            viewContacts()
        elif press == 3:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")
    except ValueError:
        print("Invalid input! Please enter a valid number.\n")