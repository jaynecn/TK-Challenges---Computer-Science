from datetime import datetime

class User:
  def __init__(self, name, is_admin=False):
    self.name = name
    self.is_admin = is_admin

class Warden(User):
  def __init__(self, name):
    super().__init__(name, is_admin=True)
  def close_parking_lot(self, ):
  def open_parking_lot(self, ):

class Customer(User):
  def __init__(self, name):
    super().__init__(name)
    self.purchases = []
  def purchase_ticket(self, ticket):
    purchase = Tickets(ticket, self)
    self.purchases.append(purchase)

# class Vendor(User):
#   def __init__(self, name):
#     super().__init__(name)
#     self.products = []
#   def create_product(self, product_name, product_price):
#     product = Product(product_name, product_price, self)
#     self.products.append(product)
    
class Tickets:
  def__init__(self, name, price):
    self.name = name
    self.price = price
    
class Purchase:
  def__init__(self, ticket, customer):
    self.ticket = ticket
    self.customer = customer
    self.purchase_price = ticket.price
    self.purchase_data = datetime.now()
    
    
    