# This program takes inputs from the users until the user stops the program by inputting "stop" to the program
# After the user stops the function the functions outputs the sum of all the integers the user entered

def sum_user_input():
    y = 0
    count = 0
    x = input("Please enter an integer or stop the program by writing \"stop\" ")
    while x != "stop":
        try:
            y += int(x)
            count += 1
        except:
            if x == "stop":
                break
        x = input()
    if (count == 0):
        return "User did not enter any integers"
    return y


print(sum_user_input())
