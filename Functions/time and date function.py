# import time
# print(time.time())
#
# sec = 1710048247.2733347
#
# #ctime()
# print(time.ctime(sec))
#
# #sleep()
# time.sleep(3)
# print("I am printing after 3 sec of current time exicute")
#
# #Local time
# print(time.localtime(1710048247.2733347))

# #=>> datetime
# import datetime
# # print(datetime.datetime.now())
# #
# # #current utc time
# # print(datetime.datetime.utcnow())
# #
# # # today
# # print(datetime.date.today())
#
# ##=> time tuple
# current_datetime= datetime.datetime.now()
# struct_time_obj = current_datetime.timetuple()
# print(struct_time_obj[0])
# print(struct_time_obj[1])
# print(struct_time_obj[2])

##=> date formating :
from datetime import datetime

# current_datetime = datetime.now()
# print(current_datetime)
#
# # strftime() method
# print(datetime.strftime(current_datetime, "%d/%m/%Y %H:%H:%S"))

book_creation_date = "04, march, 2024"
actualDate = datetime.strptime(book_creation_date, "%d, %B, %Y")
print(actualDate)
print(type(actualDate))