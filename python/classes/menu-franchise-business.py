class Menu:
  
  def __init__(self, name: str, items: dict, start_time: int, end_time: int):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self):
    return(f'Our {self.name} menu is available from {self.start_time}:00 up to {self.end_time}:00')

  def calculate_bill(self, purchased_items):
    total_price = []
    for item in purchased_items:
      total_price.append(self.items[item])
    return sum(total_price)

brunch = Menu(
  'brunch', 
  {
    'pancakes': 7.50,
    'waffles': 9.00,
    'burger': 11.00,
    'home fries': 4.50,
    'coffee': 1.50,
    'espresso': 3.00,
    'tea': 1.00,
    'mimosa': 10.50,
    'orange juice': 3.50
  },
  11,
  16
  )

early_bird = Menu(
  'early bird',
  {
  'salumeria plate': 8.00, 
  'salad and breadsticks (serves 2, no refills)': 14.00, 
  'pizza with quattro formaggi': 9.00, 
  'duck ragu': 17.50, 
  'mushroom ravioli (vegan)': 13.50, 
  'coffee': 1.50, 
  'espresso': 3.00,
  },
  15,
  18
)

dinner = Menu(
  'dinner',
  {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
  },
  17,
  23
)

kids = Menu(
  'kids',
  {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
  },
  11,
  21
)

arepas_menu = Menu(
  'arepas',
  {
  'arepa pabellon': 7.00, 
  'pernil arepa': 8.50, 
  'guayanes arepa': 8.00, 
  'jamon arepa': 7.50
  },
  10,
  20
)

class Franchise:

  def __init__(self, address: str, menus: list):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    print(f'This franchise is at {self.address}')

  def available_menus(self, time: int):
    available = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available.append(menu.name)
    return available

class Business:

  def __init__(self, name: str, franchises: list):
    self.name = name
    self.franchises = franchises

flagship_store = Franchise('1232 West End Road', [brunch, early_bird, dinner, kids])

new_installment = Franchise('12 East Mulberry Street', [brunch, early_bird, dinner, kids])

arepas_place = Franchise('189 Fitzgerald Avenue', [arepas_menu])

basta_fazoolin = Business('Take a Arepa', [arepas_place])