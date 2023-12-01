# use fdc_id to get nutrient conversion factor, then search this table for results
createCalorieConversionFactorTable = '''
  CREATE TABLE IF NOT EXISTS calorie_conversion_factor (
      food_nutrient_conversion_factor_id INT PRIMARY KEY,
      protein_value REAL,
      fat_value REAL,
      carbohydrate_value REAL
  );
'''

calorieConversionFactorCSV = 'food_calorie_conversion_factor.csv'

calorieConversionFactorInsertTable = "INSERT INTO calorie_conversion_factor VALUES (?, ?, ?, ?)"

calorieConversionFactorTable = [
  createCalorieConversionFactorTable,
  calorieConversionFactorCSV,
  calorieConversionFactorInsertTable
  ]