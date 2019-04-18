def menu_list(input_cuisines, input_dishes):
    import string
    # check input types, input_cuisines should be an int, and input_dishes should be a list of positive ints
    if not isinstance(input_dishes, list):
        raise Exception('input_dishes should be a list')
    if not isinstance(input_cuisines, int):
        raise Exception('input_cuisines should be an int')
    if not all([isinstance(ii, int) for ii in input_dishes]):
        raise Exception('input_dishes should be a list of ints')
    if any([ii < 1 for ii in input_dishes]):
        raise Exception('input_dishes should be a list of positive ints')

    # check if all input_cuisines have number of dishes specified
    if input_cuisines != len(input_dishes):
        raise Exception('Each cuisine should have the number of dishes specified')
    if input_cuisines > len(string.ascii_letters):
        raise Exception('add more characters for more than 52 cuisines')

    cuisine_strings = string.ascii_letters[0:input_cuisines]  # set alphabets for cuisines

    global output_menu_list  # output list
    output_menu_list = []

    curr_menu = [1] * input_cuisines  # initialize curr_menu, [1,input_cuisines], to indicate current menu
    print_menu(cuisine_strings, curr_menu)
    if curr_menu == input_dishes:  # In case all cuisines only have one dish
        return ()

    dish_plus_one(curr_menu, cuisine_strings, input_dishes)
    # add one dish for the current menu each time, recursively

    #     print('output menu list', output_menu_list)
    return output_menu_list


def dish_plus_one(curr_menu, cuisine_strings, input_dishes):
    # add one dish for the current menu each time, recursively
    curr_cuisine_ind = find_min_non_identical_ind(curr_menu, input_dishes)
    # adding one dish from the first cuisine that not reach the input_dishes
    curr_menu[curr_cuisine_ind] += 1
    print_menu(cuisine_strings, curr_menu)
    if curr_menu == input_dishes:
        return ()
    if curr_menu[curr_cuisine_ind] == input_dishes[curr_cuisine_ind]:
        # when current cuisine reaches the input_dishes, add dish to the next available cuisine, and reset the menu for previuos cuisines
        curr_cuisine_ind = find_min_non_identical_ind(curr_menu, input_dishes)
        curr_menu[0:curr_cuisine_ind] = [1] * curr_cuisine_ind
        curr_menu[curr_cuisine_ind] = curr_menu[curr_cuisine_ind] + 1
        print_menu(cuisine_strings, curr_menu)
    dish_plus_one(curr_menu, cuisine_strings, input_dishes)


def print_menu(cuisine_strings, dish_ind_list):
    # print and append menu to output
    cuisine_ind = 0
    menu = cuisine_strings[cuisine_ind] + str(dish_ind_list[cuisine_ind])
    while cuisine_ind < len(cuisine_strings) - 1:  # enumerate cuisines
        cuisine_ind += 1
        menu = menu + ' ' + cuisine_strings[cuisine_ind] + str(dish_ind_list[cuisine_ind])
    #     print(menu)
    output_menu_list.append(menu)


def find_min_non_identical_ind(curr_menu, input_dishes):
    # find the minimum index in input_dishes, where curr_menu[min_non_identical_ind]!=curr_menu[min_non_identical_ind] 
    # return an int
    min_non_identical_ind = 0
    while curr_menu[min_non_identical_ind] == input_dishes[min_non_identical_ind]:
        min_non_identical_ind += 1
        if min_non_identical_ind >= len(input_dishes):
            break
    return min_non_identical_ind

	
input_cuisines = 4
input_dishes = [2, 5, 2, 9]
print('input', input_cuisines, input_dishes)
menu_list(input_cuisines, input_dishes)
