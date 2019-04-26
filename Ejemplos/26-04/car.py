class Car:
    def __init__(self, make, model, year=2019):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def print_description(self):
        print(self.make + " " + self.model + " " + str(self.year))

    def update_odometer(self, new_value):
        if new_value < 0:
            print("Can't reduce the odometer")
        else: 
            self.odometer += new_value

    def read_odometer(self):
        print("This car has traveled " + str(self.odometer) + " kilometers")
