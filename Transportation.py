# Contains classes for all the different modes of transportation
# The different factors that will affect the viability for a mode of transportation will include: 
#   cost, size of vehicle, time required to start moving, parking, transport time, environmental impact, traffic, 
#   safety, maintainability

class Transportation:
    def __init__(self, name, cost, size, time_to_start, parking, transport_time, environmental_impact, traffic, safety, maintainability, infrastructure, disability_support):
        self.name = name # ex: "train", "car"
        self.cost = cost # scale of 1 - 10
        self.size = size # amount of people supported, give an estimate
        self.time_to_start = time_to_start # time to get on the road, scale of 1-10 , will be lowest for walking and a lot higher for bus or plane
        self.parking = parking # how difficult it is to find parking, scale of 1-10 where 1 is no parking
        self.transport_time = transport_time # scale of 1-10, essentially how quick the transportation tends to be
        self.environmental_impact = environmental_impact # scale of 1 - 10
        self.traffic = traffic # scale of 1 - 10 for how hard it is to navigate in traffic
        self.safety = safety # scale of 1 - 10
        self.maintainability = maintainability # scale of 1 - 10, how much the user would have to input to maintain it
        self.disability_support = disability_support # boolean that determines whether the vehicle supports people who cannot operate a vehicle




