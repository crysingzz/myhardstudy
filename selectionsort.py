#__________selection_sort_________________
a = [321,123,534,1234,2,321,6,77,0,4324,76,56,54,23,32,-123]
#имеем рандомный массив
for i in range(len(a)-1):
    min_index = i
    for j in range(i+1, len(a)):
        if a[j]<a[min_index]:
            a[min_index],a[j] = a[j],a[min_index]
print(a)