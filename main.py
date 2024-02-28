class Passenger:
    def __init__(self, firstName="", lastName="", passportNo="", email="", phoneNo=0, nationality=""):
        self._firstName = firstName
        self._lastName = lastName
        self._passportNo = passportNo
        self._email = email
        self._phoneNo = phoneNo
        self._nationality = nationality

    def set_firstName(self, firstName):
        self._firstName = firstName

    def get_firstName(self):
        return self._firstName

    def set_lastName(self, lastName):
        self._lastName = lastName

    def get_lastName(self):
        return self._lastName

    def set_passportNo(self, passportNo):
        self._passport = passportNo

    def get_passportNo(self):
        return self._passportNo

    def set_email(self, email):
        self._email = email

    def get_email(self):
        return self._email

    def set_phoneNo(self, phoneNo):
        self._phoneNo = phone_no

    def get_phoneNo(self):
        return self._phoneNo

    def set_nationality(self, nationality):
        self._nationality = nationality

    def get_nationality(self):
        return self._nationality

    def __str__(self):
        return f"Full Name: {self._firstName} {self._lastName}\n" \
               f"Passport Number: {self._passportNo}\n" \
               f"Email: {self._email}\n" \
               f"Phone Number: {self._phoneNo}\n" \
               f"Nationality: {self._nationality}"


passenger1 = Passenger("Hammad", "Al Zaabi", "H68DG4789H", "Hammad321@gmail.com", 971548733672, "Emirati")
print(passenger1)
passenger2 = Passenger("James", "Smith", "KJAEI231451", "SmithJames456@gmail.com", 13125096995, "American")
print(passenger2)

from enum import Enum


class TicketType(Enum):
    ECONOMY = "Economy"
    BUSINESS = "Business"
    FIRST_CLASS = "First Class"


class Ticket:
    def __init__(self, passengerName="", airportName="", flightNo="", seatNo="", ticketType=TicketType.BUSINESS,
                 price=0.0):
        self.__passengerName = passengerName
        self.__airportName = airportName
        self.__flightNo = flightNo
        self.__ticketType = ticketType
        self.__seatNo = seatNo
        self.__price = price

    def get_passengerName(self):
        return self.__passengerName

    def set_passengerName(self, passengerName):
        self.__passengerName = passengerName

    def get_airportName(self):
        return self.__airportName

    def set_airportName(self, airportName):
        self.__airportName = airportName

    def get_flightNo(self):
        return self.__flightNo

    def set_flightNo(self, flightNo):
        self.__flightNo = flightNo

    def get_seatNo(self):
        return self.__seatNo

    def set_seatNo(self, seatNo):
        self.__seatNo = seatNo

    def ticketType(self):
        return self.__ticketType

    def set_ticketType(self, ticketType):
        self.__ticketType = ticketType

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def __str__(self):
        return f"Passenger Name: {self.__passengerName}\n" \
               f"Airport Name: {self.__airportName}\n" \
               f"Flight Number: {self.__flightNo}\n" \
               f"Seat Number: {self.__seatNo}\n" \
               f"Ticket Type: {self.__ticketType.value}\n" \
               f"Price: ${self.__price:.2f}"


ticket1 = Ticket("Meera Budebes", "Abu Dhabi International Airport", "78GHJ", "32AA", TicketType.ECONOMY, 345.9)
print(ticket1)
ticket2 = Ticket("James Smith", "Chicago ORD", "NA4321", "09A", TicketType.FIRST_CLASS, 1268.2)
print(ticket2)


class Airport:
    def __init__(self, name="", city="", country="", icaoCode="", iataCode=""):
        self.name = name
        self.city = city
        self.country = country
        self.icaoCode = icaoCode
        self.iataCode = iataCode

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_city(self):
        return self.city

    def set_city(self, city):
        self.city = city

    def get_country(self):
        return self.country

    def set_country(self, country):
        self.country = country

    def get_icaoCode(self):
        return self.icaoCode

    def set_icaoCode(self, icaoCode):
        self.icaoCode = icaoCode

    def get_iataCode(self):
        return self.iataCode

    def set_iataCode(self, iataCode):
        self.iataCode = iataCode

    def __str__(self):
        return f"Airport Name: {self.name}\n" \
               f"Located City: {self.city}\n" \
               f"Located Country: {self.country}\n" \
               f"Airport ICAO Code: {self.icaoCode}\n" \
               f"Airport IATA Code: {self.iataCode}"


airport1 = Airport("JFK International Airport", "New York City", "United States", "KFJK", "JFK")
print(airport1)


class Manager:
    def __init__(self, firstName="", lastName="", employeeID="", department="", salary=0.0):
        self._firstName = firstName
        self._lastName = lastName
        self._employeeID = employeeID
        self._department = department
        self._salary = salary

    def set_firstName(self, firstName):
        self._firstName = firstName

    def get_firstName(self):
        return self._firstName

    def set_lastName(self, lastName):
        self._lastName = lastName

    def get_lastName(self):
        return self._lastName

    def set_employeeID(self, employeeID):
        self._employeeID = employeeID

    def get_employeeID(self):
        return self._employeeID

    def set_department(self, department):
        self._department = department

    def get_department(self):
        return self._department

    def set_salary(self, salary):
        self._salary = salary

    def get_salary(self):
        return self._salary

    def view_flightInfo(self):
        pass

    def addFlight(self):
        pass

    def modifyFlight(self):
        pass

    def cancelFlight(self):
        pass

    def __str__(self):
        return f"Full Name: {self._firstName} {self._lastName}\n" \
               f"Employee ID: {self._employeeID}\n" \
               f"Department: {self._department}\n" \
               f"Salary: {self._salary} usd"


manager1 = Manager("Marie", "Lonberg", "56878Gh8f", "Marketing", 30000)
print(manager1)

from datetime import datetime


class Flight:
    def __init__(self, flightNo="", airportName="", departureCity="", arrivalCity="", departureDateTime=None,
                 arrivalDateTime=None):
        self._flightNo = flightNo
        self._airportName = airportName
        self._departureCity = departureCity
        self._arrivalCity = arrivalCity
        self._departureDateTime = self._datetime(departureDateTime)
        self._arrivalDateTime = self._datetime(arrivalDateTime)

    def set_flightNo(self, flightNo):
        self._flightNo = flightNo

    def get_flightNo(self):
        return self._flightNo

    def set_airportName(self, airportName):
        self._airportName = airportName

    def get_airportName(self):
        return self._airportName

    def set_departureCity(self, departureCity):
        self._departureCity = departureCity

    def get_departureCity(self):
        return self._departureCity

    def set_arrivalCity(self, arrivalCity):
        self._arrivalCity = arrivalCity

    def get_arrivalCity(self):
        return self._arrivalCity

    def set_departureDateTime(self, departureDateTime):
        self._departureDateTime = self._datetime(departureDateTime)

    def get_departureDateTime(self):
        return self._departureDateTime.strftime("%m/%d/%Y %H:%M")

    def set_arrivalDateTime(self, arrivalDateTime):
        self._arrivalDateTime = self._datetime(arrivalDateTime)

    def get_arrivalDateTime(self):
        return self._arrivalDateTime.strftime("%m/%d/%Y %H:%M")

    def _datetime(self, datetime_str):
        return datetime.strptime(datetime_str, "%m/%d/%Y %I:%M %p")

    def __str__(self):
        return f"Flight Number: {self._flightNo}\n" \
               f"Airport Name: {self._airportName}\n" \
               f"Departure City: {self._departureCity}\n" \
               f"Arrival City: {self._arrivalCity}\n" \
               f"Departure Date & Time: {self._departureDateTime.strftime('%m/%d/%Y %H:%M')}\n" \
               f"Arrival Date & Time: {self._arrivalDateTime.strftime('%m/%d/%Y %H:%M')}"


flight1 = Flight("BA1442", "Haneda Airport", "Tokyo", "Seoul", "03/05/2024 12:00 AM", "03/05/2024 02:40 AM")
print(flight1)
flight2 = Flight("NA4321", "Chicago ORD Airport", "Chicago", "New York City", "12/06/2020 11:40 AM",
                 "12/06/2020 01:30 PM")
print(flight2)