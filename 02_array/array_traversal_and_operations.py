#print all the numbers in the list

numbers = [5, 10, 15, 20, 25]

for num in numbers:
  print(num)
  
#print the sum of all the numbers in the list without uaing the sum()

numbers = [10,20,30,40,50]

total = 0 

for num in numbers:
    total = total + num
    
print(total)

#find the index of a target number in the lsit

numbers = [12, 45, 23, 67, 89, 34]
target = 67

for i in range(len(numbers)):
  if numbers[i] == target:
    print("found at index:",i)
    break

#find the lergest number in the list

numbers = [23, 56, 12, 89, 34, 78]

largest = numbers[0]

for num in numbers:
  if num > largest:
    largest = num 

print(largest)
