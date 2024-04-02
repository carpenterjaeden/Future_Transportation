# Contains classes for all the different types of roadways
class Infrastructure:
    def __init__(self, type, size):
        self.type = type
        self.size = size
        self.roads = []

    def add_road(self, road):
        self.roads.append(road)

    def initialize_infrastructure(self):
        if self.type == "grid":
            # Create a grid-like structure of roads
            for i in range(self.size):
                for j in range(self.size):
                    self.add_road(Road(f"Road {i}-{j}"))
                    if i < self.size - 1:
                        self.add_road(Road(f"Avenue {i}-{j}"))
        elif self.type == "highway":
            

class Road:
    def __init__(self, name):
        self.name = name


