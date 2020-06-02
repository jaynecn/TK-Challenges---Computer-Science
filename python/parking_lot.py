from datetime import datetime

class User:
  def __init__(self, name, is_admin=False):
    self.name = name
    self.is_admin = is_admin

class Warden(User):
  def __init__(self, name):
    super().__init__(name, is_admin=True)
    self.valid_tickets = []
  def __str__(self):
    return(f"I'm a new admin.  My name is {self.name}")
  def check_tickets(self, customer):
    tickets = customer.purchases
    print(f"{customer.name} tickets:")
    print(tickets)
    # checking = Tickets(ticket_name, ticket_price, ticket_is_valid)
    # if (ticket_is_valid == True):
    #   print("Your ticket is valid.")
    #   self.valid_tickets.append(checking)
    # else:
    #   print("Your ticket isn't valid")
  def issue_ticket(self):
    print("Your ticket isn't valid.  You have to pay a fine.")  
    
class Customer(User):
  def __init__(self, name):
    super().__init__(name)
    self.purchases = []
  def __str__(self):
    return(f"Hello I'm a new customer.  My name is {self.name} .")
  def purchase_ticket(self, ticket_name, ticket_price):
    purchase = Tickets(self, ticket_name, ticket_price)
    self.purchases.append(purchase)
    print(self.purchases)
    
jayne = Customer("Jayne")
print(jayne)


matt = Warden("matt")
print(matt)

class ParkingLot:
  def __init__(self, name):
    self.name = name
    self.parking_lot = []
  def __str__(self):
    return(f"New Parking lot created: {self.name}")
  def car_in_parking_lot(self, registration):
    car_added = Car(registration)
    self.parking_lot.append(car_added)
    print(f"{registration} added to {self.name}")
    print(self.parking_lot)
  def close_parking_lot(self):
    if (len(self.parking_lot) == 100):
      print(f"{self.name} parking lot is full")
    else:
      print(f"{self.name} parking lot: Spaces")
      
wood_street = ParkingLot("Wood Street")
print(wood_street)
wood_street.close_parking_lot()


class Car:
  def __init__(self, registration):
    self.registration = registration
    
wood_street.car_in_parking_lot('AB11')
print(wood_street.parking_lot)
    
class Tickets:
  def __init__(self, name, price, is_valid=True):
    self.name = name
    self.price = price
    
jayne.purchase_ticket('tuesday', 5)
matt.check_tickets(jayne)
    
class Purchase:
  def __init__(self, ticket, customer):
    self.ticket = ticket
    self.customer = customer
    self.purchase_price = ticket.price
    self.purchase_data = datetime.now()
    
