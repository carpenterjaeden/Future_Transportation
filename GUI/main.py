from User import User
from Methods import *
from args_setup import args
import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()
mot = set_modes_of_transportation()
toi = set_types_of_infrastructure()

# Set up the screen dimensions and font
WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Infrastructure Simulation")
font = pygame.font.Font(None, 32)
smallerFont = pygame.font.Font(None, 16)

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)

# Text rendering function
def draw_text(text, x, y):
    rendered_text = font.render(text, True, BLACK)
    screen.blit(rendered_text, (x, y))

def draw_user_info(user):
    while True:
        initialize_infrastructure(user, toi)
        # complete the analysis and print
        top_modes = analyze_output(user, mot)
        screen.fill(WHITE)

        # Render multiline text
        text_lines = print_modes(top_modes).split('\n')
        y_offset = 50
        for line in text_lines:
            rendered_text = smallerFont.render(line, True, BLACK)
            screen.blit(rendered_text, (50, y_offset))
            y_offset += rendered_text.get_rect().height + 5  # Add some vertical spacing

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                return


def draw_test_info(transport):
    while True:
        screen.fill(WHITE)
        lines = transport.split('\n')
        y = 50
        for line in lines:
            rendered_text = smallerFont.render(line, True, BLACK)
            screen.blit(rendered_text, (50, y))
            y += rendered_text.get_rect().height + 5  # Add some vertical spacing

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                return


# Main menu options
options = ["Create New User", "Generate Random User", "Run Longitudinal Tests"]
selected_option = 0  # Default selected option index

# Main game loop
running = True
while running:
    screen.fill(WHITE)  # Fill the screen with white

    # Display main menu options
    menu_y = 200
    for i, option in enumerate(options):
        if i == selected_option:
            draw_text(">> " + option + " <<", 100, menu_y)
        else:
            draw_text(option, 150, menu_y)
        menu_y += 40

    # Update the display
    pygame.display.update()

    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()
        elif event.type == KEYDOWN:
            if event.key == K_DOWN:  # Move selection down
                selected_option = (selected_option + 1) % len(options)
            elif event.key == K_UP:  # Move selection up
                selected_option = (selected_option - 1) % len(options)
            elif event.key == K_RETURN:  # Select option
                if selected_option == 0:  # Create New User
                    #print("Create New User selected")
                    input_fields = {
                        "Age": "",
                        "Distance (Miles)": "",
                        "Time (Importance 0-10)": "",
                        "Size of Party": "",
                        "Disability (True/False)": "",
                        "Traffic (0-10)": "",
                        "Cost (Importance 0-10)": "",
                        "Infrastructure (highway/grid)": ""
                    }
                    active_field = None  # Currently active input field (None initially)

                    # Main game loop
                    inputting = True
                    while inputting:
                        screen.fill(WHITE)  # Fill the screen with white

                        # Display input fields and labels
                        input_y = 100
                        for key, value in input_fields.items():
                            draw_text(f"{key}:", 100, input_y)
                            pygame.draw.rect(screen, BLACK, pygame.Rect(600, input_y - 5, 200, 30), 2)  # Input field
                            if active_field == key:
                                pygame.draw.rect(screen, GRAY, pygame.Rect(600, input_y - 5, 200, 30))  # Highlight active field
                            draw_text(value, 605, input_y)
                            input_y += 40
                        pygame.draw.rect(screen, GREEN, pygame.Rect(350, 550, 100, 50))
                        draw_text("Create", 360, 550)

                        # Update the display
                        pygame.display.update()

                        # Handle events
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                inputting = False
                            elif event.type == MOUSEBUTTONDOWN:
                                # Check if mouse click is within an input field
                                if pygame.Rect(350, 550, 100, 50).collidepoint(event.pos):  # Check if "Create" button is clicked
                                    # Create a user with entered data (add your user creation logic here)
                                    #print("User created with data:", input_fields)
                                    createdUser = User(int(input_fields["Age"]),float(input_fields["Distance (Miles)"]),float(input_fields["Time (Importance 0-10)"]),int(input_fields["Size of Party"]),input_fields["Disability (True/False)"],int(input_fields["Traffic (0-10)"]),int(input_fields["Cost (Importance 0-10)"]),input_fields["Infrastructure (highway/grid)"])
                                    draw_user_info(createdUser)
                                    
                                active_field = None
                                input_y = 100
                                for key, value in input_fields.items():
                                    field_rect = pygame.Rect(600, input_y, 100, 30)
                                    if field_rect.collidepoint(event.pos):
                                        #print("selected field" + key)
                                        active_field = key
                                    input_y += 40
                            elif event.type == KEYDOWN:
                                if active_field:
                                    if event.key == K_BACKSPACE:
                                        input_fields[active_field] = input_fields[active_field][:-1]
                                    elif event.key == K_RETURN:
                                        try:
                                            # Convert input to int or float if possible
                                            if "." in input_fields[active_field]:
                                                input_fields[active_field] = float(input_fields[active_field])
                                            else:
                                                input_fields[active_field] = int(input_fields[active_field])
                                        except ValueError:
                                            # Handle invalid input (non-numeric)
                                            input_fields[active_field] = ""  # Clear the input field
                                        active_field = None  # Deactivate the field after processing Enter
                                    else:
                                        input_fields[active_field] += event.unicode
                elif selected_option == 1:  # Generate Random User
                    #print("Generate Random User selected")
                    user = User.random_parameters()
                    draw_user_info(user)
                elif selected_option == 2:  # Run Longitudinal Tests
                    print("Run Longitudinal Tests selected")
                    active = False
                    numitems = ""
                    inputting = True
                    while inputting:
                        screen.fill(WHITE)
                        draw_text("Enter Number of Tests:", 100, 100)
                        pygame.draw.rect(screen, BLACK,pygame.Rect(500, 100-5, 200, 30), 2)
                        if active:
                            pygame.draw.rect(screen, GRAY, pygame.Rect(500, 100 - 5, 200, 30))  # Highlight active field
                        draw_text(numitems, 500, 100)
                        draw_text("Submit", 250, 250)
                        pygame.display.update()

                        for event in pygame.event.get():
                            if event.type == QUIT:
                                inputting = False
                            elif event.type == MOUSEBUTTONDOWN:
                                # Check if mouse click is within an input field
                                if pygame.Rect(500, 100, 200, 30).collidepoint(event.pos):  # Check if Tile is selected
                                    active = True
                                elif pygame.Rect(250, 250, 100, 50).collidepoint(event.pos):  # Check if submit
                                    scores = longitudal_analysis(int(numitems), mot, toi)
                                    draw_test_info(print_scores(scores))
                            elif event.type == KEYDOWN:
                                if active:
                                    if event.key == K_BACKSPACE:
                                        numitems = numitems[:-1]
                                    elif event.key == K_RETURN:
                                        try:
                                            # Convert input to int 
                                            numitems = int(numitems)
                                        except ValueError:
                                            # Handle invalid input (non-numeric)
                                            numitems = ""  # Clear the input field
                                        active = False  # Deactivate the field after processing Enter
                                    else:
                                        numitems += event.unicode





# Quit Pygame
pygame.quit()

##################################################################
###### BELOW is original implementation using the terminal #######
##################################################################
# instantiate different modes of transportation (may be moved to a different file)
# instantiate different infrastructures (may be moved to a different file)
# ask for user input by calling a method in user

# mot = set_modes_of_transportation()
# toi = set_types_of_infrastructure()

# if args.random:
#     # instantiate a user using random parameters
#     user = User.random_parameters()
#     # adjust the transportation class based on user input parameters
#     initialize_infrastructure(user, toi)
#     # complete the analysis and print
#     top_modes = analyze_output(user, mot)
#     print_modes(top_modes)
# elif args.la is not None:
#     # longitudal analysis
#     num_tests = args.la
#     scores = longitudal_analysis(num_tests, mot, toi)
#     print_scores(scores)
# elif args.user:
#     # instantiate a user using parameters input in the command console
#     user = User.input_parameters()
#     # adjust the transportation class based on user input parameters
#     initialize_infrastructure(user, toi)
#     # complete the analysis and print
#     top_modes = analyze_output(user, mot)
#     print_modes(top_modes)
# else:
#     print("args error")





