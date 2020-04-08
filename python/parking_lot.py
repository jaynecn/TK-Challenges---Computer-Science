from datetime import datetime

class User:
  def __init__(self, name, is_admin=False):
    self.name = name
    self.is_admin = is_admin

class Warden(User):
  def __init__(self, name):
    super().__init__(name, is_admin=True)
    valid_tickets = []
  def check_tickets(self, ticket, customer):
    checking = Tickets(self, name, is_valid)
    if (is_valid == True):
      self.valid_tickets.append(checking)    
    
class Customer(User):
  def __init__(self, name):
    super().__init__(name)
    self.purchases = []
  def purchase_ticket(self, ticket):
    purchase = Tickets(ticket, self)
    self.purchases.append(purchase)

class ParkingLot:
  def__init__(self, name):
    self.name = name
    self.parking_lot = []
  def car_in_parking_lot(self, ):
    car_added = Car(car_registration, self)
    self.parking_lot.append(car_added)
  def close_parking_lot(self):
    if (len(parking_lot) == 100):
      print("Parking lot is full")
    else print ("Spaces")


class Car:
  def__init__(self, registration):
    self.registration = registration
    
class Tickets:
  def__init__(self, name, price, is_valid=True):
    self.name = name
    self.price = price
    
class Purchase:
  def__init__(self, ticket, customer):
    self.ticket = ticket
    self.customer = customer
    self.purchase_price = ticket.price
    self.purchase_data = datetime.now()
    
