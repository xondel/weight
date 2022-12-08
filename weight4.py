# FUNCTIONS -----------------------------------------------------------------

def user_input_ecc(user_input, required_input_type, option1, option2):
    if required_input_type == "str":
        while user_input != option1 and user_input != option2:
            print("Error")
            if option2 == 0:
                user_input = input("%s? " % (option1))
            else:
                user_input = input("%s or %s? " % (option1, option2))
        else:
            print("OK")
        return str(user_input)
    if required_input_type =="int":
        while (user_input).isnumeric() == False:
            print("Error")
            user_input = input("Weight? ")
        else:
            print("OK")
        return float(user_input)

def passcheck(password):
    import sys
    attempts = 5
    passcheck = (input("Confirm password: "))
    if passcheck == password:
        print("Access Granted.")
    while passcheck != password:
        if attempts > 0:
            print("Attempts remaining: " + str(attempts))
            passcheck = (input("Confirm password: "))
            attempts -= 1
        if passcheck == password:
            print("Access Granted.")
            break
        if attempts == 0:
            sys.exit("Access Denied.")
            
def conversion_process(weight, unit):
    if unit == "kg":
        weight = weight * 2.2
        print("You weigh", "%.2f"%weight, "pounds!")
    if unit == "lb":
        weight = weight / 2.2
        print("You weigh", "%.2f"%weight, "kilograms!")

# SYSTEMS ------------------------------------------------------------------------

def system1():
    # Password:
    password1 = input("Set password: ")
    passcheck(password1)

    # User Name Information:
    user_name = input("Name? ")
    print("Nice to meet you, " + user_name + "!")

    # User Weight Information:
    user_weight = user_input_ecc((input("Weight? ")), "int", "Weight ", 0)

    # User Unit Information:
    user_unit = user_input_ecc(input("kg or lb? "), "str", "kg", "lb")
    print("You're fat.")

    # Update Password:
    print("Your password broke when you sat on it.")
    password2 = input("Set new password: ")

    # Unit Conversion Process:
    convert = user_input_ecc(input("Convert units? "), "str", "yes", "no")
    if convert == "yes":
        print("Confirm password to see result.")
        passcheck(password2)
        conversion_process(user_weight, user_unit)
    else:
        really = "really"
        while convert == "no":
            print("You should, you're %s fat." % (really))
            convert = user_input_ecc(input("Convert units? "), "str", "yes", "no")
            really += str(", really")
            if convert == "yes":
                print("Confirm password to see result.")
                passcheck(password2)
                conversion_process(user_weight, user_unit)

# RUNTIMES ------------------------------------------------------------------------

system1()