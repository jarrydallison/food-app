# Author: Jarryd Allison
# Date: 11/22/2023
# Description: Generic function for generating a database

import sqlite3
import csv

database = 'food.db'
csvDirectory = 'FoodData_Central_foundation_food_csv_2023-10-26'

# Function to read data from the supplied CSV filename
def readCSV(file):
  with open(file) as f:
    reader = csv.reader(f)
    data = list(reader)
  return data

def generateDB(createTable: str, csvFileName: str, insertTable: str):
  # Create the initial database connection
  conn = sqlite3.connect(database)
  # Create a cursor object
  c = conn.cursor()

  # Create the database
  c.execute(createTable)

  # Fill the database
  data = readCSV(csvDirectory+"/"+csvFileName)
  count = 0
  for row in data:
    # Omit the table headers from each CSV
    if (count > 0):
      c.execute(insertTable, row)
    count += 1
  # Commit the changes
  conn.commit()
  conn.close()

