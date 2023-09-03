def binary_search(list_num , to_search):
    first_index = 0
    size = len(list_num)
    last_index = size - 1
    mid_index = (first_index + last_index) // 2
    mid_element = list_num[mid_index]
    is_found = True
    while is_found:
        if first_index == last_index:
            if mid_element != to_search:
                is_found = False
                return "Элемент не найден"
        elif mid_element == to_search:
            return f"{mid_element} находится под индексом {mid_index}"
        elif mid_element > to_search:
            new_position = mid_index - 1
            last_index = new_position
            mid_index = (first_index + last_index) // 2
            mid_element = list_num[mid_index]
            if mid_element == to_search:
                return f"{mid_element} находится под индексом {mid_index}"
        elif mid_element < to_search:
            new_position = mid_index + 1
            first_index = new_position
            last_index = size - 1
            mid_index = (first_index + last_index) // 2
            mid_element = list_num[mid_index]
            if mid_element == to_search:
                return f"{mid_element} находится под индексом {mid_index}"

list = [1 , 2 , 3 , 14 , 28 , 29 , 31 , 37]
print(binary_search(list , 14))
print(binary_search(list , 32))