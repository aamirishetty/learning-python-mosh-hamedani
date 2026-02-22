bag_of_fruits = ['apple', 'orange', 'banana', 'strawberry', 'apple', 'strawberry','banana']
print("-------- While loop Example 1 --------- ")
print("Output: ")
while len(bag_of_fruits) != 0:
    print(f"    Picked {bag_of_fruits[0]}...")
    bag_of_fruits.pop(0)
    if 'apple' not in bag_of_fruits:
        print(f"        No more apples")
    if 'orange' not in bag_of_fruits:
        print(f'        No more oranges')
    if 'banana' not in bag_of_fruits:
        print(f'        No more bananas')
    if 'strawberry' not in bag_of_fruits:
        print(f'        No more strawberries')
else:
    print('    No more fruits! Bag is empty!')
print("-------- While loop Example 1 --------- ")
