class Client:
    def __init__(self, client_id, last_name, first_name, address, phone, driver_license, 
                 patronymic=None, email=None):
        self._client_id = client_id
        self._last_name = last_name
        self._first_name = first_name
        self._patronymic = patronymic
        self._address = address
        self._phone = phone
        self._email = email
        self._driver_license = driver_license

    @property
    def client_id(self):
        return self._client_id
    
    @client_id.setter
    def client_id(self, value):
        self._client_id = value

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def patronymic(self):
        return self._patronymic
    
    @patronymic.setter
    def patronymic(self, value):
        self._patronymic = value

    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, value):
        self._address = value

    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, value):
        self._phone = value

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        self._email = value

    @property
    def driver_license(self):
        return self._driver_license
    
    @driver_license.setter
    def driver_license(self, value):
        self._driver_license = value

    def __repr__(self):
        return "client_id=" + str(self.client_id) + ", " + \
               "last_name='" + str(self.last_name) + "', " + \
               "first_name='" + str(self.first_name) + "', " + \
               "patronymic='" + str(self.patronymic) + "', " + \
               "address='" + str(self.address) + "', " + \
               "phone='" + str(self.phone) + "', " + \
               "email='" + str(self.email) + "', " + \
               "driver_license='" + str(self.driver_license) + "'" 

client = Client(
    client_id=1,
    last_name="Петров",
    first_name="Александр",
    patronymic="Сергеевич",
    address="г.Краснодар, ул.Красная, д.9",
    phone="+78005553535",
    driver_license="111111111111111",
    email="petrovas@yandex.ru"
)

print(client)
