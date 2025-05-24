#task 9 Inheritance
#Create inheritance using MobilePhone as base class and Apple &
 #Samsung as child class 
'''1. The base class should have properties: 
1. ScreenType = Touch Screen 
2. NetworkType = 4G/5G 
3. DualSim = True or False 
4. FrontCamera = (5MP/8MP/12MP/16MP) 
5. rearCamera = (8MP/12MP/16MP/32MP/48MP) 
6. RAM = (2GB/3GB/4GB) 
7. Storage = (16GB/32GB/64GB)

2. Create basic mobile phone functionalities in the classes like:
 make_call, recieve_call, take_a_picture, etc. 
3. Use super() constructor for calling parent classes constructor 
4. Make some objects of Apple class with different properties 
5. Make some objects of Samsung class with different properties
'''

# Base class
class MobilePhone:
    def __init__(self, brand, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.brand = brand
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def make_call(self, number):
        print(f"{self.brand}: Calling {number}...")

    def receive_call(self):
        print(f"{self.brand}: Incoming call...")

    def take_picture(self):
        print(f"{self.brand}: Taking picture with {self.rear_camera} rear camera.")

# Child class: Apple
class Apple(MobilePhone):
    def __init__(self, model, *args):
        super().__init__("Apple", *args)
        self.model = model

# Child class: Samsung
class Samsung(MobilePhone):
    def __init__(self, model, *args):
        super().__init__("Samsung", *args)
        self.model = model

# Creating Apple objects
iphone = Apple("iPhone 13", "Touch Screen", "5G", False, "12MP", "48MP", "4GB", "128GB")
iphone.make_call("9876543210")
iphone.take_picture()

# Creating Samsung objects
galaxy = Samsung("Galaxy S21", "Touch Screen", "5G", True, "16MP", "64MP", "6GB", "256GB")
galaxy.receive_call()
galaxy.take_picture()
