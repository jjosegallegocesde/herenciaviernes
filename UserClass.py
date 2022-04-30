class UserClass:
    def __init__(self, userName, phone, adress, typeOfVehicle):
        self.__userName = userName
        self.__phone = phone
        self.__adress = adress
        self.__priceHour = 0
        self.__typeOfVehicle = typeOfVehicle
        self.setPrice()

    @property
    def userName(self):
        return self.__userName

    @property
    def phone(self):
        return self.__phone

    @property
    def adress(self):
        return self.__adress

    @property
    def setPrice(self):
        if(self.__typeOfVehicle.lower() == "m"):
            self.__priceHour = 1000
        else:
            self.__priceHour = 2000

    @property
    def priceHour(self):
        return self.__priceHour
