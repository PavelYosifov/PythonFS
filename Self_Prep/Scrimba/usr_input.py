name = str(input("Enter your name: "))
name = name.capitalize()
km = float(input("Enter the distance in km: "))
miles = km/1.609
miles = round(miles, 2)
print("Hello, " + name + ". You entered "+str(km) +
      " km, which are "+str(miles)+" miles.")
