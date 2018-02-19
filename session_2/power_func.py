def powerset(input_list, print_set=False):
    """
     Get a set as a list and output a list as powerset
    :param input_list:
     Input set as a list
    :param print_set:
     If want to print final powerset this is True
    :return:
    Powerset as output list
    """
    output_list = [[]]  # create a list with [] member(all set's have [] member)

    # scan every list member in input list
    for list_member in input_list:

        temp_list = []  # create a empty temp list
        # for_debug
        print("list_member =", list_member)

        # scan every member of output list
        for sub_list in output_list:
            # Add list_member into every output_list member and add \
            # it to temp list
            temp_list += [sub_list + [list_member]]
            # for_debug
            print("sub_list =", sub_list)
            print("temp_list =", temp_list)

        # add temp list to output list
        output_list.extend(temp_list)
        # for_debug
        print("output_list = ",output_list)
        print()

    # sort output list with python sort func.
    output_list.sort()

    # print output powerset if you want
    if print_set:
        print(output_list)

    # return output list
    return output_list


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
