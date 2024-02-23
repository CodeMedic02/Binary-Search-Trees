# Name: Trent Adams
# Date: 2024-11-02


class Client:
    def __init__(self, client_id=0, first_name="Unknown", last_name="Unknown", phone="Unknown", email="Unknown"):
        self.__client_id = client_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__phone = phone
        self.__email = email

    def __lt__(self, other):
        return self.__client_id < other.__client_id

    def __le__(self, other):
        return self.__client_id <= other.__client_id

    def __eq__(self, other):
        return self.__client_id == other.__client_id

    def __str__(self):
        return "[" + str(self.__client_id) + "]"

    # Getters and Setters

    def get_client_id(self):
        return self.__client_id
    
    def get_first_name(self):
        return self.__first_name
    
    def get_last_name(self):
        return self.__last_name
    
    def get_phone(self):
        return self.__phone
    
    def get_email(self):
        return self.__email
    
    def set_client_id(self, client_id):
        self.__client_id = client_id
