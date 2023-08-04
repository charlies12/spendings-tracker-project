import json
"""Something to keep track of expenses. WIll keep track of the cost and name of item. User inputs price and name. Print
    item to a separate txt file."""


# item_name returns name of item as a string
def item_name():
    name_list = []
    begin = True
    while begin:
        name = input("Enter item name: \nEnter q to end entry.\n")
        if name.strip() == "":
            print("No name entered. Enter an item name.")
        else:
            name_list.append(name)
            if name.lower() == "q":
                name_list.pop()
                begin = False
                return name_list


# item_price returns price of item as a float
def item_price():

    price_list = []
    begin = True
    while begin:
        try:
            for name in result_item_name:
                price = float(input(f"Enter {name} price: \n"))
                price_list.append(price)
                if name == result_item_name[-1]:
                    begin = False
                    return price_list
        except ValueError:
            print("Enter only numbers and a decimal point if needed.")


# name_and_price will return a dictionary whose key:value pair is based on item name and item price
def name_and_price(name_value, price_value):
    result_item_name = name_value
    result_item_price = price_value

    name_and_price_pairs = dict(zip(result_item_name, result_item_price))
    return name_and_price_pairs


# total_cost returns only the values from the name_and_price_pairs dictionary and total money spent as a key.
def total_cost():
    count = 0
    for value in name_and_price(result_item_name, result_item_price).values():
        count += value
    total = dict(total=count)
    return total


# writes name, price, and total to a file using json import
def copy_to_file():
    with open("purchases_tracker", "a+") as file:
        file.write(json.dumps(name_and_price(result_item_name, result_item_price)) + "\n")
        file.write(json.dumps(total_cost()) + "\n")


if __name__ == '__main__':
    result_item_name = item_name()
    result_item_price = item_price()
    copy_to_file()
