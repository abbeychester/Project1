import os
import filecmp
from dateutil.relativedelta import *
from datetime import date

inFile = open("P1DataA.csv", "r")
lines = inFile.readlines()
inFile.close()
dictList = []
for line in lines:
	line = line.rstrip()
	student_dict = {}
	values = line.split(",")
	first_name = values[0]
	last_name = values[1]
	email = values[2]
	year = values[3]
	DOB = values[4]
	student_dict["first_name"] = first_name
	student_dict["last_name"] = last_name
	student_dict["email"] = email
	student_dict["year"] = year
	student_dict["DOB"] = DOB
	dictList.append(student_dict)

def getData(file):
	inFile = open(file, "r")
	lines = inFile.readlines()
	inFile.close()
	dictList = []
	for line in lines:
		line = line.rstrip()
		student_dict = {}
		values = line.split(",")
		first_name = values[0]
		last_name = values[1]
		email = values[2]
		year = values[3]
		DOB = values[4]
		student_dict["first_name"] = first_name
		student_dict["last_name"] = last_name
		student_dict["email"] = email
		student_dict["year"] = year
		student_dict["DOB"] = DOB
		dictList.append(student_dict)
	print(student_dict)
	return student_dict
# get a list of dictionary objects from the file
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows
getData("P1DataA.csv")
getData("P1DataB.csv")

def mySort(data,col):
	hand = open(data, "r")
	lines = hand.readlines()
	hand.close()
	dictList = []
	for line in lines:
		line = line.rstrip()
		student_dict = {}
		values = line.split(",")
		first_name = values[0]
		last_name = values[1]
		email = values[2]
		year = values[3]
		DOB = values[4]
		student_dict["first_name"] = first_name
		student_dict["last_name"] = last_name
		student_dict["email"] = email
		student_dict["year"] = year
		student_dict["DOB"] = DOB
		dictList.append(student_dict)
	keylist = student_dict.keys()
	print(student_dict["first_name"], student_dict["last_name"])

# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName

mySort("P1DataA.csv", "firstName")
getData("P1DataB.csv", "firstName")

def classSizes(data):
	hand = open(data, "r")
	lines = hand.readlines()
	hand.close()
	dictList = []
	yearDict = {}
	yearDict['Freshman']: 0
	yearDict['Sophomore']: 0
	yearDict['Junior']: 0
	yearDict['Senior']: 0
	for line in lines:
		line = line.rstrip()
		student_dict = {}
		values = line.split(",")
		first_name = values[0]
		last_name = values[1]
		email = values[2]
		year = values[3]
		DOB = values[4]
		student_dict["first_name"] = first_name
		student_dict["last_name"] = last_name
		student_dict["email"] = email
		student_dict["year"] = year
		student_dict["DOB"] = DOB
		dictList.append(student_dict)
		if student_dict["year"] == 'Freshman':
			yearDict['Freshman'] +=1
		elif student_dict['year'] == 'Sophomore':
			yearDict['Sophomore'] +=1
		elif student_dict['year'] == 'Junior':
			yearDict['Junior'] += 1
		else:
			yearDict['Senior'] += 1
	print(sorted(student_dict, key = lambda k: k[1], reverse=True))

# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

classSizes(student_dict)

def findMonth(a):
	inFile = open(file, "r")
	lines = inFile.readlines()
	inFile.close()
	x = {}
	x['1'] = 0
	x['2'] = 0
	x['3'] = 0
	x['4'] = 0
	x['5'] = 0
	x['6'] = 0
	x['7'] = 0
	x['8'] = 0
	x['9'] = 0
	x['10'] = 0
	x['11'] = 0
	x['12'] = 0
	for line in lines:
		line = line.rstrip()
		values = line.split(',')
		DOB = values[4]
		splitDOB = DOB.split('/')
		month = splitDOB[0]
		for a in month:
			if a == '1':
				x['1'] = x['1'] + 1
			elif a == "2":
				x['2'] = x['2'] + 1
			elif a == "3":
				x['3'] = x['3'] + 1
			elif a == "4":
				x['4'] = x['4'] + 1
			elif a == "5":
				x['5'] = x['5'] + 1
			elif a == "6":
				x['6'] = x['6'] + 1
			elif a == "7":
				x['7'] = x['7'] + 1
			elif a == "8":
				x['8'] = x['8'] + 1
			elif a == "9":
				x['9'] = x['9'] + 1
			elif a == "10":
				x['10'] = x['10'] + 1
			elif a == "11":
				x['11'] = x['11'] + 1
			else:
				x['12'] = x['12'] + 1
		sortedList = sorted(x, key=lambda k: month, reverse = True)
		return sortedList[0]

# Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data
findMonth(student_dict)

def mySortPrint(a,col,fileName):
	hand = open(fileName, "r")
	lines = hand.readlines()
	hand.close()
	dictList = []
	for line in lines:
		line = line.rstrip()
		student_dict = {}
		values = line.split(",")
		first_name = values[0]
		last_name = values[1]
		email = values[2]
		year = values[3]
		DOB = values[4]
		student_dict["first_name"] = first_name
		student_dict["last_name"] = last_name
		student_dict["email"] = email
		student_dict["year"] = year
		student_dict["DOB"] = DOB
		dictList.append(student_dict)
	download_dict = 'mySortPrint.csv'
	csv = open(download_dict, 'w')
	columnTitleRow = "first, last, email\n"
	csv.write(columnTitleRow)
	for key in student_dict:
		row = student_dict["first_name"] + student_dict["last_name"] + student_dict["email"]
		csv.write(row)
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written

mySortPrint(student_dict, "first_name", "mySortPrint.csv")

def findAge(a):
	inFile = open(file, "r")
	lines = inFile.readlines()
	inFile.close()
	current_year = 2018
	age_list = []
	for line in lines:
		line = line.rstrip()
		values = line.split(',')
		DOB = values[4]
		splitDOB = DOB.split('/')
		year = splitDOB[2]
		age = current_year - year
		age_list.append(age)
	avg = sum(age_list)/len(age_list)
	return avg

findAge(student_dict)

# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.

################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
