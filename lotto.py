import random
import sys

sys.setrecursionlimit(1500) #python is ein spaßverderber

#aufgabe 1:
numbers = []
def getNr(allowDuplicates = False):
    if len(numbers) >= 45 and not allowDuplicates:
        raise Exception
    nr = int(random.random()*45)
    return nr if not nr in numbers or allowDuplicates else getNr()

for i in range(0,6):
    numbers.append(getNr())

print(numbers)

#aufgabe 2 in langweilig:
numbers = {}
for i in range(45):
    numbers[i] = 0

for i in range(1000):
    numbers[getNr(True)] += 1

#aufgabe 2 in anders (was ist diese ominöse "Statistikmethode"?)

def statfun(mini, maxi, dict): #mini und maxi haben fun, benedict schaut zu :^)
    dict[getNr(True)] += 1
    if mini >= maxi:
        return dict #sind mini und maxi gleichauf ist der höhepunkt erreicht, dict geht heim
    else:
        return statfun(mini+1, maxi, dict) #sonst haben mini und maxi mehr fun

for i in range(45):
    numbers[i] = 0

print(statfun(0, 999, numbers))
#in der angabe steht "alle 45 zahlen", aus faulheitsgründen gehen meine 45 zahlen von 0-44
