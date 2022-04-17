import copy
import pyPDF2

## This class is made to store all the information related to each time the perception recieves an example to learn from
## 'inputs' is the array of 1's and 0's that tell us information about what the current object we are trying to classify
## 'prediction' is the prediction that the perceptron makes about the classification about the object based on the current weights set
## 'answer' is the actual answer that the perceptron should have predicted
## 'adjWeights' is the array of the newly adjusted weights after making changes based on what the prediction was, what the answer is, and what the inputs are
class lesson:
    def __init__(self,inputs,prediction,answer,adjWeights):
        self.inputs = inputs
        self.prediction = prediction
        self.answer = answer
        self.adjWeights = adjWeights

## This function takes an array of lessons, and prints them in the format specified by the ECS 170 SUM II assignment 4 directions
def printPasses(arrayOfPasses):
    for x in range(len(arrayOfPasses)):
        print("")
        print("Pass ", (x+1))
        print("")
        for y in range(len(arrayOfPasses[x])):
            print("inputs: ", arrayOfPasses[x][y].inputs)
            print("prediction: ", arrayOfPasses[x][y].prediction, "   answer: ", arrayOfPasses[x][y].answer)
            print("adjusted weights: ", arrayOfPasses[x][y].adjWeights)

## This function adds an element to an array
def cons(lst, item):
    return lst + [item]

## This function is the perceptron
## 'Threshold' is the maximum amount of weight after passing inputs through the perceptron that will keep it from passing the inputs as part of whatever classification is being taught
## 'adjFactor' is the amount that each weight that corresponds with a '1' input is subtracted by when there is a false positive, or added by when their is a false negative
## 'weights' is the array of weights in which each weight that corresponds with one input in array of inputs in the examples
## 'examples' is the array of objects that each hold an array of inputs and whether or not those inputs are supposed to output true or false
## 'numPasses' is the number of times in which the function will pass the list of examples through the perceptron in order to try and get it to learn more.
allReturns = []
varAvgArr = []
varAdjArr = []
currentWeights = []
def getAvgInArraySpot(arrSpot):
    for a in range(len(allReturns)):
        totalNum = allReturns[a][1][arrSpot]
    avg = totalNum/(len(allReturns))
    return avg
def perceptron(weights,examples):
    startingWeights = copy.deepcopy(weights)
    recordOfPasses = []
    ifDoneOverall = False
    ifDone = []
    recordOfLessonsInOnePass = []
    leewayAdj = 0.0001*len(examples)
    leeway = 0.0001*len(examples)
    while(ifDoneOverall == False):
        for y in range(len(examples)):
            threshold = examples[y][0]
            total = 0
            for z in range(len(weights)):
                total = total + weights[z]*examples[y][1][z]
            if (total < threshold):
                for a in range(len(weights)):
                    if(examples[y][1][a] < varAvgArr[a]):
                        varAdjFact = (varAvgArr[a] - examples[y][1][a])/varAvgArr[a]
                        weights[a] = weights[a]*(1+varAdjFact*0.1)
            if (total > threshold):
                for a in range(len(weights)):
                    if(examples[y][1][a] > varAvgArr[a]):
                        varAdjFact = (examples[y][1][a] - varAvgArr[a])/varAvgArr[a]
                        weights[a] = weights[a]/(1+varAdjFact*0.1)
            if(total >= (threshold - leeway) and total <= (threshold + leeway)):
                ifDone[y] = True
        ifDoneTemp = True
        for x in range(len(examples)):
            if (ifDone[x] == False):
                ifDoneTemp = False
                leeway = leeway + leewayAdj/len(examples)
        ifDoneOverall = ifDoneTemp
            recordOfLessonsInOnePass = cons(recordOfLessonsInOnePass,lesson(examples[y][1],prediction,examples[y][0],copy.deepcopy(weights)))
        recordOfPasses = cons(recordOfPasses,recordOfLessonsInOnePass)
    printPasses(recordOfPasses)
    return weights

def nextEntry(returnEntry):
    allreturns.append(returnEntry)
    for a in range(5):
        varAvgVar[a] = getAvgInArraySpot(a)
    if(##user says they want to enter info for NN):
        weightsTemp = perceptron(currentWeights,returnEntry);
        currentWeights = weightsTemp
    if(##user says they want to use NN):
        rating = 0
        for z in range(len(weights)):
        rating = rating + currentWeights[z]*returnEntry[1][z]
        return rating
    
    
    