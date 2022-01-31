import random
import time
def current_milli_time():
    return round(time.time() * 1000)
random.seed(current_milli_time())
class indiv:
    chromosome=[]
    chromosomeLength=0
    fitness=0.0
    def __init__(self,chromosomeLe):
        self.chromosomeLength=chromosomeLe
        self.chromosome=range(chromosomeLe)
        return self
    def fiteval(adj,self): 
        sum=0
        for i in range(self.chromosomeLength):  #
            if(i+1<=self.chromosomeLength):
                sum+=adj[self.chromosome[i]][self.chromosome[i+1]]
            else:
                sum+=adj[self.chromosome[i]][self.chromosome[0]]
        self.fitness=1/sum
        return 1/sum;        
    def chromosomeappend(j,self):
        if(self.chromosomeLength>len(self.chromosome)):
            self.chromosome.append(j)
    def print(self):
        for i in range(self.chromosomeLength):
            print(" ",self.chromosome[i])
            print("\n")
    
class Population:
    populationSize=0
    popu=[]
    bestch=0
    def __init__(self,chromosomeLe):
        #print(type(self.popu.chromosomeLength[0]))
        random.seed(time.time())
        for i in range(self.populationSize):
            self.popu[i]=indiv(chromosomeLe)
            s=range(self.popu.chromosomeLength)
            self.popu[i].chromosome=random.shuflle(s)

    def populationSizeMethod(self):
        return self.populationSize  
    def print(self):
        for i in self.popu:
            i.print()
            print("\n")
    def getChild( self,parent1, parent2, CX1, CX2 ):
        m = parent1.chromosomeLength
        child=indiv()
        for i in range (m):
            child.chromosome[i]=-1

        j = CX1 + 1
        i = CX1 + 1
        while(i <= CX2 and j <= CX2):
            child.chromosome[j+1] = parent1.chromosome[i+1]
        j = 0
        i = CX2 + 1
        while(j <= CX1) :
            if(parent2[i] not in child  ) :
                child[j+1] = parent2.chromosome[i]
            i = (i + 1)%m
		
        j = CX2 + 1
        while(j < m) :
            if(parent2[i] not in child ) :
                child[j+1] = parent2.chromosome[i]
			
            i = (i + 1)%m
		
        return child
    def swapMutation(self,Pm) :
        random.seed(current_milli_time())
        m = self.popu.chromosomeLength
        mutatedChromosome =indiv()
        for i in range(m):
            mutatedChromosome.chromosome[i] = self.popu.chromosome[i]
            r=random.random()
            r1=int( round(random.random())*(m-1))
            r2=int( round(random.random())*(m-1))            
            if( r< Pm) :
                temp = mutatedChromosome.chromosome[r1]            
                mutatedChromosome[r1] = mutatedChromosome[r2]
                mutatedChromosome[r2] = temp
			
        return mutatedChromosome

    def insertMutation(self,Pm):
        random.seed(current_milli_time())
        m = self.popu.chromosomeLength
        mutatedChromosome =indiv(m)
        for i in range(m):
            mutatedChromosome.chromosome[i] = self.popu.chromosome[i]
            r=random.random()
            r1=int( round(random.random())*(m-1))
            r2=int( round(random.random())*(m-1))
            s= mutatedChromosome.chromosome[r1+1:r2-1]           
            if( r< Pm) :
                mutatedChromosome[r1+1] = mutatedChromosome[r2]	
                mutatedChromosome.chromosome[r1+2:r2]=s		
        return mutatedChromosome
        
    def scrambleMutation(self,Pm):
        random.seed(current_milli_time())
        m = self.popu.chromosomeLength
        mutatedChromosome =indiv(m)
        for i in range(m):
            mutatedChromosome.chromosome[i] = self.popu.chromosome[i]
            r=random.random()
            r1=int( round(random.random())*(m-1))
            r2=int( round(random.random())*(m-1))
            if( r< Pm) :
                s=mutatedChromosome.chromosome[r1:r2]
                mutatedChromosome.chromosome[r1:r2]=random.shuffle(s)           
        return mutatedChromosome

    def inversionMutation(self,Pm):
        random.seed(time.time())
        m = self.popu.chromosomeLength
        mutatedChromosome =indiv(m)
        for i in range(m):
            mutatedChromosome.chromosome[i] = self.popu.chromosome[i]
            r=random.random()
            r1=int( round(random.random())*(m-1))
            r2=int( round(random.random())*(m-1))         
            if( r< Pm) :
                s=mutatedChromosome.chromosome[r1:r2]
                mutatedChromosome.chromosome[r1:r2]=s.inverse()           
        return mutatedChromosome
 	
    def  orderedCrossover(self,parents) :
        m = parents[0].chromosomeLength
        children = indiv(parents.chromosomeLength)
        r=random.random()
        CX1 = int (round(r*(m-3)))
        CX2 = CX1 + int( round(r*(m-2-CX1)))
        child1 = self.getChild(parents[0], parents[1], CX1, CX2)
        child2 = self.getChild(parents[1], parents[0], CX1, CX2)
        children[0] = child1 
        children[1] = child2
        return children
    
    def circledCrossover():
        pass
    def summedPopulationFitness(self):
        fitness = 0.0
        for i in range(self.populationSize):
            fitness += self.population[i].fitness
        return fitness

    def spinWheel(population1,n,pointer)->indiv :
        rouletteWheel = 0.0
        for i in population1:
            rouletteWheel += i.fitness
            if rouletteWheel >= pointer :
                return i
        return population1[n-1]
    def rouletteWheelSelection(self):
        n = self.populationSize
        summedPopulationFitness = self.summedPopulationFitness()
        i = 0
        while(i < n) :
            i+=1
            pointerPosition = random.random()*summedPopulationFitness
            ind=self.spinWheel(self.popu, n, pointerPosition)
            self.popu.chromosome[i] = self.spinWheel(self.popu, n, pointerPosition)
        return self

    def bestEval(self):
        
        for i in self.popu:
            if i.fitness>self.bestch:
               self.bestch=i.fitness
        return self.bestch
            


def crossover(population,Pc) :
    cp=population
    n = population.populationSizeMethod()
    tempInput =[]
    tempOutput = []
    for i in range(0,n-1,2):
        if random.random() < Pc:
            tempInput[0] = population.popu[i]
            tempInput[1] = population.popu[i+1]
            tempOutput = Population.orderedCrossover(tempInput)
            cp.append( tempOutput[0])
            cp.append( tempOutput[1])
    return cp

	
def mutation( population, Pm) :
    mp=population
    n = population.populationSizeMethod()
    for i in range(n):
        mp.append (population.popu[i].swapMutation(Pm))    #instead of swapMutation method, any other mutation method can be implemented
    return mp

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
   
	

   
	
