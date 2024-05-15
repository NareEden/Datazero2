# Method showing the table columns
  def table_columns(self):
    cur = self.conn.cursor()
    # Execute the query to fetch column names
    cur.execute(f"DESCRIBE {'WeatherForecast'};")

    # Fetch all rows (column descriptions)
    columns = cur.fetchall()

    # Extract and print column names
    column_names = [column[0] for column in columns]
    print(f"Columns in table '{'WeatherForecast'}':")
    for column_name in column_names:
      print(column_name)\
# Method showing the tables
  def show_tables(self):
    cursor = self.conn.cursor()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()

    # Print the tables
    print("Tables in your_database:")
    for table in tables:
      print(table[0])
