from numpy import *
import random


class Chromosome:

    def __init__(self, chromosome, f_x, fitness, fitnessRatio):
        self.chromosome = chromosome
        self.f_x = f_x
        self.fitness = fitness
        self.fitnessRatio = fitnessRatio

    def setChromosome(self, chromosome):
        self.chromosome = chromosome

    def setFx(self, f_x):
        self.f_x = f_x

    def setFitness(self, fitness):
        self.fitness = fitness

    def setFitnessRatio(self, fitnessRatio):
        self.fitnessRatio = fitnessRatio




        # _____________ CLASS ENDS


def rankBasedSorted(objectArray):
    largest = objectArray[0].fitnessRatio
    secondLargest = objectArray[1].fitnessRatio
    if objectArray[2].fitnessRatio > largest:
        secondLargest = largest
        largest = objectArray[2].fitnessRatio

        objectArray[0], objectArray[1] = objectArray[1], objectArray[0]

        objectArray[0], objectArray[2] = objectArray[2], objectArray[0]

    if objectArray[2].fitnessRatio > secondLargest:
        secondLargest = objectArray[2].fitnessRatio

        objectArray[1], objectArray[2] = objectArray[2], objectArray[1]

    if secondLargest > largest:
        a = largest
        largest = secondLargest
        secondLargest = a

        # temp = objectArray[0]
        # objectArray[0]=objectArray[1]
        # objectArray[1]=objectArray

        objectArray[0], objectArray[1] = objectArray[1], objectArray[0]  # SWAPPING

    return objectArray


def calculateFx(array, chromo):
    fx = 0
    for i in range(len(chromo) - 1):
        fx += array[chromo[i]][chromo[i + 1]]

    return fx


def calculateFitness(fx, highestFitness):
    fitness = highestFitness - fx

    return fitness


def calculateFitnessRatio(fitness, highestFitness):
    fitnessRatio = (fitness / highestFitness) * 100
    return fitnessRatio



def crossOver(chromoo1, chromoo2, cutOffIndex):
    offspring = []
    for i in range(cutOffIndex):
        x = chromoo1[i]
        offspring.append(x)

    for i in chromoo2:
        if i not in offspring:
            offspring.append(i)

    return offspring


def Mutation(offspring, index):
    #swap(offspring[index], offspring[index + 1])
    offspring[index],offspring[index+1]=offspring[index+1],offspring[index]
    return offspring


row = 20
col = 20

arr = zeros((row, col), dtype=int)

for i in range(row):
    for j in range(col):
        if i == j:
            arr[i][j] = 0
            continue
        x = random.randint(1, 5)
        arr[i][j] = x

print(arr)

# ------ CREATING CHROMOSOMES

chromo1 = [0, 1, 2, 3, 4,5,6,7,8,9,10,11,12,15]
chromo2 = [0, 1, 4, 3, 2,10,11,13,15,17,18,19,16,12]
chromo3 = [1, 4, 0, 2, 3,11,10,13,15,18,17,16,19,12]

# ------ CREATING CHROMOSOME OBJECTS

c1 = Chromosome(chromo1, 0, 0, 0)
c2 = Chromosome(chromo2, 0, 0, 0)
c3 = Chromosome(chromo3, 0, 0, 0)

# -------- CALCULATING FX

c1.f_x = calculateFx(arr, c1.chromosome)
c2.f_x = calculateFx(arr, c2.chromosome)
c3.f_x = calculateFx(arr, c3.chromosome)



# ------ CALCULTING FITNESS

highestFitness = 100

c1.fitness = calculateFitness(c1.f_x, highestFitness)
c2.fitness = calculateFitness(c2.f_x, highestFitness)
c3.fitness = calculateFitness(c3.f_x, highestFitness)



# ------- CALCULATING FITNESS RATIOS

c1.fitnessRatio = calculateFitnessRatio(c1.fitness, highestFitness)
c2.fitnessRatio = calculateFitnessRatio(c2.fitness, highestFitness)
c3.fitnessRatio = calculateFitnessRatio(c3.fitness, highestFitness)


objectArray = [c1, c2, c3]

c4 = Chromosome([0, 0, 0, 0], 0, 0, 0)
flag=False
k=0
while k<100:
    k+=1


    objectArray = rankBasedSorted(objectArray)

    print("SELECTED CHROMOSOMES")

    for i in range(len(objectArray)-1):
        print("Chromosome : ",objectArray[i].chromosome)
        print("Fitness Ratio : " ,objectArray[i].fitnessRatio)

    cutOffIndex = random.randint(1,2)

    os = crossOver(objectArray[0].chromosome, objectArray[1].chromosome, cutOffIndex)

    print("After Crossover ",os)

    index = 2
    offspring = Mutation(os, index)

    print("After Mutation ",offspring)


    offspringFx = calculateFx(arr, offspring)
    offSpringFitness = calculateFitness(offspringFx, highestFitness)
    offSpringFitnessRatio = calculateFitnessRatio(offSpringFitness, highestFitness)

    c4.setChromosome(offspring)
    c4.setFx(offspringFx)
    c4.setFitness(offSpringFitness)
    c4.setFitnessRatio(offSpringFitnessRatio)

    if c4.fitnessRatio > 70:
            print("Highest fitness of chromosome ",c4.chromosome)
            print("Fitness Ratio is ",c4.fitnessRatio)
            flag=True
            break;

    objectArray[2] = c4
    print("Offspring Fitness Ration : ",c4.fitnessRatio)

if flag==False:
    print("No chromosome and offpring found whose fitness ratio is greator 70%")
