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
# with open('testFile', 'w') as file:
#     file.write("this is for test purpose")


# ##problem :
# user_data = [
#     {
#         'fileName': 'user1.tet',
#         'context' : "Hello This is from user 1"
#     },
#     {
#         'file_name' : 'user2',
#         'context' : "Hello this is from user 2"
#     },
#     {
#         'file_name': 'user3',
#         'context': "Hello this is from user 3"
#     }
# ]
#
# with open('user1', 'w') as file:
#     file.write("Hello This is from user 1")
# with open('user2', 'w') as file:
#     file.write("Hello This is from user 2")
# with open('user3', 'w') as file:
#     file.write("Hello This is from user 3")

##=> deleting a file:
import os
path = 'user1'
if os.path.isfile(path) :
    os.remove(path)
    print("successfully removed")
else:
    print("the file is not exits")