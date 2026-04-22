import random


def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(values):
    for j in range(len(values)):
        min_index = j
        min_values = values[min_index]
        for i in range(j + 1, len(values)):
            if values[i] < min_values:
                min_index = i
                min_values = values[i]

        values[j], values[min_index] = values[min_index], values[j]
        print(values)
    return  values


def bubble_sort(values):
    for j in range(len(values)):
        for val in range(len(values)-1):

            if values[val] > values[val+1]:
                values[val], values[val+1] = values[val+1], values[val]

    print (values)
    return values




if __name__ == "__main__":
    values = random_numbers(10)  # 10 čísel v rozsahu 0–100
    print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]

    small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20
    print(small)
    min_index = selection_sort(values)
    values_b = bubble_sort(values)
