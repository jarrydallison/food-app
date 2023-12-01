createPortionTable = '''
  CREATE TABLE IF NOT EXISTS portion (
          id INT PRIMARY KEY,
          fdc_id INT,
          seq_num INT,
          amount REAL,
          measure_unit_id INT,
          portion_description VARCHAR(10),
          modifier VARCHAR(50),
          gram_weight REAL,
          data_points INT,
          footnote VARCHAR(40),
          min_year_acquired DATE
  );
'''

portionCSV = 'food_portion.csv'

portionInsertTable = "INSERT INTO portion VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

portionTable = [createPortionTable, portionCSV, portionInsertTable]