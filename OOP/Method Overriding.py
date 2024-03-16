class User:
    def __init__(self,user_name,Total_Purchase):
        self.name = user_name
        self.Total_purchase = Total_Purchase

    def getShippingcost(self):
        if self.Total_purchase >= 1000:
            return 40
        return 60

class premiumUser(User):
    def getDiscount(self):
        if self.Total_purchase >=2000:
            return 100
        return 20

    ##override
    def getShippingcost(self):
        return 0

user = premiumUser("asif",2000)
print(user.getShippingcost())
print(user.getDiscount())