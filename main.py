from User import User
from Methods import *
from args_setup import args

# instantiate different modes of transportation (may be moved to a different file)
# instantiate different infrastructures (may be moved to a different file)
# ask for user input by calling a method in user

mot = set_modes_of_transportation(args.offroad)
toi = set_types_of_infrastructure()

if args.random:
    # instantiate a user using random parameters
    user = User.random_parameters()
    # adjust the transportation class based on user input parameters
    initialize_infrastructure(user, toi)
    # complete the analysis and print
    top_modes = analyze_output(user, mot)
    print_modes(top_modes)
elif args.la is not None:
    # longitudal analysis
    num_tests = args.la
    scores = longitudal_analysis(num_tests, mot, toi)
    print_scores(scores)
elif args.user:
    # instantiate a user using parameters input in the command console
    user = User.input_parameters()
    # adjust the transportation class based on user input parameters
    initialize_infrastructure(user, toi)
    # complete the analysis and print
    top_modes = analyze_output(user, mot)
    print_modes(top_modes)
else:
    print("args error")





