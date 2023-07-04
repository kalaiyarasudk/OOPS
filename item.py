import csv


class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate


    def __connect(self):
        pass

    def __preper_body(self):
        return f"""
            Hi someone 
            {self.__name} , {self.quantity}
            available in Mystore
        """
    
    def __send(self):
        pass

    def send_mail(self):
        self.__connect()
        self.__preper_body()
        self.__send()
        print("Mail send sucessfully")

    @classmethod
    def instance_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get("price")),
                quantity=int(item.get("quantity")),
            )

    @staticmethod
    def isInteger(num):
        #to check the num is integer or not
        if isinstance(num, float):
            return num.is_integer()
        elif(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__} : ('{self.name}', {self.price}, {self.quantity})"