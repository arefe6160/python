from collections import defaultdict

class contactbook:
    """ A simple contact book application to add, view, update, and delete contacts.
    Each contact consists of a name, phone number, and an optional email address.
    Attributes:
        contact (defaultdict): A dictionary to store contacts with names as keys and
        their details (phone and email) as values.
    Methods:
        add(name: str, phone: str, email: str = None): Adds a new contact to the contact book.
        view(): Displays all contacts in the contact book.
        delete(name: str): Deletes a contact from the contact book by name.
        update(name: str, phone: str = None, email: str = None): Updates    
        the details of an existing contact.
    """
    def __init__(self):
        self.contact=defaultdict(dict)

    def add(self,name : str,phone : str,email = None):
        if name in self.contact:
            print("contact already exist!")

        self.contact[name]['phone']= phone
        self.contact[name]['email']=email
    def view(self):
        for name, info in self.contact.items():
            print(f"name:{name}")
            print(f"phone: {info['phone']}")
            print(f"email:{info['email']}")
            print('-'*50)
    def delete(self,name : str):
        if name in self.contact:
            del self.contact[name]
            print("delete successfuly")
        else:
            print("cantact not found!")
    def update(self,name : str,phone = None,email = None):
        if name in self.contact:
            if phone:
                self.contact[name]['phone'] = phone
            if email:
                self.contact[name]['email'] = email
            return
        print("contact not found!")

if __name__ =='__main__':
    book = contactbook()

while True:
    print("welcome to contact book app")
    print("1. add")
    print("2. edit")
    print("3. view")
    print("4. delete")
    print("5. quit")

    user_choice = input("choose an object:")

    if user_choice == '5':
        break
    if user_choice == '1':
        name = input("name:")
        phone = input("phone:")   
        email = input("email:")

        book.add(name,phone,email)
        
    if user_choice == '2':
        name = input("name:")
        phone = input("phone:")   
        email = input("email:")

        book.update(name,phone,email)

    if user_choice == '3':
        book.view()
        
    if user_choice == '4':
        name = input("name:")

        book.delete(name)
