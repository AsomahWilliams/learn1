from datetime import datetime

#class Human:

 #   def __init__(self, color, height,name, age):
    #    self.color = color
    #    self.height = height
     #   self.name = name
     #   self.age = age

   # def print_name(self):  
   #     print(self.name) 



#bob = Human (color="black", height="3.1" , name="bd")
#bob.print_name()

#dad = Human(color= 'yellow', height="1.5", name="sda")
#dad.print_name()







#class Mat:
    #def __init__(self):
    #    pass
    #accept 2 numbers
   # must have method to divid add sub,muiltiply the 2numbers








class Dog:
    def __init__(self, name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("whoof whoof")   

class Owner:
    def __init__(self,name, address, contact_number):
        self.name = name
        self.address = address
        self.contact_number = contact_number

Owner1 = Owner("dar", "123 ablekuma", "+1233554849494")  
dog1 = Dog("fry","gey",Owner1)
#print(dog1.owner.name) 
#print(dog1.owner.address)
#print(dog1.owner.contact_number)

Owner2 = Owner("nay","321 lapaz", "+1234")
dog2 =Dog("rey", "gen",Owner2)
#print(dog2.owner.name)
#print(dog2.owner.address)
#print(dog2.owner.contact_number)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(F"Hello, my name is {self.name} and I am {self.age} years old.")

Person1 = Person("Alice", 30)
#Person1.greet() 

person2 = Person("Bob", 20)
#person2.greet()



class User:
    def __init__(self,username,email, password):
        self.username = username
        self._email = email
        self.password = password

        @property
        def email(self):
            print("Email accesed")   
            return self._email
        

        @email.setter
        def email(self, new_email):
            if"@" in new_email:
                self._email = new_email
        

user1 =User("nana", "nana@gmail.com", "321")
user2 = User("dada", "dada@gmail.com","123")
#user1.email = "this is not an email"
#print(user1.email)


class User:
    user_count = 0

    def __init__(self, username,email):
        self.username = username
        self.email = email
        User.user_count += 1


        def display_user(self):
            print(F"Username:{self.username}, Email: {self.email}")


user1 = User("dan", "gaga@gmail.com")
user2 = User("sa123", "sall123@gmail.com")
#print(User.user_count)
#print(user1.user_count)
#print(user2.user_count)



    
class BankAccount:
    MIN_BALANCE = 100

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self,amount):
        if amount > 0 :
            self._balance += amount
            print(f"{self.owner}'s new balance: ${self._balance} ")
        else:
            print ("Deposit amount must be positive.") 

@staticmethod
def is_valid_interest_rate(rate):
    return 0 <= rate <= 5

account = BankAccount("Alive", 500)   
account.deposit(200)

print(BankAccount.is_valid_interest_rate(3))
print(BankAccount.is_valid_interest_rate(10))
            



       
        