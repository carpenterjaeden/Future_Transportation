import Infrastructure
import Transportation
import User

# instantiate different modes of transportation (may be moved to a different file)
# instantiate different infrastructures (may be moved to a different file)
# ask for user input by calling a method in user
# name, cost, size, time_to_start, parking, transport_time, env_impact, traffic, safety, maintain, dis_sup
train = Transportation('train', 3, 50, 7, 1, 7, 2, 1, 8, 1, True);
car =   Transportation('car'  , 6, 4 , 3, 7, 5, 5, 6, 7, 6, True);

# this is how to instantiate a user using input parameters
user = User.input_parameters()