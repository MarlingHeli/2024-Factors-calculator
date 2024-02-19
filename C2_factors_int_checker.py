# generates headings
def statement_generator(statement, decoration):  # prints statement with fancy decoration
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# displays instructions
def instructions():
    statement_generator("The ultimate factor finder", "_")

    print("""Enter an integer (whole number) and I will tell you if it's a unity, 
prime, or perfect square number\n""")


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


# Main routine here
want_instructions = input("Press <enter> to read the instructions or any key to continue ")

if want_instructions == "":
    instructions()

while True:

    to_factor = num_check("To factor: ")
    print("You chose to factor", to_factor, "\n")

    # quit
    if to_factor == "xxx":
        break
