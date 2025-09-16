class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.speed = 0

    def start(self):
        print(f"{self.brand} car has started.")

    def accelerate(self, increase):
        self.speed += increase
        print(f"{self.brand} is now going at {self.speed} km/h.")

    def stop(self):
        print(f"{self.brand} car has stopped.")
        self.speed = 0
car1 = Car("Tesla", "Red")
car2 = Car("BMW", "Black")

car1.start()
car1.accelerate(50)
car1.stop()

car2.start()
print("############################################")
########################################################
#__init__
class Car:
    def __init__(self, brand, color): 
        self.brand = brand
        self.color = color
        self.speed = 0 

    def start(self):
        print(f"{self.brand} car has started.")

car1 = Car("Tesla", "Red")
car2 = Car("BMW", "Black")

print(car1.brand) 
print(car2.color)  

car1.start()
print("############################################")
##############################################
#__str__ method
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def __str__(self):
        return f"Car(Brand: {self.brand}, Color: {self.color})"

car1 = Car("Tesla", "Red")
car2 = Car("BMW", "Black")

print(car1)
print(car2)
print("############################################")
##############################################
#inheritance
class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print(f"{self.brand} has started.")

    def stop(self):
        print(f"{self.brand} has stopped.")

class Car(Vehicle): 
    def honk(self):
        print(f"{self.brand} is honking! Beep Beep!")

car1 = Car("Tesla", "Red")
car1.start()      
car1.honk()       
car1.stop()  
print("############################################")     
##############################################
#method overriding
class Vehicle:
    def start(self):
        print("Vehicle is starting...")

class Car(Vehicle):
    def start(self):  
        print("Car engine is starting..")

car = Car()
car.start()
print("############################################")
###############################################
#object overloading
class Car:
    def __init__(self, speed):
        self.speed = speed

    def __add__(self, other):
        return self.speed + other.speed

car1 = Car(100)
car2 = Car(150)

print(car1 + car2)
print("############################################")
###############################################
#method overriding
class Payment:
    def process(self):
        print("Processing generic payment...")

class CreditCardPayment(Payment):
    def process(self):  
        print("Processing credit card payment...")

class UpiPayment(Payment):
    def process(self): 
        print("Processing UPI payment...")

payments = [CreditCardPayment(), UpiPayment()]

for payment in payments:
    payment.process()
