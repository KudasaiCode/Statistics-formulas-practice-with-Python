import math
import re

def mean(num_set):
	avg = 0
	for i in num_set:
		avg += float(i)
	return float(avg/len(num_set))
		
def variance(num_set):
	vari = 0
	for i in num_set:
		vari += pow(float(i) - mean(num_set), 2)
	return vari/len(num_set) 
	
def stndDev(num_set):
	return math.sqrt(variance(num_set))
	
def corrCoef(num_set_1, num_set_2):
	product_stnd_units = 0
	for i in range(len(num_set_1)):
		stnd_unit_1 = (float(num_set_1[i]) - mean(num_set_1))/stndDev(num_set_1)
		stnd_unit_2 = (float(num_set_2[i]) - mean(num_set_2))/stndDev(num_set_2)
		product_stnd_units += (stnd_unit_1 * stnd_unit_2)
	return product_stnd_units/len(num_set_1)
	
print('Enter all the numbers in the set,\n\n"c" to clear the entry,' +
	  '\n"d" to delete the last entry,\n"u" to undo last action,' + 
	  '\nLeave blank to complete:')

inputNum = 0
numList = list()
numList2 = list()
undoList = list()


while inputNum != "end":
	inputNum = input('#')
	if inputNum == '':
		break
	elif inputNum in ('c','C'):
		undoList.append(numList.copy())
		numList.clear()
	elif inputNum in ('d','D'):
		undoList.append(numList.copy())
		numList.pop()
	elif inputNum in ('u','U'):
		numList =  undoList.pop()
		
	if re.compile("\d").match(inputNum):
		numList.append(inputNum)
	print(numList)
	
	


print('\nMean: ' + str(mean(numList)))
print('Variance: ' + str(variance(numList)))
print('Standard Deviation: ' + str(stndDev(numList)))

print('Correlation Coefficient: ' + str(corrCoef(numList, numList)))
