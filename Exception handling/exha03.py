
# using else condition also in exception handling

try:
    file = open('ramya03','r')
    print(file.read())
except FileNotFoundError as e:
    print("File not found")
except IOError:
    print("An error occurred while reading the file")
else:
    print("File reading completed successfully")
finally:
    print("always executed, no matter what!")