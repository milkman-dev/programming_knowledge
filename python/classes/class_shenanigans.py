class Store:
  items_in_store = {}
  money = 0

class Item:

  def __init__(self, name, price):
    self.name = name
    self.price = price
    self.is_stored = False
  
  def __repr__(self):
    for item in Store.items_in_store.keys():
      if item == self.name:
        self.is_stored = True
    return f"This item is an {self.name} and it costs {self.price} and it is {'stored' if self.is_stored else 'not stored'}"

  def save_item(self):
    Store.items_in_store[self.name] = self.price
    return Store.items_in_store

  def sell_item(self, name, price):
    Store.money += price
    item_sold = Store.items_in_store.pop(self.name)
    print(f"You just bought {self.name} and it cost you {self.price} the store now has {Store.money}")

class Shopper:

  def __init__(self, name, money, savings):
    self.name = name
    self.money = money
    self.savings = savings
  
  def __repr__(self):
    return f"This shopper name is {self.name} and it has {self.money} available to spend!"

  def atm(self):
    withdraw = input("How much money you want to get out?")
    self.savings -= int(withdraw)
    self.money += int(withdraw)
    return print(f"You now have {self.money} in your pockets and {self.savings} in your bank account")
  
  def buy(self):
    item_to_buy = input("What would you like to buy?")
    if item_to_buy in Store.items_in_store.keys() and class_instances.keys():
      item_price = Store.items_in_store[item_to_buy]
      self.money -= item_price
      item_instance = class_instances[item_to_buy]
      item_instance.sell_item(item_to_buy, item_price)



orange = Item("orange", 2.5)
banana = Item("banana", 3)
apple = Item("apple", 1.5)

class_instances = {"orange": orange, "banana": banana, "apple": apple}

print(orange)

orange.save_item()
banana.save_item()
apple.save_item()

print(Store.items_in_store)

logan = Shopper("Logan", 10, 1000)
print(logan)

logan.atm()
logan.buy()

print(Store.items_in_store)