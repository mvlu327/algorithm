print("AMAN")
def bubble_sort(sort_list):
    for j in range(len(sort_list)):
        for k in range(len(sort_list) - 1):
            if sort_list[k] > sort_list[k + 1]:
                sort_list[k], sort_list[k + 1] = sort_list[k + 1], sort_list[k]
    print(sort_list)
 
 
lst = []
size = int(input("Enter size of the list: \t"))
 
for i in range(size):
    elements = int(input("Enter the element: \t"))
    lst.append(elements)
 
bubble_sort(lst)


Output:-
AMAN
Enter size of the list: 	5
Enter the element: 	1
Enter the element: 	2
Enter the element: 	3
Enter the element: 	4
Enter the element: 	5
[1, 2, 3, 4, 5]
