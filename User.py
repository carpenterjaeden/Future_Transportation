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
        age = distance = time = size = disability_input = traffic = cost = infrastructure_name = None
        while age is None:
            try:
                age = int(input("Enter your age: "))
                if age < 0:
                    raise ValueError("Your age should be greater than -1.")
            except ValueError:
                print("Please enter a valid age.")
                age = None;
        # age = int(input("Enter your age: "))
        # distance = float(input("Enter the approximate distance to your destination in miles: "))
        # time = float(input("How important is the time of travel (0-10): "))
        # size = int(input("Enter the number of people travelling: "))
        # disability_input = input("Are there any impairments or disabilities that affect your ability to operate a motor vehicle? (True/False): ")
        # disability = (disability_input.lower() == 'true')
        # traffic = int(input("What is the estimated amount of traffic? (0-10): "))
        # cost = int(input("How important is the cost? (0-10): "))
        # infrastructure_name = input("What kind of infrastructure are you travelling in? highway or grid: ")
        
        while distance is None:
            try:
                distance = float(input("Enter the approximate distance to your destination in miles: "))
                if distance < 0:
                    raise ValueError("Time distance should be greater than 0.")
            except ValueError:
                print("Please enter a valid distance.")
                distance = None
    
        while time is None:
            try:
                time = float(input("How important is the time of travel from lowest to highest priority (0-10): "))
                if time < 0 or time > 10:
                    raise ValueError("Time importance should be between 0 and 10.")
            except ValueError as e:
                print(e)
                time = None
    
        while size is None:
            try:
                size = int(input("Enter the number of people travelling: "))
                if size < 0:
                    raise ValueError("There should be more than 0 people traveling.")
            except ValueError:
                print("Please enter a valid number of people.")
                size = None

        while disability_input is None:
            try:
                disability_input = input("Are there any impairments or disabilities that affect your ability to operate a motor vehicle? (True/False): ")
                if disability_input.lower() not in ['true', 'false']:
                    raise ValueError("Please enter 'True' or 'False'.")
            except ValueError:
                print("Please enter True or False.")
                disability_input = None

        while traffic is None:
            try:
                traffic = int(input("What is the estimated amount of traffic from lowest to highest? (0-10): "))
                if traffic < 0 or traffic > 10:
                    raise ValueError("Traffic estimate should be between 0 and 10.")
            except ValueError as e:
                print(e)
                traffic = None

        while cost is None:
            try:
                cost = int(input("How important is the cost from lowest priority to highest? (0-10): "))
                if cost < 0 or cost > 10:
                    raise ValueError("Cost importance should be between 0 and 10.")
            except ValueError as e:
                print(e)
                cost = None

        while infrastructure_name is None:
            try:
                infrastructure_name = input("What kind of infrastructure are you travelling in? highway or grid: ")
                if infrastructure_name.lower() not in ['highway', 'grid']:
                    raise ValueError("Please enter 'highway' or 'grid'.")
            except ValueError as e:
                print(e)
                infrastructure_name = None

        return cls(age, distance, time, size, disability_input, traffic, cost, infrastructure_name)
    
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
    


