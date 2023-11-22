#!/usr/bin/env python3
# Author: Jarryd Allison
# Date: 11/22/2023
# Description: Python script to create databases from FDA csvs

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

# Create the initial database connection
conn = sqlite3.connect(database)

# Create a cursor object
c = conn.cursor()

# Create the base food database
c.execute('''
  DROP TABLE IF EXISTS food;
''')

c.execute('''
  CREATE TABLE IF NOT EXISTS food (
          fdc_id INT PRIMARY KEY,
          data_type VARCHAR(30),
          description VARCHAR(40),
          food_category_id INT,
          publication_date DATE
  );
''')

# Fill the base food database
foodRows = readCSV(csvDirectory+'/food.csv')
for row in foodRows:
  # Omit the table headers from the CSV in the database
  if (row[0] != 'fdc_id'):
    c.execute("INSERT INTO food VALUES (?, ?, ?, ?, ?)", row)
# Commit the changes
conn.commit()
conn.close()

# Notes
# Consider a CTE to reduce foods down to something like SELECT * FROM food GROUP BY description