# Functions:
def user_input_ecc(user_input, input_type, option1, option2):
    if input_type == "str":
        while user_input != option1 and user_input != option2:
            print("Error")
            if option2 == 0:
                user_input = input("%s? " % (option1))
            else:
                user_input = input("%s or %s? " % (option1, option2))
        else:
            print("OK")
        return str(user_input)
    if input_type =="int":
        while (user_input).isnumeric() == False:
            print("Error")
            user_input = input("Weight? ")
        else:
            print("OK")
        return float(user_input)

def passcheck(password):
    import sys
    attempts = 5
    passcheck = (input("Password: "))
    if passcheck == password:
        print("Access Granted.")
    while passcheck != password:
        if attempts > 0:
            print("Attempts remaining: " + str(attempts))
            passcheck = (input("Password: "))
            attempts -= 1
        if passcheck == password:
            print("Access Granted.")
            break
        if attempts == 0:
            sys.exit("Access Denied.")
            
def conversion_process():
    global user_unit
    global user_weight
    if user_unit == "kg":
        user_weight = user_weight * 2.2
        print("You weigh", "%.2f"%user_weight, "pounds!")
    if user_unit == "lb":
        user_weight = user_weight / 2.2
        print("You weigh", "%.2f"%user_weight, "kilograms!")

# ----------------------------------------------------------

# Password:
#password1 = (input("Set Password: "))
passcheck(input("Pass?"))

# User Name Information:
user_name = input("Name? ")
print("Nice to meet you, " + user_name + "!")

# User Weight Information:
user_weight = (input("Weight? "))
user_weight = user_input_ecc(user_weight, "int", "Weight ", 0)

# User Unit Information:
user_unit = input("kg or lb? ")
user_unit = user_input_ecc(user_unit, "str", "kg", "lb")
print("You're fat.")

# Unit Conversion Process:
convert = input("Convert units? ")
convert = user_input_ecc(convert, "str", "yes", "no")
if convert == "yes":
    conversion_process()