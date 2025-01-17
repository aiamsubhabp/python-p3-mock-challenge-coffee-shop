class Coffee:
    def __init__(self, name):
        self.name = name

        self._orders = []
        self._customers = []

    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3 and not hasattr(self, "name"):
            self._name = name
        
    def orders(self):
        return self._orders
    
    def customers(self):
        return list(set(self._customers))
        
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        total = 0

        for order in self._orders:
            total += order.price

        average_price = total/len(self._orders)
        return average_price
        

class Customer:

    all = [] 

    def __init__(self, name):
        self.name = name

        self._orders = []
        self._coffees = []

        Customer.all.append(self)
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        
    
    def orders(self):
        return self._orders
    
    def coffees(self):
        return list(set(self._coffees))
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        customer_amount_spent = {}

        for customer in cls.all:
            for order in customer._orders:
                if order.coffee == coffee:
                    if customer in customer_amount_spent:
                        customer_amount_spent[customer] += order.price
                    else:
                        customer_amount_spent[customer] = order.price
        
        if len(customer_amount_spent) == 0:
            return None
        else:
            return max(customer_amount_spent, key = customer_amount_spent.get)
    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

        self.coffee._orders.append(self)
        self.coffee._customers.append(self.customer)

        self.customer._orders.append(self)
        self.customer._coffees.append(self.coffee)

        Order.all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if isinstance(price, float) and 1.0 <= price <= 10.00 and not hasattr(self, "price"):
            self._price = price

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer

    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
    
