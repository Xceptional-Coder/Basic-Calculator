import re

print("Our Basic Calculator")
print("Type 'quit' to Exit\n")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation =""
    if previous == 0:
        equation = input("Enter your mathematical problem:")
    else:
        equation = input(str(previous))


    if equation == 'quit':
        print("So you chose to quit")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

while run:
    performMath()