from flask import *
app = Flask(__name__)
import requests

def makeForm(data):
	index = [i for i in range(len(data)) if data.startswith('docssharedWizToggleLabeledLabelText exportLabel freebirdFormviewerViewItemsRadioLabel', i)]
	return (index)

names = [[]]
@app.route('/setup',methods = ['POST'])
def login():
	x = requests.get(request.form['link']).text.replace("\n","")
	INDEX_OF_MULTIPLE_CHOICE = makeForm(x)
	INDEXES_OF_INSERTION = []
	for e in INDEX_OF_MULTIPLE_CHOICE:
		print(x[e:e+100])
		INDEX_OF_INSERTION = x.find("</span>",e) + 7
		INDEXES_OF_INSERTION.append(INDEX_OF_INSERTION)

	indexOfQuestions = [i for i in range(len(x)) if x.startswith('radiogroup', i)]

	prev = 0
	cur = 0
	curO = 0
	fin = ""	
	for e in INDEXES_OF_INSERTION:
		
		
		if(len(indexOfQuestions) > 0 and e > indexOfQuestions[0]):
			cur += 1
			curO = 0
			names.append([])
			indexOfQuestions.pop(0)
			print(indexOfQuestions)

		nameC = str(cur) + " " + str(curO)
		fin += x[prev:e] + '<input type = "text" name =' + nameC + '/>'
		prev = e
		curO += 1
		names[cur].append(nameC)
	fin += x[prev:len(x)]

	print(names)
	return fin

if __name__ == '__main__':
   app.run(debug = True)

