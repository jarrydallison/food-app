#!/usr/bin/env python3
# Author: Jarryd Allison
# Date: 11/22/2023
# Description: Python script to create a database from the food.csv file

from const.foodTable import foodTable
from const.nutrientTable import nutrientTable
from const.portionTable import portionTable
from const.nutrientConversionFactorTable import nutrientConversionFactorTable
from const.calorieConversionFactorTable import calorieConversionFactorTable
from utils.generateDB import generateDB

database = 'food.db'
csvDirectory = 'FoodData_Central_foundation_food_csv_2023-10-26'

tables = [
  foodTable,
  nutrientTable,
  portionTable,
  nutrientConversionFactorTable,
  calorieConversionFactorTable,
]

count = 0 
for row in tables:
  count += 1
  generateDB(row[0], row[1], row[2])
  print(count)

print(count,' tables created!')