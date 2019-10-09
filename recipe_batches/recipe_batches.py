#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    count = 0
    length = len(recipe)
    while True:
        for key in recipe:
            if key not in ingredients:
                return count // length
            if recipe[key] > ingredients[key]:
                return count // length
            else:
                ingredients[key] = ingredients[key] - recipe[key]
                count += 1


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
