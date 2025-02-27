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



class Mat:
    def __init__(self,num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
        return self.num2 + self.num1
    
    def sub(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divided(self):
        return self.num1 / self.num2
    
mat = Mat(5,10)

print("add:", mat.add())
print("sub:", mat.sub())
print("multiply:", mat.multiply())
print("divided:", mat.divided())
    

