motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# motorcycles[0] = 'ducati'
# print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

print('!!! Part Two !!!')

motorcycles_two = []
motorcycles_two.append('honda')
motorcycles_two.append('yamaha')
motorcycles_two.append('suzuki')
motorcycles_two.insert(0, 'ducati')

print(motorcycles_two)

del motorcycles_two[1]

print(motorcycles_two)

print('!!! Part Three !!!')

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print(f"The last motorcycle I owned was a {popped_motorcycle.title()}")

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}")

motorcycles.append('BMW')
too_expensize = 'BMW'
motorcycles.remove(too_expensize)
print(motorcycles)
print(f"\nA {too_expensize.upper()} is too expensive for me.")