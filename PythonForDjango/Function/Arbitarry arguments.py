def function(*args):
    print(args)
function("Mohababat","Hridoy")

##Arbitary keyword argument :
def func(**args):
    print(args)
func(fname="Mohabbat",lname="Hridoy")

##Both together:
def funct(*args,**kwargs):
    print(args,kwargs)
funct("23","43",fname="Mohabbat",lname="where is my ahliya")

