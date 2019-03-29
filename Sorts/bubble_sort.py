#Bubble_Sort

def bubble_sort(v):
    fim = len(v) - 1

    while fim > 0:
        i = 0
        while i < fim:
            if v[i] > v[i + 1]:
                temp = v[i + 1]
                v[i + 1] = v[i]
                v[i] = temp
            i += 1
        fim -= 1
 

