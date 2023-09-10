# ASK THE USER TO INPUT A STRING OF ODD LENGTH, RETURN THE STRING LENGTH 3 FROM ITS MIDDLE.
# THE STRING LENGTH WILL BE ATLEAST 3.

st_r = input("Enter a string of odd no:")


def middle(st_r):
    if len(st_r) % 2 == 0:
        return 'Enter correct string of odd num and try again'
    else:
        i = int((len(st_r)-1)/2)
        return st_r[i-1:i+2]
print(middle(st_r))
