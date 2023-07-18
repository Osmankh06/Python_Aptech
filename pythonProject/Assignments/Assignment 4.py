
list1 = ["mango", "orange", "banana"]
print(list1)
print("Enter the Index of items you want to change:")
item_no_start = int(input("Start:"))
item_no_end = int(input("End:"))
for i in range(item_no_start,item_no_end):
    new_item = input("Enter new item:")
    list1[i] = new_item
print(list1)
