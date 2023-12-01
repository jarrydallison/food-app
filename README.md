# food-app
A tool for viewing FDA food data

# How to start
1. Set up a venv environment
2. Start the venv with . .venv/bin/activate
3. Navigate into this directory
4. sqlite3 food.db
5. Run whatever queries you wish

# To Create the databases
1. First, delete the food.db file
2. Then, run ./generation_scripts/generate_tables.py
3. Start the sqlite3 server
4. Example query: select * from food group by food_category_id limit 10;