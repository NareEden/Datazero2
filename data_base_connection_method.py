# Data base connection method
def connect_to_database(self):       # okay
    try:
        conn = mariadb.connect(
        user = self.user,
        password = self.password,
        host = self.host,
        database = self.database  # Use the name of your database here
      )
      print("Connected to MariaDB!")
      return conn
    except mariadb.Error as e:
      print(f"Error connecting to MariaDB: {e}")
      return None
