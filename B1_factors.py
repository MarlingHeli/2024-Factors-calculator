# generates headings
def statement_generator(statement, decoration):  # prints statement with fancy decoration
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# displays instructions
def instructions():
    statement_generator("The ultimate factor finder", "_")

    print("""Enter an integer (whole number) and I will tell you if it's a unity, 
prime, or perfect square number\nPress 'xxx' to quit\n""")


# check whether input is an integer between 1 and 200
def num_check(question):
    error = "Please enter an integer\n"
    while True:

        response = input(question).lower()
        if response == "xxx":  # check if user quits
            return response

        try:
            # ask user for a number
            response = int(response)

            if 1 <= response <= 200:  # check that response is within 1 to 200
                return response  # ends loop
            elif response < 1:
                print("Please enter an integer that is more than (or equal to) 1\n")
            elif response > 200:
                print("Please enter an integer that is less than (or equal to) 200\n")

        except ValueError:  # prevents string input
            print(error)

#works out factors and returns a sorted list
def factor(var_to_factor):
    all_factors = []

    for item in range(1, (to_factor+1)): #range is from 1 to to_factor
        factor_pair = to_factor // item #get the number that pairs with a factor (item)
        is_factor = to_factor % item #get remainder

        if is_factor == 0: #if no remainders, then is factor
            if item not in all_factors: #checks if factor and its pair exist in the list already
                all_factors.append(item)
            if factor_pair not in all_factors:
                all_factors.append(factor_pair)
            all_factors.sort()  # sort from smallest to biggest
                #print(f"{item} and {factor_pair} are factors of {to_factor}!")

    return all_factors

# Main routine here
want_instructions = input("Press <enter> to read the instructions or any key to continue ")

if want_instructions == "":
    instructions()

while True:

    comment = ""

    #ask user what number they want to factor

    to_factor = num_check("Enter an integer to factor (or press 'xxx' to quit): ")

    # quit
    if to_factor == "xxx":
        break

    #get factors for integers that are 2 or more. 1 is a unity number
    elif to_factor != 1:
        all_factors = factor(to_factor)

    #comment for unity
    else:
        all_factors = ""
        comment = "One is a unity number. It only has one factor which is itself.\n"

    #comments for squares/primes

    #prime numbers have two factors only
    if len(all_factors) == 2:
        comment = f"{to_factor} is a prime number.\n"

    #check if the list has an odd amount of items
    elif len(all_factors) % 2 == 1:
        comment = f"{to_factor} is a perfect square\n"

    #headings
    if to_factor > 1:
        heading = f"Factors of {to_factor}"
    else:
        heading = "One is special."

    #output factors and comments
    statement_generator(heading, "*")
    print(all_factors)
    print(comment)

print("Thank you for using the factors calculator")

