#alternate_character_str= "Hello World"
#print(alternate_character_str)
#string_length = len(alternate_character_str)
#print(string_length)
#alt_char_pos = alternate_character_str [0]
#x = "Hello World"
#length_of_str = len(x)
#print (length_of_str)
#new_string_upper = x[0:12:2].upper() #this singles out the data that needs to be upper case
#new_string_lower = x[1:11:2].lower() #this singles out the data that needs to be lower case 
#print (new_string_lower)
#print (new_string_upper)
#combined_string = new_string_upper+new_string_lower #this has just combined the two strings that i sliced so not the solution i am after 
#print(combined_string)
#.join function will only work with a loop
#x = input("enter a word, phrase or sentence: ")
#string_length = len(x)
#for n in range (len(x)):
#print((n+2)).upper()
#my previous attempts at trying to solve this problem

#Eventually, I found a solution as seen below. It is not as versitile id like it to be, i.e. does not ask user for input
#The question does not ask me to ask the user therefore the solution below applies
txt_1 = "Hello"
txt_2 = "World"
x = txt_1.split() #converting into a list so .replace can be used 
y = txt_1.replace("Hello", "HeLlO") #replace with the desired output
w = txt_2.split() #same as line 27
z = txt_2.replace("World", "WoRlD") #same as line 28
print(y +" "+ z) #added a space " " in the concatenation 

#part 2 of question, making each alternative word as upper or lower case 

a = txt_2.replace("World", "WORLD")
print (txt_1 + " " + a)

#I have not used .join() in this assingment as I have tried to avoid using concepts in lists as much as possible
#this is because lists and dictionaries is the next assignment 
#ideally I would like to find a solution that takes input from the user but given time contraints i have decided to hardcode values in


















