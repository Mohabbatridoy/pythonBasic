my_list = ['mohabat','sfj','banana']
for i in my_list:
    print(i)


for i in range(1,11):
    if i == 5 :
        break;
    print(i)

print("now continue time")
for i in range(1,11):
    if i >=5 and i<=7:
        continue
    print(i)