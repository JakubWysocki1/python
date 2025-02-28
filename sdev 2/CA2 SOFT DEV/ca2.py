"""
Jakub Wysocki
X00164430
CA2
"""
import csv


class ProductUtility:
    VAT = 1.23

    @staticmethod
    def menu():
        print("*"*80)
        print("*{:^78}*".format("Computer Accessory System"))
        print("*"*80)
        print("*{:78}*".format(" 1) List All Stock"))
        print("*{:78}*".format(" 2) List Low-stock Products"))
        print("*{:78}*".format(" 3) Reorder Low Stock"))
        print("*{:78}*".format(" 4) Make a Sale"))
        print("*{:78}*".format(" 5) Add a New Product"))
        print("*{:78}*".format(" 6) Product and Stock on Hand"))
        print("*{:78}*".format(" 7) Exit"))
        print("*" * 80)

    @staticmethod
    def display_stock(csv_list_in):
        print("{:20}{:^17}{:^26}{:^20}{:^20}{:^24}".format("ID", "Name","Cost Price €","Selling Price €",
                                                           "Quantity On Hand", "Re-order lever"))
        for i in csv_list_in:
            for item in i:
                stock = str(item)
                print("{:<23}".format(stock), end="")
            print()

    @staticmethod
    def display_low_stock(csv_list_in):
        low_stock_counter = 0
        print("*" * 75)
        print("{:20}{:20}{:20}{}".format("ID", "Name","Quantity", "Re-order level"))
        print("*" * 75)
        for i in csv_list_in:
            if int(i[4]) <= int(i[5]):  #if quantity is less than or equal re order level
                low_stock_counter += 1
                print("{:20}{:20}{:<20}{:<20}".format(i[0], i[1], i[4], i[5])) #prints out id, name, quantity and reorder level for each row of 2d list
        print()
        print("Number of low stock items:", low_stock_counter)

    @staticmethod
    def reorder_low_stock(csv_list_in):
        reorder_counter = 0
        for i in csv_list_in:
            if int(i[4]) < int(i[5]): #if quantity is less than or equal re order level
                reorder_counter += 1
                i[4] = i[5] #The 4th column of the row (quantity) gets set to the 5th (reorder level)
                print("{:20}{:20}{:<20}{:<20}".format(i[0],i[1],i[4],i[5]))
        print()
        print("Number of products raised to re-order level:", reorder_counter)

    @staticmethod
    def make_sale(csv_list_in, id_item_in, quantity_in):
        cost = 0
        qty_hand = ProductUtility.get_qty(csv_list, id, quantity) #calls the get_qty method to check if there is sufficient items in stock
        if qty_hand: #if sufficient items in stock , the for loop gets executed. otherwise the cost will be retured as 0 which was set at the start
            for i in csv_list_in:
                if id_item_in in i: #finds the row in which the item searched for is in
                    cost = (float(i[3]) * ProductUtility.VAT) * int(quantity_in) #cost is the price represented by 3rd column in the row * the constant * quantity
                    i[4] = int(i[4]) - int(quantity_in) #reduces the quantity in the list by the amount sold
        return cost

    @staticmethod
    def get_qty(csv_list_in, id_item_in, quantity_in):
        for i in csv_list_in:
            if id_item_in in i:
                if quantity_in < int(i[4]): #checks if there is more in stock than the person wants to buy. If not nothing is returned
                    return i[4] #Returns amount in stock

    @staticmethod
    def add_product(csv_list_in, id_in, name_in, cost_price_in, selling_price_in, quantity_on_hand_in, reorder_lvl_in):
        product = [id_in,name_in,cost_price_in,selling_price_in,quantity_on_hand_in,reorder_lvl_in]
        csv_list_in.append(product)
        print()
        print("Product added")

    @staticmethod
    def create_dictionary(csv_list_in):
        dictionary = {}
        print("{:20}{:20}".format("Accessory ID", "Quantity on Hand"))
        print("_"*35)
        for i in csv_list_in:
            if i[0] not in dictionary: #Makes sures there is no duplicates
                dictionary[i[0]] = i[4] #sets the key as the id and the term as the quantity
        for key in dictionary:
            print("{:10}{:>20}".format(key, dictionary[key]))

ProductUtility.menu()
choice = int(input("Enter an option: "))

with open("products.csv","r") as infile:
    csv_list = list(csv.reader(infile))


while choice != 7:
    if choice == 1:
        ProductUtility.display_stock(csv_list)

    elif choice == 2:
        ProductUtility.display_low_stock(csv_list)

    elif choice == 3:
        ProductUtility.reorder_low_stock(csv_list)

    elif choice == 4:
        id = input("Enter the id number: ")
        quantity = int(input("Enter the quantity: "))
        sale = ProductUtility.make_sale(csv_list, id, quantity)
        if sale == 0:
            print("Error getting cost of sale. ID of item doesnt exist or there is not enough in stock")
        print("Cost of the sale: €", round(sale, 2))

    elif choice == 5:
        add_id = input("Enter the id of the product you want to add: ")
        add_name = input("Enter the name of the product: ")

        add_costprice = float(input("Enter the cost price of the product: €"))
        while add_costprice <= 0:
            add_costprice = float(input("Re-Enter the cost price of the product (Greater than 0): €"))

        add_sellprice = float(input("Enter the selling price of the product: €"))
        while add_sellprice < add_costprice:
            add_sellprice = float(input("Re-Enter the selling price of the product (Must be bigger than cost price) : €"))

        add_qtyhand = int(input("Enter the quantity on hand: "))
        add_reorderlvl = int(input("Enter the re-order level: "))
        ProductUtility.add_product(csv_list, add_id, add_name, add_costprice, add_sellprice, add_qtyhand, add_reorderlvl)

    elif choice == 6:
        ProductUtility.create_dictionary(csv_list)

    else:
        print("Error: re-enter option ")

    print()
    ProductUtility.menu()
    choice = int(input("Enter an option: "))
    print()

if choice == 7:
    with open("stock.csv", "w", newline='') as outfile:
        for row in csv_list:
            write = csv.writer(outfile)
            write.writerow(row)