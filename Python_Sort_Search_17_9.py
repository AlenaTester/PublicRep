ar = list(map(int, input("Введите последовательность чисел через пробел: \n").split()))
figure = int(input("Введите любое число: \n"))

left = 0
right = len(ar)


def sort(ar):
    for i in range(len(ar)):
        min_index = i
        for j in range(i, len(ar)):
            if ar[j] < ar[min_index]:
                min_index = j
            if i != min_index:
                ar[i], ar[min_index] = ar[min_index], ar[i]
    return ar


def binary_search(ar, figure, left, right):
    middle = (right + left) // 2
    if ar[middle] == figure:
        x = ar[: middle]
        for i in x:
            if i == figure:
                x.remove(figure)
        index_1 = (len(x) - 1)
        y = ar[middle:]
        for n in y:
            if n <= figure and len(y) > 1:
                y.remove(n)
        f = y[0]
        index_2 = ar.index(f)
        if index_1 < 0:
            print(index_2)
        elif index_2 == len(ar) - 1:
            print(index_1)
        else:
            print(index_1, index_2)
        return index_1, index_2
    elif figure < ar[middle]:
        return binary_search(ar, figure, left, middle - 1)
    else:
        return binary_search(ar, figure, middle + 1, right)


print(sort(ar))
print((ar, figure, left, right))
