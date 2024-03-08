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
student = {
    "name": "Mohabbat Hossain",
    "skills": ["python","c","javascript","java"],
    "id": "213-15-4508"
}

# print(student["name"])
# print(student["skills"])
# print(student.get("ida","not found! please check the key."))

##=> how to change dictionary item:
student["name"] = "Mohabbat Hossain Ridoy"
print(student)

#=> change multiple item using update() method:
student.update(
    {
        "name": "Rezwan coder",
        "id": "213-15-4559"
    }
)
print(student)