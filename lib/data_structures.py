spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    names = []
    for name in spicy_foods:
        names.append(name.get('name'))
    return names


def get_spiciest_foods(spicy_foods):
    heat_list = []
    for food in spicy_foods:
        if food['heat_level'] > 5:
            heat_list.append(food)

    return heat_list


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(
            f'{food.get("name")} ({food.get("cuisine")}) | Heat Level: {food.get("heat_level") * "🌶"}')


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    food_by_cuisine = [food
                       for food in spicy_foods if food.get("cuisine").lower() == cuisine.lower()]
    return food_by_cuisine[0]


def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food.get("heat_level") > 5:
            print(
                f'{food.get("name")} ({food.get("cuisine")}) | Heat Level: {food.get("heat_level") * "🌶"}')


def get_average_heat_level(spicy_foods):
    list_heat_level = [food.get("heat_level") for food in spicy_foods]
    return sum(list_heat_level) / len(list_heat_level)


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
