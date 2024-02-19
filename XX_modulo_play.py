for item in range(1, 13): #goes from 1 to 12
    num_lollies = 12
    num_students = item

    #calculations
    division = num_lollies / num_students
    per_student = num_lollies // num_students #// double division gives the integer part of division
    lollies_left = num_lollies % num_students #% modulo gives the remainder

    if lollies_left == 0:
        print(f"{item} is a factor of 12!")

    print(f"Each student gets {per_student} and we have {lollies_left} left over")