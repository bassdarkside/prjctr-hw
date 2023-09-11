# 1
class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def add(self, country):
        name = self.name + " " + country.name
        population = self.population + country.population
        return Country(name, population)


bosnia = Country("Bosnia", 10_000_000)
herzegovina = Country("Herzegovina", 5_000_000)

bosnia_herzegovina = bosnia.add(herzegovina)
bosnia_herzegovina.population  # 15_000_000
bosnia_herzegovina.name  # 'Bosnia Herzegovina'


# 2
class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def __add__(self, country):
        new_name = self.name + " " + country.name
        new_population = self.population + country.population
        return Country(new_name, new_population)


bosnia = Country("Bosnia", 10_000_000)
herzegovina = Country("Herzegovina", 5_000_000)

bosnia_herzegovina = bosnia + herzegovina
bosnia_herzegovina.population  # 15_000_000
bosnia_herzegovina.name  # 'Bosnia Herzegovina'


# 3
class Car:
    def __init__(self, brand, model, year, speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed >= 5:
            self.speed -= 5
        else:
            self.speed = 0

    def display_speed(self):
        return f"The speed of the {self.year} {self.brand} {self.model} is {self.speed} km/h."


car = Car("Tesla", "Model S", 2023)
print(car.display_speed())

car.accelerate()
print(car.display_speed())

car.brake()
print(car.display_speed())
