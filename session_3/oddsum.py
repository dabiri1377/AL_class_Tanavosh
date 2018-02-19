def odd_sum(min_number, max_number=None):

    # exception handeling
    try:
        if max_number is None:
            max_number = int(min_number)
            min_number = int(0)
        else:
            max_number = int(max_number)
            min_number = int(min_number)
    except Exception:
        # user input char
        print("unvalid input")
        return None

    print("min =", min_number)
    print("max= ", max_number)
    sum_of_odd_number = 0
    for numbers in range(min_number, max_number + 1):
        print("number =", numbers)
        if (numbers % 2) == 1:
            sum_of_odd_number += numbers

    print(sum_of_odd_number)
    return sum_of_odd_number


def last_odd_number(number):
    return 2 * ((number - 1) // 2) + 1





min_n,max_n = input("enter min and max").split()
odd_sum(min_n, max_n)

