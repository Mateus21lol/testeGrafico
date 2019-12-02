import random
import matplotlib.pyplot

Generation = []
meses = ["Pior 4","medio 17","medio 18","medio 19","medio 20", "Otimo 27"]

# print("Vez numero", cont)
Generation = [5,3,2,5,8,1]


#matplotlib.pyplot.plot(Generation, meses)
matplotlib.pyplot.bar(meses, Generation)
matplotlib.pyplot.show()

