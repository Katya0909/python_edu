goods_lst = []
goods_number = 1
while True:
    action = input("Do you want to add new good to catalogue? y/n: ")
    if action in ["y", "n"]:
        if action == 'y':
            g_name = input("Enter goods name: ")
            g_price = input("Enter goods price: ")
            g_count = input("Enter goods quantity: ")
            g_unit = input("Enter goods unit: ")
            goods_lst.append((goods_number, {"name": g_name, "price": g_price, "quantity": g_count, "unit": g_unit}))
            goods_number += 1
            print("The good is added to the catalogue")
        else:
            if len(goods_lst) == 0:
                print("Goods list is empty")
            else:
                print(goods_lst)
            break
    else:
        print("You need to enter 'y' or 'n'")
