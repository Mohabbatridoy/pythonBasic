# # Declaring dictionary:
# student = {
#     "firstName": "Mohabbat",
#     "lastName": "Hridoy",
#     "id": "213-15-4508"
# }
# #empty dictionary:
# emptDic = {}
# emptset = set()
# print(type(emptset))
# print(type(emptDic))
#
# print(student)

#access item from dictionary:
# student = {
#     "name": "Mohabbat Hossain",
#     "skills": ["python","c","javascript","java"],
#     "id": "213-15-4508"
# }
#
# # print(student["name"])
# # print(student["skills"])
# # print(student.get("ida","not found! please check the key."))
#
# ##=> how to change dictionary item:
# student["name"] = "Mohabbat Hossain Ridoy"
# print(student)
#
# #=> change multiple item using update() method:
# student.update(
#     {
#         "name": "Rezwan coder",
#         "id": "213-15-4559"
#     }
# )
# print(student)


# ##Add item in dictionary:
# student = {
#     "firstName": "Mohabbat",
#     "lastName": "Hridoy",
#     "id": "213-15-4508"
# }
#
# student["middleName"] = "Hossain"
# student.update(
#     {
#         "University": "Daffodil Internationa University"
#     }
# )
# print(student)


#=> Remove Item:
# std = {'firstName': 'Mohabbat',
#        'lastName': 'Hridoy',
#        'id': '213-15-4508',
#        'middleName': 'Hossain',
#        'University': 'Daffodil Internationa University'
# }

# del std['middleName']
# print(std)
# print(std.pop("lastName"))
# print(std)

# ##=> iterate dictionary by loop:
# #keys
# # print(std.keys())
# print(std.items())
# # print(std.values())
#
# for i in std.keys():
#     print(i, std[i])
# print("**************************")
# for key, item in std.items():
#     print(key, item)

####=> nested dictionary:
document = {
    1: {
        "name": "Mhr",
        "id": 4508
    },
    2: {
        "name": "hridoy",
        "id": 4208
    }
}

document[1]["name"] = "Mohabbat"
document[1]["cg"] = "3.60"
document.update(
    {
        3: {
            "name": "Hriody",
            "id": "213-154508"
        }
    }
)
print(document)

print(document[1]["id"])