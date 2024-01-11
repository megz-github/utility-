items_in_stock = [#this statement have all the information about the items in the vending machine
    {
        "item_id": 0,
        "item_name": "Biscuits",
        'item_price': 8,
    },
    {
        "item_id": 1,
        "item_name": "Soda",
        'item_price': 3,
    },
    {
        "item_id": 2,
        "item_name": "Chips",
        'item_price': 2.5,
    },
    {
        "item_id": 3,
        "item_name": "Gum",
        'item_price': 2,
    },
    {
        "item_id": 4,
        "item_name": "Water",
        'item_price': 1,
    },
]


the_item = []

reciept = """
\t\tPRODUCT -- PRICE
"""

sum = 0

run = True

print("--------------Vending Machine-------------\n\n")#this statement displays a the messeage for welcoming the user
print("------------The Items In Stock:------------\n\n")

for i in items_in_stock:
    print(f"Item: {i['item_name']} --- Price: {i['item_price']} --- Item ID: {i['item_id']}")#prints the item name price and the id for the user to pick from


def machine(items_in_stock, run, the_item):
    while run:

        buy_item = int(input("\n\nEnter the item code of the product you want to buy: "))#to enter the item code of the product that the user chooses

        if buy_item < len(items_in_stock):
            the_item.append(items_in_stock[buy_item])
        else:
            print("THE PRODUCT ID IS WRONG!")

        more_items = str(input("press any key to add more items and press q to quit.. "))#after selecting the user's choice, they can either finish selecting the item or continue to select the item

        if more_items == "q":
            run = False

    rec_bool = int(input(("1. print the reciept? 2. only print the total sum .. ")))
    if rec_bool == 1:
        print(create_reciept(the_item, reciept))
    elif rec_bool == 2:
        print(sum(the_item))
    else:
        print("INVALID ENTRY")


def sum(the_item):
    sum = 0

    for i in the_item:
        sum += i["item_price"]

    return sum

def create_reciept(the_item, reciept):

    for i in the_item:
        reciept += f"""
        \t{i["item_name"]} -- {i['item_price']}
        """

    reciept += f"""
        \tTotal --- {sum(the_item)}
        
        
        """
    return reciept


if __name__ == "__main__":
    machine(items_in_stock, run, the_item)