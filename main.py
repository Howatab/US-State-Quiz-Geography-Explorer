import pandas
import turtle
import time
#setup
data = pandas.read_csv("50_states.csv")
states = data['state'].str.lower()
print(states)

screen  = turtle.Screen()
screen.tracer(0)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#user_inputs

def user_input():
    User_input = screen.textinput(title="Enter a State Name " , prompt= "Enter a US State name ")
    print(User_input)
    return User_input


#comparing_inputs
def Comparing(User_input):
    
    if User_input.lower() in states.values:
        cor = data[data["state"].str.lower() == User_input.lower()]
        print(cor['x'])
        write_state_name(User_input=User_input , x=int(cor['x']) , y=int(cor['y']))
        return True

#Displaying_name 
def write_state_name(User_input,x,y):
    writer = turtle.Turtle()
    writer.shape('circle')
    writer.shapesize(0.2,0.2)
    writer.penup()
    writer.goto(x,y)
    writer.write(User_input)
    screen.update()

score_turtle = turtle.Turtle()
score_turtle.penup()
score_turtle.hideturtle()
font = ("Arial" , 14 , "bold")

#display Score
def display_score(score):
    score_turtle.goto(-300,250)
    score_turtle.clear()
    score_turtle.write(f"States answered : {score}",font=font)
    score_turtle.goto(150,250)
    score_turtle.write(f"States left : {50- score}",font=font)


game_over = False
score = 0
answered_states = []


while not game_over:
    display_score(score)
    screen.update()
    input = user_input()
    if input == 'exit':
        break
    if Comparing(input):
        score += 1
        answered_states.append(input)
        if score == 50:
            game_over = True
            
    time.sleep(2)
    
unanswered_state = []
unanswered_state_dict  = {'Unanswred states'  : []}
for item in states.values:
    if item not in answered_states:
        unanswered_state.append(item)

unanswered_state_dict['Unanswred states'].extend(unanswered_state)

df = pandas.DataFrame.from_dict(unanswered_state_dict)
df.to_csv("Unanswered States ")

screen.bye()
turtle.mainloop()