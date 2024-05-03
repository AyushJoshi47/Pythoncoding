def search(input):
    if isinstance(input, int):
        integer_search(input)
    elif isinstance(input, str):
        string_search(input)

def integer_search(search_index):
    def binary_search(seq, search_index):
        list_begin_index = 0
        list_end_index = len(seq) - 1

        while list_begin_index <= list_end_index:
            mid = list_end_index + (list_begin_index - list_end_index) // 2
            mid_value = seq[mid]
            if search_index == mid_value:
                position = mid + 1
                print("\nThe index of the searched number is:", mid)
                print("\nThe position of the searched number is:", position)
                return
            elif search_index < mid_value:
                list_end_index = mid - 1
            else:
                list_begin_index = mid + 1
        else:
            print('The number was not found!!!')

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
                print("Enter an integer!")

    search_index = int(input("Enter the number to be searched: "))
    binary_search(seq, search_index)
def string_search(search_index):
    def binary_search(seq, search_index):
        list_begin_index = 0
        list_end_index = len(seq) - 1

        while list_begin_index <= list_end_index:
            mid = list_end_index + (list_begin_index - list_end_index) // 2
            mid_value = seq[mid]
            if search_index == mid_value:
                position = mid + 1
                print("\nThe index of the searched string is:", mid)
                print("\nThe position of the searched string is:", position)
                return
            elif search_index < mid_value:
                list_end_index = mid - 1
            else:
                list_begin_index = mid + 1
        else:
            print('The string was not found!!!')

    seq = []
    n = int(input("Enter the amount of Strings you want in your list: "))
    for i in range(1, n + 1):
        while True:
            try:
                input_string = input(f"Enter the string at position {i}: ")
                seq.append(input_string)
                print(seq)
                break
            except ValueError:
                print("Enter a valid string!")

    search_index = input("Enter the string to be searched: ")
    binary_search(seq, search_index)

input_user = input("Enter which elements you want in your list: Integer or String = ")
search(input_user)

