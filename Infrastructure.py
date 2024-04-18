# Contains classes for all the different types of roadways
# types = "highway", "grid", "few_roads"
# size = "small", "medium", "large"
class Infrastructure:
    def __init__(self, type, size):
        self.type = type
        self.size = size
        self.roads = []



