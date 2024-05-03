def binary_search():
    def find_integer():
        seq = []
        n = int(input("Enter the amount of Integers you want in your list: "))
        for i in range(1, n + 1):
                while True:
                    try:
                        input_numbers = int(input(f"Enter the integer at position {i}: "))
                        seq.append(input_numbers)
                        print(seq)
                        break
                    except ValueError:
                        print("Enter the integer!!!!")

    def find_string():
        seq = []
        n = int(input("Enter the amount of Strings you want in your list: "))
        for i in range(1, n + 1):
            while True:
                    try:
                        input_numbers = input(f"Enter the string at position {i}: ")
                        seq.append(input_numbers)
                        print(seq)
                        break
                    except ValueError:
                        print("Enter the integer!!!!")

        if isinstance(input_numbers, int):
            search_index = int(input("Enter the Number to be searched: "))
        elif isinstance(input_numbers, str):
            search_index = input("Enter the string to be searched: ")

        list_begin_index = 0
        list_end_index = len(seq) - 1

        while list_begin_index <= list_end_index:
            mid = list_end_index + (list_begin_index - list_end_index) // 2
            mid_value = seq[mid]
            if search_index == mid_value:
                position = mid + 1
                print("\nThe index of the searched number is: ", mid)
                print("\nThe position of the searched number is: ", position)
                break
            elif search_index < mid_value:
                list_end_index = mid - 1
            else:
                list_begin_index = mid + 1
        else:
            print('The number was not found!!!')

    input_user = input("Enter Which elements you want in your list: Integer or String = ")
    if input_user.lower() == 'integer':
        find_integer()
    elif input_user.lower() == 'string':
        find_string()

binary_search()


