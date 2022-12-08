# Functions:
def user_name_ecc():
    global user_name
    while user_name != "Sean":
        user_name = input("Who? ")

def user_weight_ecc():
    global user_weight
    while (user_weight).isnumeric() == False:
        print("Error")
        user_weight = (input("Weight? "))

def user_unit_ecc():
    global user_unit
    while user_unit != "kg" and user_unit != "lb":
        print("Invalid unit")
        user_unit = input("kg or lb? ")

def user_str_ecc(x,y,z):
    while x != "y" and x != "z":
        print("Error")
        x = input("%s or %s" % (x,y))

def convert_ecc():
    global convert
    while convert != "yes" and convert != "no":
        convert = input("yes or no motherfucker? ")

def conversion_process():
    global user_unit
    global user_weight
    if user_unit == "kg":
        user_weight = user_weight * 2.2
        print("You weigh", "%.2f"%user_weight, "pounds!")
    if user_unit == "lb":
        user_weight = user_weight / 2.2
        print("You weigh", "%.2f"%user_weight, "kilograms!")

# Merge ECC functions into one?
# ----------------------------------------------------------

# User Name Information:
user_name = input("Name? ")
user_name_ecc()
print("Nice to meet you, " + user_name + "!")

# User Weight Information:
user_weight = (input("Weight? "))
user_weight_ecc()
user_weight = float(user_weight)

# User Unit Information:
user_unit = input("kg or lb? ")
user_unit_ecc()
print("You're fat.")

# Unit Conversion Process:
convert = input("Convert units? ")
convert_ecc()
if convert == "yes":
    conversion_process()