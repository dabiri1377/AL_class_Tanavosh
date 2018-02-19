def powerset(set):

    p_set = [{}]
    # scan every list member in input list
    for x in set:

        temp_set = {}
        for sub_set in p_set:
            temp_set = sub_set | {x}
            p_set = p_set + [temp_set]

        print(temp_set)

    return p_set


# __main__


input_list_set = {1,2,3}

print(powerset(input_list_set))
