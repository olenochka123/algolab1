import datetime
import csv

comparison_count = 0
swap_count = 0


class Hotel:
    def __init__(self, number_of_visitors_per_year: float, name: str, number_of_rooms: float):
        self.number_of_visitors_per_year = number_of_visitors_per_year
        self.name = name
        self.number_of_rooms = number_of_rooms

    def __str__(self):
        return 'Number of visitors per year: {}, Name: {}, Number of rooms: {}'.format(
            self.number_of_visitors_per_year, self.name, self.number_of_rooms)


def get_csv(file_name: str):
    hotels = []

    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            hotels.append(Hotel(int(line[0]), str(line[1]), int(line[2])))
    return hotels


def selection_sort(list_to_sort: list, key):
    comparison_count = 0
    swap_count = 0
    start_time = datetime.datetime.now()
    for num in range(len(list_to_sort) -1,0,-1):
        min_value = num
        for item in range(0,num):
            comparison_count += 1
            if key(list_to_sort[item]) < key(list_to_sort[item+1]):
                min_value = item
        temp = list_to_sort[item]
        list_to_sort[item] = list_to_sort[item + 1]
        list_to_sort[item + 1] = temp
        swap_count += 1
    print(f"[Selection Sort] Comparisons: {comparison_count}, swaps: {swap_count}, "
          f"execution time: {datetime.datetime.now() - start_time} sec")
    return list_to_sort


def heapify(list_to_sort, length, item, key):
    global comparison_count
    global swap_count
    least = item
    left = 2 * item + 1
    right = 2 * item + 2
    comparison_count += 3

    if left < length and key(list_to_sort[item]) < key(list_to_sort[left]):
        least = left

    if right < length and key(list_to_sort[least]) < key(list_to_sort[right]):
        least = right

    if least != item:
        swap_count += 1
        list_to_sort[item], list_to_sort[least] = list_to_sort[least], list_to_sort[item]
        heapify(list_to_sort, length, least, key)


def min_heap(list_to_sort: list, key):
    start_time = datetime.datetime.now()
    global swap_count

    length = len(list_to_sort)
    for i in range(length, -1, -1):
        heapify(list_to_sort, length, i, key)

    for i in range(length - 1, 0, -1):
        swap_count += 1
        list_to_sort[0], list_to_sort[i] = list_to_sort[i], list_to_sort[0]
        heapify(list_to_sort, i, 0, key)
    print(f"[Min-Heap Sort] Comparisons: {comparison_count}, swaps: {swap_count}, "
          f"execution time: {datetime.datetime.now() - start_time} sec")
    return list_to_sort


if __name__ == '__main__':
    input_data = get_csv('hotels.csv')
    selection_sort(input_data, key=lambda x: x.number_of_visitors_per_year)
    for i in input_data:
        print(i)
    min_heap(input_data, key=lambda x: x.number_of_rooms)
    for i in input_data:
        print(i)


