file_handler = open("order.txt", "r")

item_list = []
quantity_list = []
price_list = []

for record in file_handler:
    data = record.split("|")
    item_list.append( data[0] )
    quantity_list.append( int(data[1]) )
    price_list.append( float(data[2]) )

print("Item Name  | Qty |  Price")

for item in range(len(item_list)):
    print(f"{item_list[item]:10s} | {quantity_list[item]:3d} | {price_list[item]:6.2f}")
print(f"Total order: {sum(quantity_list)}")