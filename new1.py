numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
sum = 0
for val in numbers:
   sum = sum+val
   print("The sum is", sum)


""


print(range(10))

print(list(range(10)))

print(list(range(2, 8)))

print(list(range(2, 20, 3)))


""


fruits = ['mango', 'banana', 'grapes']
for i in range(len(fruits)):
   print("I like", fruits[i])


""


digits = [0, 1, 5]

for i in digits:
   print(i)
else:
   print("No items left.")


""


student_name = 'Aman'

marks = {'Aman': 90, 'Sanjima': 55, 'Akash': 77}
for student in marks:
  if student == student_name:
   print(marks[student])
break

else: 
   print('No entry with that name found.')
