class Product:
    def __init__(self,name,price,description,quantity):
            self.name = name
            self.price = price
            self.description = description
            self.quantity = quantity
            

    def dbcollections(self):
        return( {
            'name' : self.name,
            'price' : self.price,
            'description' : self.description,
            'quantity' : self.quantity
        })