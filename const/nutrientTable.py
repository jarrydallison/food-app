createNutrientTable = '''
  CREATE TABLE IF NOT EXISTS nutrient (
          id INT PRIMARY KEY,
          fdc_id INT,
          nutrient_id INT,
          amount REAL,
          data_points INT,
          derivation_id INT,
          min INT,
          max INT,
          median INT,
          footnote VARCHAR(40),
          min_year_acquired DATE
  );
'''

nutrientCSV = 'food_nutrient.csv'

nutrientInsertTable = "INSERT INTO nutrient VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

nutrientTable = [createNutrientTable, nutrientCSV, nutrientInsertTable]