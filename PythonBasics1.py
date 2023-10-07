class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def start_engine(self):
        print("The engine has started.")

my_car = Car(make="Toyota", model="Camry", year=2022)

print(my_car.make)
print(my_car.model)
print(my_car.year)
my_car.start_engine()