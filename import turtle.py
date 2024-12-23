import turtle
import pandas

# Set up the screen
screen = turtle.Screen()
screen.title('United States')

# Set the background image
image = 'blank_states_img.gif'
screen.bgpic(image)

# Read the data from the CSV file
data = pandas.read_csv('50_states.csv')
all_state = data.state.to_list()

# Create a turtle object
t = turtle.Turtle()
t.hideturtle()
t.penup()

# Set the turtle shape (fix this)
t.shape('circle')

# Get user input
answer_state = screen.textinput(title='Guess the State', prompt='What\'s another state?')

# Check if the answer is in the list of all states
if answer_state in all_state:
    # Get the row of the state data
    state_data = data[data.state == answer_state]
    x, y = int(state_data.x), int(state_data.y)
    
    # Move the turtle to the correct position and write the state name
    t.goto(x, y)
    t.write(answer_state, align="center", font=("Arial", 10, "normal"))

# Wait for a click to exit
screen.exitonclick()
