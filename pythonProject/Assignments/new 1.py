field = input("Enter your field(eng/med):")
percentage = int(input("Enter your percentage:"))
if (field == "eng" and percentage >= 80):
    print("You can get admission in NED")
elif (field == "eng" and percentage < 80):
    print("You cannot get admission in NED")
elif (field == "med" and percentage >= 85):
    print("You can get admission in DOW")
elif (field == "med" and percentage < 85):
    print("You cannot get admission in DOW")


