from enum import Enum
num1 = 2+3j
num2 = complex(2,3)
print(num2.real, num2.imag)#real - 2.0, imag -3.0
print(abs(-5.5)) #5.5
print(round(5.5)) #6
class State(Enum):
    INACTIVE = 0
    ACTIVE = 1
print(State.ACTIVE.value) #1
print(State.ACTIVE) #State.ACTIVE
print(State['ACTIVE']) #State.ACTIVE
print(list(State))#all possible states
print(len(State))