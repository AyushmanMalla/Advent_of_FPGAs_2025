#this is a sample implementation of a sorting algo implemented in Python for my own clarity of thought before porting it over to verilog code

#bubble sort - inefficient but simple to understand :)

def bubble_sort(arr):
    n = len(arr)

    i_limit = n-1
    iter_count = 1
    while (iter_count <= n-1):
        swapped = False
        for i in range(i_limit):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
            i += 1
        if not swapped:
            break
        iter_count += 1
        i_limit -= 1
    return arr

