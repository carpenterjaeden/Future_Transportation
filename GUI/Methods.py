from Infrastructure import Infrastructure
from Transportation import Transportation
from User import User

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
    # 12. description

    mot = [] # array that contains the modes of transportation that will be used for loops
    train = Transportation('train', 3, 70, 7, 0, 7, 2, 1, 6, 0, True, "PROS: Low Cost, Fast Travel Time (destination based), Public Transportation.")
    mot.append(train)
    car =   Transportation('car'  , 6, 4 , 1, 7, 5, 5, 6, 7, 6, False, "PROS: Immediate Start Time, Higher Safety, Private Transportation, Target Destination.") # personal car
    mot.append(car)
    taxi =  Transportation('taxi' , 5, 2 , 4, 0, 5, 5, 6, 5, 0, True, "PROS: No Parking Required, No Maintenance, Private Transportation, Target Destination.") # taxi, uber, etc.
    mot.append(taxi)
    plane = Transportation('plane', 8, 200, 10, 2, 9, 6, 1, 8, 0, True, "PROS: Larger Size, Fast Travel Time (destination based), Public Transportation.")
    mot.append(plane)
    walk =  Transportation('walk', 0, 5, 0, 0, 1, 0, 1, 5, 10, False, "PROS: No Cost, Immediate Start Time, No Parking, Low Environment Impact.") # I assume false for dis_sup?
    mot.append(walk)
    bike =  Transportation('bike', 1, 1, 0, 2, 3, 0, 3, 4, 9, False, "PROS: Low Cost, Immediate Start Time, Low Environmental Impact.")
    mot.append(bike)
    skateboard = Transportation('skateboard', 1, 1, 0, 0, 2, 0, 1, 4, 6, False, "PROS: Low Cost, Immediate Start Time, Low Space Utilization, Low Environmental Impact")
    mot.append(skateboard)
    wheelchair = Transportation('wheelchair', 2, 1, 2, 0, 1, 0, 2, 4, 2, True, "PROS: Low Maintainability Cost, Disability Support.")
    mot.append(wheelchair)    
    rollerblades = Transportation('rollerblades', 2, 1, 1, 0, 2, 0, 1, 3, 6, False, "PROS: Low Cost, Easy Storage, Low Environmental Impact.");
    mot.append(rollerblades)
    parasailing = Transportation('parasailing', 3, 3, 10, 0, 4, 5, 2, 2, 9, True, "PROS: More Direct Route, More Scenic Route, Limited Disability Support")
    mot.append(parasailing);
    motorcycle = Transportation('motorcycle', 4, 1, 4, 5, 4, 4, 4, 3, 7, False, "PROS: Better Traffic Manuverability, Fast Start Time")
    mot.append(motorcycle)
    helicopter = Transportation('helicopter', 7, 4, 7, 4, 7, 6, 1, 7, 0, True, "PROS: Fast Travel Time, Disability Support.")
    mot.append(helicopter)
    emergency_vehicle = Transportation('emergency_vehicle', 10, 2, 1, 0, 10, 7, 1, 9, 0, True, "PROS: Fast Travel Time, Disability Support.")
    mot.append(emergency_vehicle)


    return mot

def set_types_of_infrastructure():
    # 1. name
    # 2. size       --> Depends on User Input (currently has placeholder values) <--
    # 3. traffic    --> Depends on User Input (currently has placeholder values) <--
    # 4. roads
    
    toi = [] # array that contains the types of infrastructure that will be used for loops
    highway = Infrastructure('highway', 3, 5, 2)
    toi.append(highway)
    grid =    Infrastructure('grid', 7, 7, 8)
    toi.append(grid)

    return toi

def initialize_infrastructure(user, toi):
    # set the infrastructure class that is stored in the user variable to the correct infrastructure

    for infrastructure in toi:
        if infrastructure.name == user.infrastructure_name:
            user.infrastructure = infrastructure
            break
    else:
        raise ValueError("Infrastructure not found")
        
    # adjust the infrastructure to fit the user inputs
    user.infrastructure.input_parameters(user)
    return

# perform all the analysis and printing
# takes a user class, an array of modes of transportation, and a boolean true or false value to denote whether to print to console
def analyze_output(user,mot):
    score = {} # dictionary that maps the modes of transportation to their scores
    for trans in mot:
        s = trans.calculate_viability(user, user.infrastructure)
        if s > -10000:
            score[trans] = s
    # sort the scores to provide a list with the top 5 modes of transportation
    top_modes = sorted(score, key=score.get, reverse=True)[:4]
    return top_modes

# prints out the modes of transportation
def print_modes(top_modes):
    outString = "" + "Top modes of transportation: \nHigher values are better\n"
    #print("Top modes of transportation: ")
    #print("Higher values are better")
    for trans in top_modes:
        outString += trans.create_graph() + "\n"
    return outString

# analyzes many different values for the user
def longitudal_analysis(num_tests, mot, toi):
    # initialize all scores to 0
    scores = {trans: 0 for trans in mot}
    for _ in range(num_tests):
        # run analysis for num_tests amount of tests
        user = User.random_parameters()
        initialize_infrastructure(user, toi)
        top_modes = analyze_output(user, mot)
        if top_modes:
            for i in range(len(top_modes)):
                scores[top_modes[i]] += 1
        else:
            print("no top mode")
            print(vars(user))
    return scores

# print out the longitudal analysis scores
def print_scores(scores):
    #print("Scores:")
    outString = "Scores:\n"
    for trans, score in scores.items():
        outString += f"{trans.name}: {score}\n"
        #print(f"{trans.name}: {score}")
    
    return outString


    