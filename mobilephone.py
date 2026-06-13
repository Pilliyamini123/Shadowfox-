#base class
class MobilePhone:
    def __init__(self,screen_type,network_type,dual_sim,front_camera,rear_camera,ram,storage):
        self.screen_type=screen_type
        self.network_type=network_type
        self.dual_sim=dual_sim
        self.front_camera=front_camera
        self.rear_camera=rear_camera
        self.ram=ram
        self.storage=storage
    def display(self):
        print("model:",self.model)
        print("Screen Type:",self.screen_type)
        print("Network Type:",self.network_type)
        print("Dual Sim:",self.dual_sim)
        print("Front Camera:",self.front_camera)
        print("Rear Camera:",self.rear_camera)
        print("RAM:",self.ram)
        print("Storage:",self.storage)
    def make_calls(self):
        print("Making calls...")
    def receive_calls(self):
        print("Receiving calls...")
    def take_a_picture(self):   
        print("Taking a picture...")
#child class Apple
class Apple(MobilePhone):
    def __init__(self,screen_type,network_type,dual_sim,front_camera,rear_camera,ram,storage):
        super().__init__(screen_type,network_type,dual_sim,front_camera,rear_camera,ram,storage)
        self.model="Apple"
    def display(self):
        super().display()
        print("This is an Apple mobile phone.")
#child class Samsung    
class Samsung(MobilePhone):
    def __init__(self,screen_type,network_type,dual_sim,front_camera,rear_camera,ram,storage):
        super().__init__(screen_type,network_type,dual_sim,front_camera,rear_camera,ram,storage)
        self.model="Samsung"
    def display(self):
        super().display()
        print("This is a Samsung mobile phone.")
# Apple objects
apple_phone1=Apple("touch screen","5G",False,"12MP","12MP","5GB","64GB")
apple_phone2=Apple("touch screen","5G",True,"12MP","12MP","6GB","128GB")
# Samsung objects
samsung_phone1=Samsung("AMOLED","4G",True,"8MP","32MP","8GB","128GB")
samsung_phone2=Samsung("AMOLED","5G",False,"10MP","48MP","12GB","256GB")
# Displaying details of Apple phones    
apple_phone1.display()
apple_phone2.display()
# Displaying details of Samsung phones
samsung_phone1.display()
samsung_phone2.display()
#display apple 1
print("Details of Apple Phone 1:")
apple_phone1.make_calls()
apple_phone1.receive_calls()
apple_phone1.take_a_picture()
#display apple 2
print("Details of Apple Phone 2:")  
apple_phone2.make_calls()   
apple_phone2.receive_calls()
apple_phone2.take_a_picture()
#display samsung 1
print("Details of Samsung Phone 1:")
samsung_phone1.make_calls()
samsung_phone1.receive_calls()      
samsung_phone1.take_a_picture()
#display samsung 2
print("Details of Samsung Phone 2:")
samsung_phone2.make_calls()
samsung_phone2.receive_calls()
samsung_phone2.take_a_picture()

