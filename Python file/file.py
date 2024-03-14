# import os
# path = '../Functions'
# # # os.listdir(path)
# # all_files = os.listdir(path)
# #
# # for files in all_files :
# #     if os.path.isfile(os.path.join(path, files)):
# #         print("{} is a file".format(files))
#
#
# ##=>  os.scandir() method:
#
# all_files = os.scandir(path)
# for file in all_files:
#     if file.is_file():
#         print("{} is a file".format(file.name))
#
# ## using pathlib module:
#
# import pathlib
#
# path_obj = pathlib.Path(path)
# for file in path_obj.iterdir():
#     if file.is_file():
#         print(file.name)

##=> check if a file exists or not:
path = 'testFile'

#using os.path:
import os
print(os.path.isfile(path))

#using pathlib.Path:
import pathlib
file = pathlib.Path(path)
print(file.is_file())