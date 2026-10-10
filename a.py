number = [10, 23, 45, 67, 89]

smallest = number[0]
for num in number:
    if num < smallest:
        smallest = num
        
print("smallest number:",smallest)