
from typeguard import typechecked
from interfaceDecarator import interface_decorator

#When defining an interface class, the startswith('I') must be .
#  Repository Interface
class IRepository():
    
    def get_by_id(self, id:int):
        pass

    def save(self):
        pass

    def delete(self):
        pass
   
#When defining an interface class, the class name startswith('I') must be.
#Customer interface
@interface_decorator(IRepository)   
class ICustomerRepository():
    
    def saveAll(self, entity):
        pass
    
#When defining an interface class, the class name startswith('I') must be.
#Order interface
@interface_decorator(IRepository)    
class IOrderRepository():
    
    def getAll(self, id:int):
        pass
    
# Base Class
@interface_decorator(IRepository)
class Base():
    @typechecked
    def __init__(self, id:int, name:str):        
        self.id = id
        self.name = name
        
    
    def get_by_id(self):
        print("get_by_id method run-->id:",self.id,"-->name:",self.name)
        
        
    def save(self):
        print("save method run--->id:",self.id,"-->name:",self.name)

    def delete(self):
        print("delete method run--->id:",self.id,"-->name:",self.name)
      
@interface_decorator(ICustomerRepository)   
class Customer(Base):
    #Base class'dan miras alına sınıflar
    @typechecked
    def saveAll(self, entity:str):
         print("saveAll method run--->entity:",entity)
         
@interface_decorator(IOrderRepository)           
class Order(Base):  
    #Base class'dan miras alına sınıflar
    @typechecked
    def getAll(self, id:int):
        print("getAll method run--->id:",id)       
# Kullanım Örneği
print("--------------Customer methods-----------------")
customer = Customer(21,"Mike")
customer.get_by_id()
customer.save()
customer.delete()
customer.saveAll("enttity")
print("--------------Order methods-----------------")
order= Order(2,"Fred")
order.get_by_id()
order.save()
order.delete()
order.getAll(41)
        

