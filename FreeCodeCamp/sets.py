set1 = {"Roger", "Syd"}
set2 = {"Roger"}
set3 = {"Nikolas"}
intersect = set1 & set2  # intersection
print(intersect)
mod = set1 | set3  # union
print(mod)
mod2 = set1 - set2  # difference
print(mod2)
mod3 = set1 > set2  # superset check
print(mod3)
mod4 = set1 < set2  # subset check
print(mod4)
