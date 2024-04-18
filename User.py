# Class for the User
# Optimized to have the easiest, fewest questions while still being able to get a good idea for the best mode of transportation
class User:
    def __init__(self, age, distance, time, size, disability, traffic):
        self.age = age # age of user will affect how appropriate some modes of transportation are (ie: under 16 cannot drive)
        self.size = size # number of people travelling
        self.distance = distance # approximate distance in miles
        self.time = time # scale 1-10 of how fast the user wants to go
        self.disability = disability # boolean that determines whether the user cannot operate a motor vehicle
        self.traffic = traffic # scale 1-10

    # method that takes user input and uses it to instatiate the class
    @classmethod
    def input_parameters(cls):
        age = int(input("Enter your age: "))
        distance = float(input("Enter the approximate distance to your destination in miles: "))
        time = float(input("How important is the time of travel (1-10): "))
        size = int(input("Enter the number of people travelling: "))
        disability = bool(input("Are there any impairments or disabilities that affect your ability to operate a motor vehicle? (True/False): "))
        traffic = int(input("What is the estimated amount of traffic? (1-10)"))

        return cls(age, distance, time, size, disability, traffic)
    


