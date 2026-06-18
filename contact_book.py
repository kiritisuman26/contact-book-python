contact = {}
print("Welcome to Contact Book!")
while True:
    print("The features of Contact book are : ")
    print("1. View Contacts")
    print("2. Add Contacts")
    print("3. Search Conatct")
    print("4. Delete Contact")
    print("5. Exit")
    ch = int(input("Enter your choice (1-5): "))
    if ch == 1:
        if not contact:
            print("Contact book is empty")
        else:
            for key,value in contact.items():
                print(f"Name: {key}, Phone no. : {value}")
    elif ch == 2:
        name = input("Enter the name to add in Contact Book : ")
        ph = input("Enter phone number to add in Contact Book : ")
        if name in contact and contact[name] == ph:
            print(f"Name : {name} and phone number : {ph} already exist in Contact Book")
        else:
            contact[name] = ph
            print(f"Name : {name} and phone number : {ph} added in Contact Book")
    elif ch == 3:
        name = input ("Enter the name to search in Contact Book : ")
        if name in contact:
            print(f"Name : {name} found in Contact Book and phone number is : {contact[name]}")
        else:
            print(f"Name : {name} not found in Contact Book")
    elif ch == 4:
        name = input("Enter the name to delete from Contact Book : ")
        if name in contact:
            contact.pop(name) 
            print(f"Name : {name} deleted from Contact Book")
        else:
            print(f"Name : {name} not found in Contact Book")
    elif ch == 5:
        print("Exiting Contact Book. Thank You")
        break
    else: 
        print("Invalid choice. Please enter a valid choice (1-5)")