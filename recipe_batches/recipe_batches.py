#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):

  if recipe.keys() == ingredients.keys():

    batch_size= []

    for i, j in zip(recipe.values(), ingredients.values()):
      batch_size.append(j//i)
      return min(batch_size)

  else:
    return 0
    

if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))










"""
  def recipe_batches(recipe, ingredients):
    results = [0] * len(recipe.values())
    diff = set(recipe.keys()) - set(ingredients.keys())
    for d in diff:
        ingredients[d] = 0
    ingredients_values = list(ingredients.values())
    recipe_values = list(recipe.values())
    for i in range(len(results)):
        results[i] = int(ingredients_values[i] / recipe_values[i])
    if min(results) < 1:
        return 0
    return min(results)
"""
