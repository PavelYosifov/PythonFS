import module_dog  # importing module "module_dog"
from module_dog import bark  # importing only the function bark from the module

module_dog.bark()  # using the function from "module_dog"
bark()  # after uploading only the function bark from the module, we only type bark()

# using other libraries
import math

print(math.sqrt(4))

from math import sqrt  # importing only sqrt function

print(sqrt(4))
