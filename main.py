import Infrastructure
import Transportation
import User
import Methods

# instantiate different modes of transportation (may be moved to a different file)
# instantiate different infrastructures (may be moved to a different file)
# ask for user input by calling a method in user

mot = Methods.set_modes_of_transportation()

# this is how to instantiate a user using input parameters
user = User.input_parameters()