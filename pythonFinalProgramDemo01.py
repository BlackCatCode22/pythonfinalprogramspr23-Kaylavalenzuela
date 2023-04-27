# pythonFinalProgramDemo01.py
# starting code by chatGPT!
# dH 4/13/23
# chatGPT 4/13/23

# Wow, chatGPT did a good job on this program but did not use file IO. In any event, here is the summary from
# chatGPT and I hope this will help you with your final programs. You might take chatGPT's advide and add
# additional features such as searching or filtering animals by various attributes.

# The Animal Zoo program is a Python class-based program that manages animal data for a zoo. It uses a dictionary data
# structure called "animals" to store a list of animals by species. Each animal is represented by an instance of the "Animal" class,
# which contains attributes such as species, name, age, birth season, color, gender, weight, and origin.

# When an animal is created, its ID is automatically generated based on its species and number of animals of that species
# already in the "animals" dictionary. The "get_birth_date()" method calculates the animal's birth date based on its age
# and birth season. The "str()" method returns a formatted string containing the animal's information, including its ID,
# name, age, birth date, color, gender, weight, origin, and arrival date.

# The program also defines a list of input data containing dictionaries representing various animals of different species.
# The program creates an instance of the "Animal" class for each animal in the input data and adds it to the "animals" dictionary.

# Overall, this program demonstrates how to create and use Python classes, dictionaries, and lists to manage data for a zoo.
# It can be extended or modified to include additional features, such as searching or filtering animals by various attributes.




import datetime

class Animal:
    def __init__(self, species, name, age, birth_season, color, gender, weight, origin):
        self.species = species
        self.name = name
        self.age = age
        self.birth_season = birth_season
        self.color = color
        self.gender = gender
        self.weight = weight
        self.origin = origin
        self.arrival_date = datetime.date.today()

        self.generate_id()

    def generate_id(self):
        if self.species == "hyena":
            prefix = "Hy"
        elif self.species == "lion":
            prefix = "Li"
        elif self.species == "tiger":
            prefix = "Ti"
        elif self.species == "bear":
            prefix = "Be"
        else:
            prefix = "Un"

        id_num = len(animals[self.species]) + 1
        self.id = f"{prefix}{id_num:02d}"

    def get_birth_date(self):
        if self.birth_season == "spring":
            birth_month = 3
        elif self.birth_season == "fall":
            birth_month = 9
        elif self.birth_season == "winter":
            birth_month = 12
        else:
            birth_month = 6

        birth_year = datetime.date.today().year - self.age
        return datetime.date(birth_year, birth_month, 21)

    def __str__(self):
        birth_date = self.get_birth_date().strftime("%Y-%m-%d")
        arrival_date = self.arrival_date.strftime("%Y-%m-%d")
        return f"{self.id}; {self.name}; {self.age} years old; birth date {birth_date}; {self.color} color; {self.gender}; {self.weight} pounds; from {self.origin}; arrived {arrival_date}"

# Define animals list with empty dictionaries for each species
animals = {
    "hyena": [],
    "lion": [],
    "tiger": [],
    "bear": [],
}

# Define input data
input_data = [
    {"species": "hyena", "name": "4 year old female hyena", "age": 4, "birth_season": "spring", "color": "tan", "gender": "female", "weight": 70, "origin": "Friguia Park, Tunisia"},
    {"species": "hyena", "name": "12 year old male hyena", "age": 12, "birth_season": "fall", "color": "brown", "gender": "male", "weight": 150, "origin": "Friguia Park, Tunisia"},
    {"species": "hyena", "name": "4 year old male hyena", "age": 4, "birth_season": "spring", "color": "black", "gender": "male", "weight": 120, "origin": "Friguia Park, Tunisia"},
    {"species": "hyena", "name": "8 year old female hyena", "age": 8, "birth_season": "unknown", "color": "black and tan striped", "gender": "female", "weight": 105, "origin": "Friguia Park, Tunisia"},
    {"species": "lion", "name": "6 year old female lion", "age": 6, "birth_season": "spring", "color": "tan", "gender": "female", "weight": 300, "origin": "Zanzibar, Tanzania"},
    {"species": "lion", "name": "12 year old female lion", "age": 12, "birth_season": "fall", "color": "golden", "gender": "female", "weight": 400, "origin": "Serengeti National Park, Tanzania"},
    {"species": "lion", "name": "4 year old male lion", "age": 4, "birth_season": "summer", "color": "tan", "gender": "male", "weight": 200, "origin": "Kruger National Park, South Africa"},
    {"species": "tiger", "name": "8 year old female tiger", "age": 8, "birth_season": "winter", "color": "orange and black striped", "gender": "female", "weight": 250, "origin": "Bandhavgarh National Park, India"},
    {"species": "tiger", "name": "10 year old male tiger", "age": 10, "birth_season": "spring", "color": "white with black stripes", "gender": "male", "weight": 350, "origin": "Sariska Tiger Reserve, India"},
    {"species": "tiger", "name": "6 year old female tiger", "age": 6, "birth_season": "summer", "color": "orange and black striped", "gender": "female", "weight": 200, "origin": "Bandhavgarh National Park, India"},
    {"species": "bear", "name": "9 year old male bear", "age": 9, "birth_season": "spring", "color": "brown", "gender": "male", "weight": 500, "origin": "Yellowstone National Park, USA"},
    {"species": "bear", "name": "7 year old female bear", "age": 7, "birth_season": "fall", "color": "black", "gender": "female", "weight": 350, "origin": "Yosemite National Park, USA"},
    {"species": "bear", "name": "5 year old male bear", "age": 5, "birth_season": "summer", "color": "blonde", "gender": "male", "weight": 400, "origin": "Banff National Park, Canada"},
]

# Create animal objects and add them to the corresponding species list.
for data in input_data:
  animal = Animal(data["species"], data["name"], data["age"], data["birth_season"], data["color"], data["gender"], data["weight"], data["origin"])
  animals[data["species"]].append(animal)

# print out the animals in each species
for species, animal_list in animals.items():
  print(f"{species.capitalize()}s:")
  for animal in animal_list:
    print(animal)
    print()





