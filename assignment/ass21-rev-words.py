#PROGRAM TO REVERSE WORDS IN  A STRING

my_str = "welcome to Python Programming"
#first we have to split the entire string into multiple parts or words
words = my_str.split(" ")
print(words)
#after printing - we get multiple strings- multiple words ['welcome', 'to', 'Python', 'Programming']
words_=words[-1::-1]
#so first -1 represnts reversing the words and the 2nd -1 represnts going back to the first position
print(words_)
#we get- ['Programming', 'Python', 'to', 'welcome']
#next we have to join all the items
outputstr = ' '.join(words_)
print(outputstr)


#so total code is->
my_str = "welcome to Python Programming"
words = my_str.split(" ")
print(words)
words_=words[-1::-1]
outputstr = ' '.join(words_)
print(outputstr)


