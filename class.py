
class Device:
    def __init__(self, brand):
        self.brand = brand

    def power_on(self):
        print(f"{self.brand} device is now ON.")

    def power_off(self):
        print(f"{self.brand} device is shutting down.")

class Smartphone(Device):
    def __init__(self, brand, model, storage):
        
        super().__init__(brand)
        self.model = model
        self.storage = storage
        self.apps = []

    def install_app(self, app_name):
        self.apps.append(app_name)
        print(f"{app_name} installed on {self.model}.")

    def show_info(self):
        print(f"Smartphone Info: {self.brand} {self.model}, {self.storage}GB Storage, Apps: {self.apps}")


phone1 = Smartphone("Samsung", "Galaxy S23", 256)
phone2 = Smartphone("Apple", "iPhone 14", 128)

phone1.power_on()
phone1.install_app("WhatsApp")
phone1.show_info()

phone2.power_on()
phone2.install_app("Instagram")
phone2.show_info()
