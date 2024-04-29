from User import User
from Methods import set_modes_of_transportation,set_types_of_infrastructure,initialize_infrastructure,analyze_output

# instantiate different modes of transportation (may be moved to a different file)
# instantiate different infrastructures (may be moved to a different file)
# ask for user input by calling a method in user

mot = set_modes_of_transportation()
toi = set_types_of_infrastructure()

# instantiate a user using parameters input in the command console
# user = User.input_parameters()

# instantiate a user using random parameters
user = User.random_parameters()

# adjust the transportation class based on user input parameters
initialize_infrastructure(user, toi)

# complete the analysis and print
analyze_output(user, mot, True)

