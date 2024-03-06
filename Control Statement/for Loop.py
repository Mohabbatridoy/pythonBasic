# my_list = ['mohabat','sfj','banana']
# for i in my_list:
#     print(i)
#
#
# for i in range(1,11):
#     if i == 5 :
#         break;
#     print(i)
#
# print("now continue time")
# for i in range(1,11):
#     if i >=5 and i<=7:
#         continue
#     print(i)


itemPrice = [10,50,60,100,500,600]
total_budget = 100
total_item_purches = 0

for i in itemPrice:
    total_budget -= i
    if total_budget <= 0:
        break
    total_item_purches += 1
print(total_item_purches)