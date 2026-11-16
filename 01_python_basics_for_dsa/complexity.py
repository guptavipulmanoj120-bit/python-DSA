numbers = [12, 45, 7, 89, 23]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
             
print(largest)

# find largest and smallest number in the list in one loop 

numbers = [45, 12, 89, 3, 67, 21]

largest = numbers[0]
smallest = float('inf')

for num in numbers:
  if num > largest:
    largest = num
    
  if num < smallest:
    smallest = num

print(largest)
print(smallest)

# find largest and second largest number in the list 

numbers = [12, 45, 7, 89, 23]

largest = float('-inf')
second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num

    elif num > second_largest and num != largest:
        second_largest = num

print(second_largest)

# find smallest and second smallest number in the lsit 

numbers = [34, 12, 56, 7, 89, 3, 21]

smallest = float('inf')
second_smallest = float('inf')

for num in numbers:

    if num < smallest:
        second_smallest = smallest
        smallest = num

    elif num < second_smallest and num != smallest:
        # Update second_smallest here
        pass

print("Smallest:", smallest)
print("Second smallest:", second_smallest)




