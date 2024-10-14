#--- Task 1 ---

# create an "Order" class includes: list of meal orders, table number, and next 
class Order:

    def __init__(self, orders, table_num):
        self.orders = orders
        self.table_num = table_num
        self.next = None

# -------  Task 2  -------

class Kitchen:
 
    # adds order to kitchen queue
    def __init__(self):
        self.head = None
        self.tail = None

    # removes order from the queue ??
    def add_order(self, orders, table_num):
        new_order = Order(orders, table_num)
        if self.head == None:
            self.head = new_order
            self.tail = new_order
        else:
            self.tail.next = new_order
            self.tail = new_order

    def cook_order(self):
        if self.head is None:
            print("We are done let's go HOME!")
        else:
            print(f"Cooking order for table {self.head.table_num}: {self.head.orders}")
            self.head = self.head.next
        
    # views orders
    def view_orders(self):
        current = self.head
        while current:
            print(f"Table {current.table_num}: {current.orders}")
            current = current.next





kitchen = Kitchen()

# adding order for this simulation
kitchen.add_order(["chicken salad", "diet coke"], 1)  
kitchen.add_order(["pizza", "wings"], 2)              
kitchen.add_order(["cheesecake", "coffee"], 3)  


# Starting view of order
print("Orders ready!!")
kitchen.view_orders()
print(60* "=")

# First one gets wiped up
kitchen.cook_order()

# Whats next?
print("What's next!?")
kitchen.view_orders()
print(60* "=")

# Second one gets jiggy
kitchen.cook_order()

# Alright whats next?
print("Pizza going out! What next?")
kitchen.view_orders()
print(60* "=")

# Ramsey styling
kitchen.cook_order()

# Nothing left no visual
print("Desert done!! It's past closing time I want to get out of here whats next!")
kitchen.view_orders()
print(60* "=")

#cooks anyways
kitchen.cook_order()

