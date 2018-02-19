def odd_sum(min_number, max_number=None):
    if max_number is None:
        max_number = min_number
        min_number = 0

    print("min =", min_number)
    print("max= ", max_number)
    sum_of_odd_number = 0
    for numbers in range(min_number, max_number + 1):
        print("number =", numbers)
        if (numbers % 2) == 1:
            sum_of_odd_number += numbers

    print(sum_of_odd_number)
    return sum_of_odd_number


odd_sum(3)
