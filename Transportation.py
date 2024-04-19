# Contains classes for all the different modes of transportation
# The different factors that will affect the viability for a mode of transportation will include: 
#   cost, size of vehicle, time required to start moving, parking, transport time, environmental impact, traffic, 
#   safety, maintainability

class Transportation:
    def __init__(self, name, cost, size, time_to_start, parking, transport_time, environmental_impact, traffic, safety, maintainability, disability_support, description=""):
        self.name = name # ex: "train", "car"
        self.cost = cost # scale of 0 - 10
        self.size = size # amount of people supported, give an estimate
        self.time_to_start = time_to_start # time to get on the road, scale of 0-10 , will be lowest for walking and a lot higher for bus or plane
        self.parking = parking # how difficult it is to find parking, scale of 0-10 where 1 is no parking
        self.transport_time = transport_time # scale of 0-10, essentially how quick the transportation tends to be
        self.environmental_impact = environmental_impact # scale of 0 - 10
        self.traffic = traffic # scale of 0 - 10 for how hard it is to navigate in traffic
        self.safety = safety # scale of 0 - 10
        self.maintainability = maintainability # scale of 0 - 10, how much the user would have to input to maintain it
        self.disability_support = disability_support # boolean that determines whether the vehicle supports people who cannot operate a vehicle
        self.description = description # 1 or 2 sentences that describe the benefits of the mode of transport to the user
        # maybe add an age range

    def create_graph(self):
        # will print the proper display for the mode of transportation
        # Ex: Car:
        #     cost ######
        #     time ####
        #     comfortability ####
        # There may be more shown, but the idea is that cost is the price of use (cost and maintainability)
        # Time is from out the door to the destination
        # comfortability includes traffic, parking, environmental impact
        # may add something in regards to disability support

        cost = 2*self.cost + 2*self.maintainability + self.parking # max value of 50
        time = self.parking + self.time_to_start + self.transport_time # max value of 30
        comfortability = self.parking + self.environmental_impact + self.safety + self.traffic + 5 * self.disability_support # max value of 45

        def print_val(name,value, max): # function to print the hashes
            inc = max/10 # denotes how much each hash is worth (1/10 of the max value)
            num_hashes = int(value/inc) # ensure num_hashes is an integer
            print(name + ": ", end="")
            for _ in range(num_hashes):
                print("#", end="")
            print()  # Print a newline after all hashes have been printed

        print(self.name + ":")
        print_val(name = "Cost", value = cost, max=50)
        print_val(name = "Time", value = time, max=50)
        print_val(name = "Comfort", value = comfortability, max=50)        
        return

    def calculate_viability(self, user, infrastructure):
        # based on the user and the infrastructure, there will be a rating given to the mode of transportation
        # user: age, distance, time, size, disability, traffic
        # infrastructure: name, size, traffic, roads

        # score based on user
        score = 0 # higher the score, the higher the viability
        if (user.size < self.size):
            score -= 1000
        if (user.disability != self.disability_support):
            score -= 1000
        score -= user.traffic * self.traffic * 2
        score += user.time * (self.parking + self.time_to_start + self.transport_time)
        score -= user.cost * (self.cost + self.maintainability + self.parking)
        score -= 2 * self.environmental_impact
        # score based on infrastructure

        return score