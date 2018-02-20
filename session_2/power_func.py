# with set
def powerset(input_set, print_set=False):
    """
     Get a set as a list and output a list as powerset
    :param input_set:
     Input set as a list
    :param print_set:
     If want to print final powerset this is True
    :return:
    Powerset as output list
    """
    power_set = [[]]  # create a list with [] member(all set's have [] member)

    # scan every list member in input list
    for first_set_members in input_set:

        temp_list = []  # create a empty temp list
        # for_debug
        print("first_set_members =", first_set_members)

        # scan every member of output list
        for sub_list in power_set:
            # Add first_set_members into every power_set member and add \
            # it to temp list
            temp_list += [sub_list + [first_set_members]]
            # for_debug
            print("sub_list =", sub_list)
            print("temp_list =", temp_list)

        # add temp list to output list
        power_set.extend(temp_list)
        # for_debug
        print("power_set = ",power_set)
        print()

    # sort output list with python sort func.
    power_set.sort()

    # print output powerset if you want
    if print_set:
        print(power_set)

    # return output list
    return power_set


# __main__


# get set from user
input_list_set = input('Enter input set\n').split()

# ask for print powerset
powerset_print = input('Do you want to print powerset?')
if powerset_print == 'no' or powerset_print == 'n':
    powerset_print = 0

# exception handling
try:
    powerset(input_list_set, powerset_print)
except Exception:
    print("something wrong")
    print(Exception)
