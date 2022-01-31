from part1 import crossover
from part1 import mutation
from part1 import rouletteWheelSelection
from part1 import Population

import linecache
import part1
import random
import time
def rouletteWheelSelection(self):
        n = self.populationSizeMethod()
        summedPopulationFitness = self.summedPopulationFitness()
        i = 0
        while(i < n) :
            i+=1
            pointerPosition = random.random()*summedPopulationFitness
            ind=self.spinWheel(self.popu, n, pointerPosition)
            self.popu.chromosome[i] = self.spinWheel(self.popu, n, pointerPosition)
        return self   
adj=[]
#if 1==1:
if __name__ == '__main__':
    outputFile = open('output.txt', 'w')
    with open('D:\\artificial inteligence(ungrad)\\AIFirstProject\\input.txt', 'r') as inputFile:
        listm=inputFile.readlines()
        chromosomeLe=int(listm[0])
        iteration=int(listm[1])
        Pm=float(listm[2])
        Pc=float(listm[3])
        populationSize=int(listm[4])
        i=0
        
        for words in inputFile.read().split():
            j=0
            for word in words:
                adj[i][j]=int(word)
                j+=1
            i+=1

    p=Population(chromosomeLe)
    #print(type(p))
    max=0
    index=0
    for j in p.popu:
        if max<j.fiteval(adj):
            max=j.fiteval(adj)
            index=1
    outputFile.write(str(1))
    outputFile.write(' ')
    outputFile.write(str(p.bestEval))
    outputFile.write(' ')
    outputFile.write(str(index))
    outputFile.write(' ')
    outputFile.write(str(max))
    outputFile.write('\n')

    for i in range(2,iteration+1):
        maxgeneration=0.0
        p=crossover(p,Pc)
        p=mutation(p,Pm)
        #print(type(p))
        p=rouletteWheelSelection(p)
        thisgenerationeval=p.bestEval
        #print(type(p))
        for j in p.popu:
            if max<j.fiteval(adj):
                max=j.fiteval(adj)
                index=i
        outputFile.write(str(i))
        outputFile.write(' ')
        outputFile.write(str(thisgenerationeval))
        outputFile.write(' ')
        outputFile.write(str(index))
        outputFile.write(' ')
        outputFile.write(str(max))
        outputFile.write('\n')

