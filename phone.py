from item import Item

class Phone(Item):
 
    def __init__(self, name: str, price: float, quantity=0, broken_phone = 0):
       
       #call the function/method from the parent class using super()
        super().__init__(
            name, price, quantity
        )
        
            # Run validations to the received arguments
        assert broken_phone >= 0, f"Quantity {broken_phone} is not greater or equal to zero!"


            # Assign to self object
        self.broken_phone = broken_phone

