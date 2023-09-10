#WRITE PYTHON PROGRAM TO COUNT THE NUMBER OF STRINGS IN A LIST WHERE THE STRING LENGTH IS 2 OR MORE
#AND THE FIRST AND LAST CHARACTERS ARE SAME FROM A GIVEN LIST OF STRINGS

s=0
list1=['aba','121','kgf','abc']
for x in list1:
    if len(x)>1 and x[0]==x[-1]:
        print('the given words are:',x)
        s=s+1
print('no.of words you want:',s)
