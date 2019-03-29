def insertion_sort(v):
    i = 1
    while i < len(v):
        troca = False
        temp = v[i]
        j = i - 1

        while j >= 0 and v[j] > temp:
            v[j + 1] = v[j]
            troca = True
            j -= 1

        if troca:
            v[j + 1] = temp

        i += 1

