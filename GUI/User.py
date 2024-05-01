import random
# Class for the User
# Optimized to have the easiest, fewest questions while still being able to get a good idea for the best mode of transportation
class User:
    def __init__(self, age, distance, time, size, disability, traffic, cost, infrastructure_name):
        self.age = age # age of user will affect how appropriate some modes of transportation are (ie: under 16 cannot drive)
        self.size = size # number of people travelling
        self.distance = distance # approximate distance in miles
        self.time = time # scale 0-10 of how fast the user wants to go
        self.disability = disability # boolean that determines whether the user cannot operate a motor vehicle
        self.traffic = traffic # scale 0-10
        self.cost = cost # scale of 0-10 to determine how important the cost is for the user
        self.infrastructure_name = infrastructure_name # name of the infrastructure
        self.infrastructure = None # infrastructure class

    # method that takes user input and uses it to instatiate the class
    @classmethod
    def input_parameters(cls):
        age = int(input("Enter your age: "))
        distance = float(input("Enter the approximate distance to your destination in miles: "))
        time = float(input("How important is the time of travel (0-10): "))
        size = int(input("Enter the number of people travelling: "))
        disability_input = input("Are there any impairments or disabilities that affect your ability to operate a motor vehicle? (True/False): ")
        disability = (disability_input.lower() == 'true')
        traffic = int(input("What is the estimated amount of traffic? (0-10): "))
        cost = int(input("How important is the cost? (0-10): "))
        infrastructure_name = input("What kind of infrastructure are you travelling in? highway or grid: ")

        return cls(age, distance, time, size, disability, traffic, cost, infrastructure_name)
    
    @classmethod
    def random_parameters(cls):
        age = random.randint(15, 80)
        distance = random.randint(1, 100)
        time = random.randint(0, 10)
        size = random.randint(1, 10)
        disability = random.choice([True, False])
        traffic = random.randint(0, 10)
        cost = random.randint(0, 10)
        infrastructure_name = random.choice(['highway', 'grid'])

        return cls(age, distance, time, size, disability, traffic, cost, infrastructure_name)
    


