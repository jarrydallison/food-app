createFoodTable = '''
  CREATE TABLE IF NOT EXISTS food (
          fdc_id INT PRIMARY KEY,
          data_type VARCHAR(30),
          description VARCHAR(40),
          food_category_id INT,
          publication_date DATE
  );
'''

foodCSV = 'food.csv'

foodInsertTable = "INSERT INTO food VALUES (?, ?, ?, ?, ?)"

foodTable = [createFoodTable, foodCSV, foodInsertTable]