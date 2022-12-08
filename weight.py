Name = input("Name? ")
while Name != "Sean":
    Name = input("What? ")
print("Nice to meet you, " + Name + "!")

Weight = [(input("Weight? "))]
while str(Weight[0]).isnumeric() == False:
    print("Error")
    Weight = [(input("Weight? "))]
Weight2 = float(Weight[0])

Unit = [input("kg or lb? ")]
while Unit[0] != "kg":
    if Unit[0] == "lb":
        break
    else:
        print("Invalid unit")
        Unit = [input("kg or lb? ")]

if Unit[0] == "kg" or "lb":
    if Unit[0] == "kg":
        Weight2 = Weight2 * 2.2
        print("You weigh", "%.2f"%Weight2, "pounds!")
    if Unit[0] == "lb":
        Weight2 = Weight2 / 2.2
        print("You weigh", "%.2f"%Weight2, "kilograms!")