from abs import ABC, abstractmethod
import math

#Abstract class representing a vehicle
class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model


        #Abstract method to start the vehicle
        @abstractmethod
        def start(self):
            pass

        #Abstract method to stop the vehicle
        def stop(self):
            pass

#Concrete subclass representing a Car
class Car(Vehicle):

    def start(self):
        return f"Starting {self.make} {self.model}..."
    def stop(self):
        return f"Stopping {self.make} {self.model}..."


# Concrete subclass representing a Motorcycle
class Motorcycle(Vehicle):

    def start(self):
        return f"Starting {self.make} {self.model}..."

    def stop(self):
        return f"Stopping {self.make} {self.model}..."


# Main function to demostrate abstraction
def main():
    #Create instances of vehicles
    car = Car("Toyota", "Corolla")
    motorcycle = Motorcycle("Honda", "CB700")

    #Start and stop each vehicle
    print(car.start())
    print(car.stop())
    print(motorcycle.start())
    print(motorcycle.stop)

    if __name__ == "__main__":
        main()