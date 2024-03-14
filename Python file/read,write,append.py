# Read a file

# file = open('Random_text', 'r')
# print(file.read())

## Read file line by line:
# print(file.readline())
#
# while True:
#     line = file.readline()
#     if not line:
#         break
#     print(line)


## get lines as list :
# lines = file.readlines()
# print(lines)

# ##=> close a file:
# file.close()
#
# ##now the below code will show error: casuse the file is closed
# lines = file.readlines()
# print(lines)

# ###=> open file 'with' statemetn:
#
# with open('Random_text', 'r') as file:
#     print(file.read())


# #####=>  Write on an exiting file:
# with open('Random_text','a') as file:
#     file.write("now you have use append method keep up the good work")
#     my_list = ["my name is mohabbat\n", 'my id 4508\n', 'i am a student\n']
#     file.writelines(my_list)

##=> create a new file:
