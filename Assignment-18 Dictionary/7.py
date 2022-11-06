fruits = {
    "apple" : [20, 15],
    "orange" : [10, 12]
    }

veggies = {
    "cucumber" : [30, 20],
    "cabbage" : [40, 15]
    }

streetFood = {
    "Burger" : [50, 100],
    "Pizza" : [500, 700]
}

eatable = {**fruits, **veggies, **streetFood}
print(eatable)