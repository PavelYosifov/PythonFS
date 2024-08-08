# Sets - Exercise

# 1. Check if ‘Eric’ and ‘John’ exist in friends
# 2. combine or add the two sets
# 3. Find names that are in both sets
# 4. find names that are only in friends
# 5. Show only the names who only appear in one of the lists
# 6. Create a new cars-list without duplicates

friends = {'John', 'Michael', 'Terry', 'Eric', 'Graham'}
my_friends = {'Reg', 'Loretta', 'Colin', 'John', 'Graham'}
cars = ['900', '420', 'V70', '911', '996',
        'V90', '911', '911', 'S', '328', '900']
# Answer to question 1
print("Eric" and "John" in friends)
# Answer to question 2
combined_set = my_friends.union(friends)
print(combined_set)
# Answer to question 3
print(my_friends.intersection(friends))
# Answer to question 4
print(friends.difference(my_friends))
# Answer to question 5
print(my_friends.symmetric_difference(friends))
# Answer to question 6
cars = set(cars)
print(cars)
