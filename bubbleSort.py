import time


def bubble_sort(data, draw_data):
    for _ in range(len(data) - 1):
        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                draw_data(data, ['black' if x == j or x == j + 1 else 'grey' for x in range(len(data))])
                time.sleep(0.2)
    draw_data(data, ["black" for i in range(len(data))])
