""" we have given list of cars,
find the count of cars and store it in dictionary  """

cars=["audi","audi","audi","bmw","bmw","scorpio"]
car_count={}
for car in cars:
    if car not in car_count:
        car_count.update({car:1})
    else:
        car_count.update({car:car_count[car]+1})
print(car_count)