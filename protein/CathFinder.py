"""
This program takes a CATH protein category file 
(cath-names.txt) as an input and separates the names 
based on the given filter.

The cath domain file can be downloaded from cath website:
https://www.cathdb.info/wiki?id=data:index

Written: Arjang Fahim
Last Modified: 9/8/2020

"""
FILE_NAME = "cath-domain-list.txt"

def LoadCathProteinName():
	lines = []
	file = open(FILE_NAME)
	for line in file:
		lines.append(line)
	return lines



#filter="1.10.8"
filter="2.10.10"
in_filter_list = filter.split(".")

class_code = ""

data = LoadCathProteinName()

for line in data:
	

	line_split = line.split()

	for index in range(1, len(in_filter_list)+1):
		if class_code == "":
			class_code = line_split[index]
		else:
			class_code = class_code + "." + str(line_split[index])

	if class_code != filter:
		class_code = ""
		continue
		
	else:	
		print(line_split[0])
	class_code = ""
	