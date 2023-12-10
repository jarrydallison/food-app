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

# Questions to Answer
10 pts  : Was a video included in the project submission?
5 pts   : Does the project contain at least 3 tables?
5 pts   : Are there relationships between table items (foreign keys)?
5 pts   : Are there constraints on the table columns?
5 pts   : Did the writeup/video show SQL statements (and any accompanying code) for all table creation?
5 pts   : Did the writeup/video show SQL statements for the insertion of data?
5 pts   : Did the writeup/video show SQL statements for UPDATEs?
5 pts   : Did the writeup/video show SQL statements for queries?
5 pts   : Do the tables include Indexes ? 
          (Primary key counts as index if they are data and not just row counters)?
10 pts  : Did the writeup/video show the code and execution of the trigger(s)?
5 pts   : Did the writeup/video show the Join between at least 3 tables?
5 pts   : Did the writeup/video show grouping of the data on the Join between at least 3 tables?
5 pts   : Did the writeup/video show aggregation on the Join between at least 3 tables?
5 pts   : Did the writeup/video show the deletion of items that have foreign keys?