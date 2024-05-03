def binary_search():
    def find_integer():
        seq = []
        n = int(input("Enter the amount of integers you want in your list: "))
        for i in range(1, n + 1):
            while True:
                try:
                    input_element = int(input(f"Enter the integer at position {i}: "))
                    seq.append(input_element)
                    print(seq)
                    break
                except ValueError:
                    print("Enter an integer!")

        search_index = int(input("Enter the number to be searched: "))
        list_begin_index = 0
        list_end_index = len(seq) - 1

        while list_begin_index <= list_end_index:
            mid = (list_begin_index + list_end_index) // 2
            mid_value = seq[mid]
            if search_index == mid_value:
                position = mid + 1
                print("\nThe index of the searched number is:", mid)
                print("\nThe position of the searched number is:", position)
                break
            elif search_index < mid_value:
                list_end_index = mid - 1
            else:
                list_begin_index = mid + 1
        else:
            print('The number was not found!!!')

    def find_string():
        seq = []
        n = int(input("Enter the amount of strings you want in your list: "))
        for i in range(1, n + 1):
            while True:
                try:
                    input_element = input(f"Enter the string at position {i}: ")
                    seq.append(input_element)
                    print(seq)
                    break
                except ValueError:
                    print("Enter a valid string!")

        search_index = input("Enter the string to be searched: ")
        list_begin_index = 0
        list_end_index = len(seq) - 1

        while list_begin_index <= list_end_index:
            mid = (list_begin_index + list_end_index) // 2
            mid_value = seq[mid]
            if search_index == mid_value:
                position = mid + 1
                print("\nThe index of the searched string is:", mid)
                print("\nThe position of the searched string is:", position)
                break
            elif search_index < mid_value:
                list_end_index = mid - 1
            else:
                list_begin_index = mid + 1
        else:
            print('The string was not found!!!')

    input_user = input("Enter which elements you want in your list: Integer or String: ")
    if input_user.lower() == 'integer':
        find_integer()
    elif input_user.lower() == 'string':
        find_string()
    else:
        print("Invalid choice!")

binary_search()
