# Contains classes for all the different types of roadways
class Infrastructure:
    def __init__(self, name, size, traffic, roads):
        self.name = name # "highway", "grid", "few_roads", etc 
        self.size = size # scale of 0-10 of how large the system is depends on user input
        self.traffic = traffic # level of traffic which may be based on user input or just estimated, could maybe take in the time of day instead or something
        self.roads = roads # scale of 0 - 10 of how many roads there are

    # method that takes a user and adjusts the infrastructure to match what they input
    def input_parameters(self, user):
        # adjust the size of the infrastructure based on number of miles
        # approximately 1 point per 10 miles
        self.size = int(user.distance/10)
        if self.size > 10:
            self.size = 10
        # set the traffic value equal to the average value between the user-entered value and the initial value
        self.traffic = int((self.traffic+user.traffic)/2)       
        return

