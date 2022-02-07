import copy
from pickletools import read_uint1

class Address:
    def __init__(self, street_address, city, country):
        self.city = city
        self.street_address = street_address
        self.country = country
    
    def __str__(self):
        return "address sstrs"


class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"sterrrrrr name address"

class EmployeeFactory:
    main_office_employee = Employee("", Address("direccion", 0, "london"))
    aux_office_employee = Employee("", Address("direccion2", 0, "london"))

    @staticmethod
    def __new_employee(proto, name, suite):
        result = copy.deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result 


    @staticmethod
    def new_main_employee(name, suite):
        return EmployeeFactory.__new_employee(
                EmployeeFactory.main_office_employee,
                name, suite
            
        )


    @staticmethod
    def new_aux_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
                EmployeeFactory.aux_office_employee,
                name, suite
        )