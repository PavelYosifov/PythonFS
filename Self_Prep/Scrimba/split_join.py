csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = ['Exercise: fill me with names']
print(friends_list)
csv = csv.replace(";", ",")
csv = csv.replace(":", ",")
friends_list = csv.split(",")
print(friends_list)
"""
Second way:
friends_list = csv.replace(";", ",").replace(":", ",").split(",")
print(friends_list)
"""
