from typing import NewType


class Users:
    def __init__(self, first_name, surname, email, password):
        self.first_name = first_name
        self.surname = surname
        self.email = email
        self.password = password

    def check_email(self, email):
        if email.find("@")!=-1:
            print("Valid Email")
        else:
            print("Invalid Email")

    def check_password(self, password):
        if (any(x.isupper() for x in password) and any(x.islower() for x in password) and any(x.isdigit() for x in password) and (len(password) >= 6) and len(password) <= 12):
            print("Valid Password")
        else:
            print("Invalid Password")
   

josh = Users("Joshua", "Mendel", "jmendel123@gmail.com", "17834Y")

josh.check_email(josh.email)
josh.check_password(josh.password)
    

        
