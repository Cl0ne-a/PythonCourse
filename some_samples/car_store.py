from some_samples.car import Car

blue = Car("blue", 20000)

red = Car("red", 30000)

cars = {blue, red}

for car in cars:
    print(f"color {car.color}, mileage {car.mileage}")