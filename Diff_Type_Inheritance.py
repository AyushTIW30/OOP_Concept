# class Phone:
#     def __init__(self,name,price,camera):
#         print("Inside the phone class")
#         self.name = name
#         self.price = price
#         self.camera = camera
#     def buy(self):
#         print("buying a phone")


# class Smartphone(Phone):
#     pass

# s = Smartphone("Apple",1500000,"AI").buy()

###############        MULTILEVEL         ####################
# class Product:
#     def review(self):
#         print("produce customer review")
# class Phone(Product):
#     def __init__(self,name,price,camera):
#         print("Inside the phone class")
#         self.name = name
#         self.price = price
#         self.camera = camera
#     def buy(self):
#         print("buying a phone")


# class Smartphone(Phone):


#     pass

# class Newphone(Smartphone):
#     pass

# class Featurephone(Newphone):
#     pass

# s = Featurephone("Apple",1500000,"AI")
# t = Smartphone("pineapple",1500000,"AI")
# s.buy()
# print(s.name)
# s.review()
# print(s.camera)


######################    HIERARCHICAL   #############################



# class Phone:
#     def __init__(self,name,price,camera):
#         print("Inside the phone class")
#         self.name = name
#         self.price = price
#         self.camera = camera
#     def buy(self):
#         print("buying a phone")


# class Smartphone(Phone):
#     pass
# class Featuredphone(Phone):
#     pass

# Smartphone("pineapple",1500000,"AI").buy()
# Featuredphone("Apple",1500000,"AI").buy()


#########################     MULTIPLE    #############################



class Product:
    def review(self):
        print("produce customer review")
    def buy(self):
        print("buying a product")
class Phone:
    def __init__(self,name,price,camera):
        print("Inside the phone class")
        self.name = name
        self.price = price
        self.camera = camera
    def buy(self):
        print("buying a phone")


class Smartphone(Product,Phone):
    pass

S =  Smartphone("pineapple",1500000,"AI")
S.review()
S.buy()



############################   HYBRID  ############################





















