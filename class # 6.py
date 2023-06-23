#task to create:
#Currency Converter
def currency_converter(amount_received,PKR_currency_received):
    if PKR_currency_received=="D":
        new_currency_received=(amount_received/272)
        return new_currency_received

    elif PKR_currency_received=="E":
        new_currency_received=(amount_received/300)
        return new_currency_received

    elif PKR_currency_received=="P":
        new_currency_received=(amount_received/350)
        return new_currency_received


    else:
        print("wrong currency stated")





amount_PKR=int(input("please state the amount to be converted"))
PKR_currency=input("do you want it in dollar(D), or Euro(E), or Pound(P)")
after_conversion=currency_converter(amount_PKR,PKR_currency)
print(after_conversion)
#Unit Converter
#temprature converter
#calculate volume or surface area of cylinder

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




