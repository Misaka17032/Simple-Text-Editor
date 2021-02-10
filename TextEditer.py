# -*- coding: utf-8 -*-
print "+---------+------+------+------+------+"
print "|    1    |   2  |   3  |   4  |   5  |"
print "+---------+------+------+------+------+"
print "| Setting | Read | Edit | Find | Exit |"
print "+---------+------+------+------+------+"
words_space = 1
while True:
	function = input("Input the number:")
	if function == 1:
		print "1.Set the space between words."
		setting = input("Input the set number:")
		if setting == 1:
			words_space = input("How many spaces do you want to see between words:")
		else:
			print "Please input the right number!"
	elif function == 2:
		result = ""
		path = raw_input("Input the path of the file:")
		f = open(path,"r+")
		text = f.read()
		array = text.split(" ")
		for t in array:
			result = result + t
			for i in range(words_space):
				result = result + " "
		print result
	elif function == 3:
		path = raw_input("Input the path of the file:")
		text = raw_input("Input the text:")
		f = open(path, "w")
		f.write(text)
		f.close()
	elif function == 4:
		num = 0
		is_find = False
		path = raw_input("Input the path of the file:")
		ftext = raw_input("Input the words you want to find:")
		f = open(path,"r+")
		text = f.read()
		array = text.split("\n")
		for t in array:
			num = num + 1
			result = t.find(ftext,0,len(t))
			if result != -1:
				print "The words you are finding is in " + str(result) + "th, line " + str(num)
				is_find = True
		if is_find == False:
			print "Sorry, text not found."
	elif function == 5:
		break
	else:
		print "Please input the right number!"