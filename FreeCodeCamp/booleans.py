done = True
print(type(done) == bool) #check the type of done
if done:
    print("Task completed successfully.")
else:
    print("Task failed")
read_book1 = True
read_book2 = False
ready_any_book = any([read_book1, read_book2]) #check with any, its True
read_all_books = all([read_book1, read_book2]) #check with all, its False
