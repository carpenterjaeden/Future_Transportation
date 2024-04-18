# Contains classes for all the different types of roadways
class Infrastructure:
    def __init__(self, name, size, traffic, roads):
        self.name = name # "highway", "grid", "few_roads", etc 
        self.size = size # scale of 1-10 depends on user input
        self.traffic = traffic # level of traffic which may be based on user input or just estimated, could maybe take in the time of day instead or something
        self.roads = roads # scale of 1 - 10 of how many roads there are

    # method that takes a user and adjusts the infrastructure to match what they input
    def input_parameters(self, user):



