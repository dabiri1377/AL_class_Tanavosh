# https://stackoverflow.com/questions/41626379/python-power-set-of-a-list
def powerset(input_set):
    if not input_set:  # Empty list -> empty set
        return [set()]  # Return empty list with a set member

    power_set = []  # Create a empty list
    # Scan every member of input_set and put it in 'input_set_member'
    for input_set_member in input_set:
        set_of_input_set_member = set((input_set_member,))
        for x in powerset(input_set - set_of_input_set_member):
            if x not in power_set:
                power_set.extend([x, x | set_of_input_set_member])
    return power_set

# __main__

# get set from user
input_list_set = set(input('Enter input set\n').split())

print(powerset(input_list_set))
