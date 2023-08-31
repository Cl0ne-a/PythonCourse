class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"name {self.name} age {self.age}"

    def say_hi(self, sound):
        return f"{self.name} makes sound {sound}"
