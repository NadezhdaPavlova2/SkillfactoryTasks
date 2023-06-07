while True:
    many_nums = input("Введите последовательность чисел через пробел: ")
    try:
        list_of_num = list(map(int, many_nums.split()))
    except ValueError:
        print("Неверный формат данных. Попробуйте еще раз.")
        continue
    else:
        break

while True:
    one_num = input("Введите число: ")
    try:
        one_num = int(one_num)
    except ValueError:
        print("Неверный формат данных. Попробуйте еще раз.")
        continue
    else:
        break


def sort_num(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


list_of_num = sort_num(list_of_num)

#print(list_of_num)

if one_num > list_of_num[len(list_of_num) - 1] or one_num < list_of_num[0]:
    print("Нет чисел удовлетворяющих условию")


def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] >= element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


mid = binary_search(list_of_num, one_num, 0, len(list_of_num) - 1)

for i in range(1, mid):
    if list_of_num[mid - i] < one_num:
        print(mid - i)
        break







