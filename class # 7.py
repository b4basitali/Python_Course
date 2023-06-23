# task to create:
import func

# Currency Converter
print("press 1 for currency converter")
print("press 2 for temperature converter")
print("press 3 for unit converter")
print("press 4 for volume of cylinder calculator")
print("press 5 for surface area of cylinder calculator")
choice_user=int(input("please choose choice of converter"))
if choice_user==1:
    func.currency_converter()
elif choice_user==2:
    func.temperature_converter()
elif choice_user==3:
    func.Unit_Converter()
elif choice_user==4:
    func.volume_cylinder()
elif choice_user==5:
    func.surface_area_cylinder()
else:
    print("wrong option chosen")




# def add_items():
#     item_name=input("please state the item name")
#     item_price=int(input("please state the price"))
#     item_code=int(input("please state the item code"))
#     quantity_item=int(input("please state the quantity of item"))
#     item_list=[item_name,item_price,item_code,quantity_item]
#     return item_list
#
# item_inventory=add_items()
# main_inventory=[]
# main_inventory.append(item_inventory)
#
# def show_items(main_inventory_received):
#     print(main_inventory)
#     for i in main_inventory_received:
#         for j in i:
#             print(j)




