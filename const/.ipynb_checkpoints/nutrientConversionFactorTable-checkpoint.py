# This helps convert fdc_id to the calorie conversion
createNutrientConversionFactorTable = '''
  CREATE TABLE IF NOT EXISTS nutrient_conversion_factor (
          id INT PRIMARY KEY,
          fdc_id
  );
'''

nutrientConversionFactorCSV = 'food_nutrient_conversion_factor.csv'

nutrientConversionFactorInsertTable = "INSERT INTO nutrient_conversion_factor VALUES (?, ?)"

nutrientConversionFactorTable = [
  createNutrientConversionFactorTable,
  nutrientConversionFactorCSV,
  nutrientConversionFactorInsertTable
]