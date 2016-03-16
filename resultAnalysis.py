import csv
import matplotlib.pyplot as plt

class Result:
	def __init__(self, name, accuracy):
		self.name = name
		self.accuracy = accuracy

correctAnswer = []
count = [0] * 100
# frequency = [0] * 100
accuracy = [0.0] * 100


with open('val.txt') as answerfile:
	filereader = csv.reader(answerfile)
	for row in filereader:
		oneAnswer = int(row[0].split()[1]);
 		correctAnswer.append(oneAnswer)
 		# frequency[oneAnswer] += 1;

i = 0
with open('baselineResult.val.csv') as resultfile:
	next(resultfile)
	filereader = csv.reader(resultfile)
	for row in filereader:
		if str(correctAnswer[i]) in row:
			count[correctAnswer[i]] += 1;
		i += 1

resultList = []
i = 0
with open('categories.txt') as categorytfile:
	filereader = csv.reader(categorytfile)
	for row in filereader:
		resultList.append(Result(row[0].split()[0],count[i]))
		i += 1

resultList.sort(key=lambda x: x.accuracy, reverse=True)

for i in range (0,100):
	print str(i) + " : " + resultList[i].name + "  " + str(resultList[i].accuracy)