import Infrastructure
import Transportation
import User

def set_modes_of_transportation():
    # 1. name
    # 2. cost 
    # 3. size
    # 4. time_to_start
    # 5. parking
    # 6. transport_time
    # 7. env_impact
    # 8. traffic
    # 9. safety
    # 10. maintain
    # 11. dis_sup

    mot = [] # array that contains the modes of transportation that will be used for loops
    train = Transportation('train', 3, 70, 7, 0, 7, 2, 1, 6, 0, True)
    mot.append(train)
    car =   Transportation('car'  , 6, 4 , 1, 7, 5, 5, 6, 7, 6, True) # personal car
    mot.append(car)
    taxi =  Transportation('taxi' , 5, 2 , 4, 0, 5, 5, 6, 5, 0, True) # taxi, uber, etc.
    mot.append(taxi)
    plane = Transportation('plane', 8, 200, 8, 2, 9, 6, 1, 8, 0, True)
    mot.append(plane)
    walk =  Transportation('walk', 0, 1, 0, 0, 9, 0, 1, 5, 10, False) # I assume false for dis_sup?
    mot.append(walk)
    bike =  Transportation('bike', 1, 1, 0, 2, 8, 0, 3, 4, 9, False)
    mot.append(bike)

    return mot