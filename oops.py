# class civil_construction:
#     def __init__(self,sand,bricks,cement,iron):
#         self.sand=sand
#         self.bricks=bricks
#         self.cement=cement
#         self.iron=iron
#     def ccroad(self,stone):
#         print("following materials are required for cc road construction :")
#         print("sand in ton :",self.sand)
#         print("bricks in bags :",self.bricks)
#         print("cement in kgs :",self.cement)
#         print("iron in tons :",self.iron)
#         print("stone in tons :",stone)

# obj=civil_construction(3,100,20,4)
# obj.ccroad(5)










# # creating a class(non_veg)
# class non_veg:
#     def __init__(self,chicken,mutton,spices):
#         self.chicken=chicken
#         self.mutton=mutton
#         self.spices=spices
#     def chicken_curry(self):
#         print("chicken curry is ready using :" ,self.chicken,self.spices)
#     # single ingeritance
# class chicken_fry(non_veg):
#     def __init__(self,chicken,spices,mutton,lemon):
#         super().__init__(chicken,mutton,spices)
#         self.lemon=(lemon)
#         print("chicken fry is ready using :",self.chicken,self.spices,self.lemon )
    
# class veg:
#     def __init__(self,tamota,mirchi,onion,potato):
#         self.tamota=tamota
#         self.mirchi=mirchi
#         self.onion=onion
#         self.potato=potato
#     def potato_curry(self):
#         print("potato curry is ready using :",self.potato,self.onion,self.tamota)
# # multiple inheritance
# class veg_nonveg_items(non_veg,veg):





# obj2=chicken_fry("natukodi chicken","itc masala","mutton","rayalasima lemon")
# # obj2.chicken_curry()


# # creating object
# # obj1=non_veg("itc masala","natukodi chicken","goat mutton")
# # print(obj1.chicken)
# # print(obj1.mutton)
# # print(obj1.spices)
# # obj1.chicken_curry()










# class VegItems:
#     def __init__(self, potato, carrot, tomato, fruits):
#         self.potato = potato
#         self.carrot = carrot
#         self.tomato = tomato  
#         self.fruits = fruits

#     def veg_biriyani(self):
#         print("Veg biriyani is ready using:",
#               self.potato, self.carrot, self.tomato)


# class VegSalad(VegItems):
#     def __init__(self, potato, carrot, tomato, fruits, onion):
#         super().__init__(potato, carrot, tomato, fruits)
#         self.onion = onion

#     def salad(self):
#         print("I am making a salad using:",
#               self.fruits, "and", self.onion)


# # Parent class object
# obj1 = VegItems("Potato", "Carrot", "Tomato", "Apple")
# obj1.veg_biriyani()

# # Child class object
# # obj2 = VegSalad("Potato", "Carrot", "Tomato", "Apple", "Onion")
# # obj2.veg_biriyani()
# # obj2.salad()


