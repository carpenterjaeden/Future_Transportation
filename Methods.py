import Infrastructure
import Transportation
import User

def set_modes_of_transportation():
    # name, cost, size, time_to_start, parking, transport_time, env_impact, traffic, safety, maintain, dis_sup

    mot = [] # array that contains the modes of transportation that will be used for loops
    train = Transportation('train', 3, 50, 7, 1, 7, 2, 1, 8, 1, True)
    mot.append(train)
    car =   Transportation('car'  , 6, 4 , 3, 7, 5, 5, 6, 7, 6, True)
    mot.append(car)

    return mot