name = str(input())  # name of the architect
num = int(input())  # number of projects
time = num * 3  # total time need for the projects, every project needs 3 hours to be created
#print(f"The architect {name} will need {time} hours to complete {num} project/s.")
print("The architect " + name + " will need {}".format(time)+ " hours to complete {}".format(num) +" project/s.")