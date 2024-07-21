# while loops
count = 0
while count < 10:
    print(count)
    count += 1
print("After the loop")

# for loops
items = [1, 2, 3, 4]
for item in items:
    print(item)

for index, item in enumerate(items):
    print(index, item)  # returns item and its index

word = "hello"
for letter in word:
    print(letter)

for item in range(15):
    print(item)

num = int(
    input("Enter your number: ")
)  # making sure this is a valid number for our loop
for i in range(num):
    print(i)

# break and continue
items = [1, 2, 3, 4]
for item in items:
    if item == 2:
        continue  # continue skips the iteration when the value is 2
    print(item)

for item in items:
    if item == 2:
        break  # break stops the loop when the value is 2
    print(item)
