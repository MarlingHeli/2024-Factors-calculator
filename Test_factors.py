#works out factors and returns a sorted list
def factor(to_factor):
    all_factors = []

    for item in range(1, (to_factor+1)): #range is from 1 to to_factor
        factor_pair = to_factor // item #get the number that pairs with a factor
        is_factor = to_factor % item #get remainder

        if is_factor == 0: #if no remainders, then is factor
            if item not in all_factors and factor_pair not in all_factors: #checks if factor and its pair exist in the list already
                all_factors.append(item)
                all_factors.append(factor_pair)
                all_factors.sort()  # sort from smallest to biggest
                print(f"{item} and {factor_pair} are factors of {to_factor}!")

    print("Factors:", all_factors)


to_factor = int(input("Enter an integer to factor: "))
if to_factor != 1:
    all_factors = factor(to_factor)
