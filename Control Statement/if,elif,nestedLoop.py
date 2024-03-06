area = "Mohakhali"
total_purches = 1500000

if area in ["Mirpur","Fargate","Dhanmodndi"]:
    if(total_purches >= 600):
        print("shipping free")
    elif(total_purches>=300 and total_purches<600):
        print("Shinpping cost 80")
    else:
        print("shipping cost 150")
elif area in ["Mohakhali","Gulshan"]:
    if(total_purches>=800):
        print("shipping cost is free")
    elif(total_purches>=500 and total_purches<800):
        print("shipping cost 100")
    else:
        print("shipping cost 200")
else:
    print("Shipping currently not available")




#short hand(inline) if:
x = 34;
if x == 12: y= 23
else: y = "bokkor chokkor"
print(y)