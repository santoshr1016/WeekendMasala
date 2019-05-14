def passing_cars(cars):
    size = len(cars)
    count = 0
    seen = dict()
    for idx in range(size):
        seen[idx] = len([i for i in cars[idx+1:] if i > 0])
    for idx in range(size):
        if not cars[idx]:
            count += seen[idx]
    return count

cars = [0, 1, 0, 1, 1]
print(passing_cars(cars))
