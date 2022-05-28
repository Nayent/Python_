import numpy
vet = []

for i in numpy.arange(0.01,0.31,0.01):
    vet.append(1/i**2)
    print(i)


print(vet)