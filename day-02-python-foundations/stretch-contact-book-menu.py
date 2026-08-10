# Stretch Exercise: Contact Book Menu

contacts = {
    "Anisha": {
        "phone": "123-456-7890",
        "email": "anisha@gmail.com"
    },
    "Ravi": {
        "phone": "987-654-3210",
        "email": "ravi@gmail.com"
    },
    "Maya": {
        "phone": "555-555-5555",
        "email": "maya@gmail.com"
    }
}

# 1 add contact

def add_contact(name, phone, email):
  contacts[name] = {"phone": phone, "email": email}
  print(contacts)

def search_contact(name):
  search_name = name.lower()
  for name, details in contacts.items():
    if name.lower() == search_name:
      return name, details
    else:
      None, "not found"

def delete_contact(name):
  name = name.lower()
  for actual_name, details in contacts.items():
    if actual_name.lower() == name:
      del contacts[actual_name]
      return contacts
    else:
      None, "not found"

def display_all():
  if not contacts:
    print("contacts is empty")
    return
  for name, details in contacts.items():
    print(f"{name}: {details}")


while True:
  print("\nContact Book Menu:")
  print("1. Add Contact")
  print("2. Search Contact")
  print("3. Delete Contact")
  print("4. Display All Contacts")
  print("5. Exit")

  choice = input("What do you want to perform: ")

  if choice == '1':
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    add_contact(name, phone, email)

  elif choice == '2':
    name = input("Enter name to search: ")
    result = search_contact(name)
    print(result)

  elif choice == '3':
    name = input("Enter name to delete: ")
    result = delete_contact(name)
    print(contacts)

  elif choice == '4':
    display_all()

  elif choice == 'break':
    print("Exiting the program")
    break
  else:
    print("Invalid, can only operate in 1 to 5 choices")
