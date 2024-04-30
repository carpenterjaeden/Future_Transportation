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
    car =   Transportation('car'  , 6, 4 , 1, 7, 5, 5, 6, 7, 6, True, "PROS: Immediate Start Time, Higher Safety, Private Transportation, Target Destination.") # personal car
    mot.append(car)
    taxi =  Transportation('taxi' , 5, 2 , 4, 0, 5, 5, 6, 5, 0, True, "PROS: No Parking Required, No Maintenance, Private Transportation, Target Destination.") # taxi, uber, etc.
    mot.append(taxi)
    plane = Transportation('plane', 8, 200, 8, 2, 9, 6, 1, 8, 0, True, "PROS: Larger Size, Fast Travel Time (destination based), Public Transportation.")
    mot.append(plane)
    walk =  Transportation('walk', 0, 1, 0, 0, 1, 0, 1, 5, 10, False, "PROS: No Cost, Immediate Start Time, No Parking, Low Environment Impact.") # I assume false for dis_sup?
    mot.append(walk)
    bike =  Transportation('bike', 1, 1, 0, 2, 3, 0, 3, 4, 9, False, "PROS: Low Cost, Immediate Start Time, Low Environmental Impact.")
    mot.append(bike)

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
    top_modes = sorted(score, key=score.get, reverse=True)[:5]
    return top_modes

# prints out the modes of transportation
def print_modes(top_modes):
    print("Top modes of transportation: ")
    print("Higher values are better")
    for trans in top_modes:
        trans.create_graph()
    return

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
            scores[top_modes[0]] += 1
        else:
            print("no top mode")
            print(user.disability)
    return scores

# print out the longitudal analysis scores
def print_scores(scores):
    print("Scores:")
    for trans, score in scores.items():
        print(f"{trans.name}: {score}")


    