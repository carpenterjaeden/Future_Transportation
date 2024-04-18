# Contains classes for all the different modes of transportation
# The different factors that will affect the viability for a mode of transportation will include: 
#   cost, size of vehicle, time required to start moving, parking, transport time, environmental impact, traffic, 
#   safety, maintainability, and how well it works with the infrastructure.
# disability_support is a boolean that determines whether the vehicle supports people who cannot operate a vehicle
class Transportation:
    def __init__(self, name, cost, size, time_to_start, parking, transport_time, environmental_impact, traffic, safety, maintainability, infrastructure, disability_support):
        self.name = name
        self.cost = cost
        self.size = size
        self.time_to_start = time_to_start
        self.parking = parking
        self.transport_time = transport_time
        self.environmental_impact = environmental_impact
        self.traffic = traffic
        self.safety = safety
        self.maintainability = maintainability
        self.infrastructure = infrastructure
        self.disability_support = disability_support




