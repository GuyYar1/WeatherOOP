from abc import ABC, abstractmethod

# Abstract Product (DeserializedObject) representing the product interface
class DeserializedObject(ABC):
    """Not In use !! This is To do list , arrange the semi like deserialize  but on a real pattern method"""
    @abstractmethod
    def process(self):
        pass

# Concrete Products (Deserialized Objects)
class RawDataObject(DeserializedObject):
    def process(self):
        # Deserialization logic for raw data
        # ...

class CachedDataObject(DeserializedObject):
    def process(self):
        # Deserialization logic for cached data
        # ...

class ErrorDataObject(DeserializedObject):
    def process(self):
        # Deserialization logic for error data
        # ...
        return {
            "date time": "",
            "temperature": "",
            "humidity": "",
            "description": ""  # self.weather_description
        }

# Factory Method (Abstract Creator)
class DeserializerFactory(ABC):
    @abstractmethod
    def create_deserialized_object(self, data: dict) -> DeserializedObject:
        pass

# Concrete Factories
class RawDataFactory(DeserializerFactory):
    def create_deserialized_object(self, data: dict) -> DeserializedObject:
        return RawDataObject()

class CachedDataFactory(DeserializerFactory):
    def create_deserialized_object(self, data: dict) -> DeserializedObject:
        return CachedDataObject()

class ErrorDataFactory(DeserializerFactory):
    def create_deserialized_object(self, data: dict) -> DeserializedObject:
        return ErrorDataObject()


# How to use this code:
  # data = {
  #         'Failure': None,
  #         'Fromcache': True,
 #        'RawData': {...}  # Your actual raw data here
 #    }
 #
 #    raw_data_factory = RawDataFactory()
 #    deserialized_object = raw_data_factory.create_deserialized_object(data)
    # Use deserialized_object.process() as needed


# short and simple example with summary

#
# # Abstract Product class
# class Vehicle(ABC):
# @abstractmethod
# # Factory Method (Abstract Creator)
# class VehicleFactory(ABC):
# @abstractmethod
#
#
# # Concrete Products
# class Car(Vehicle):
# 	create_vehicle
# # Concrete Products
# class Bicycle(Vehicle)
# 	create_vehicle
#
#
# # Concrete Factories
# class CarFactory(VehicleFactory):
# # Concrete Factories
# class BicycleFactory(VehicleFactory):
#
#
# Summary:
# # Concrete Factories is sub class.  VehicleFactory super class
# # The method of the Concrete Factories returns Concrete Products
