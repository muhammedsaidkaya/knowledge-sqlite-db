import sqlite3

class RepositoryLayer():

  def __init__(self, filename):
    self.conn = sqlite3.connect(filename)
    self.conn.execute("PRAGMA foreign_keys = 1")
    self.cur=self.conn.cursor()

  def write_query(self, query):
    self.cur.execute(query)
    self.conn.commit()

  def read_query(self, query):
    return self.cur.execute(query)

  def create_tables(self):
    self.write_query('''CREATE TABLE IF NOT EXISTS PERSON
    (ID INTEGER PRIMARY KEY,
    Name  TEXT    NOT NULL,
    Circle       TEXT)''')      

    self.write_query('''CREATE TABLE IF NOT EXISTS TECHNOLOGYSTACK
    (ID INTEGER PRIMARY KEY,
    Name  TEXT    NOT NULL)''') 

    self.write_query('''CREATE TABLE IF NOT EXISTS TECHNOLOGY
    (ID INTEGER PRIMARY KEY,
    Name  TEXT    NOT NULL,
    Ts_id INT,
    FOREIGN KEY (Ts_id) REFERENCES TECHNOLOGYSTACK (ID))''')

    self.write_query('''CREATE TABLE IF NOT EXISTS KNOWLEDGE
    (ID INTEGER PRIMARY KEY,
    P_id INT,
    T_id  INT,
    FOREIGN KEY (P_id) REFERENCES PERSON (ID),
    FOREIGN KEY (T_id) REFERENCES TECHNOLOGY (ID))''') 

  def insert_data(self, objects):
    if len(objects) > 0:
      query = self.__cretate_insert_query(objects)
      query = self.__patch_insert_query_values(query, objects)
      self.write_query(query)
      
  def __cretate_insert_query(self, objects):
    columns = objects[0].get_column_names()
    clazz_name = type(objects[0]).__name__.upper()
    query = "INSERT INTO {}(".format(clazz_name)
    for i in range(len(columns)):
      query += " {}".format(columns[i])
      query += "" if (i+1) == len(columns) else ","
    query += ") "
    return query
  
  def __patch_insert_query_values(self, query, objects):
    query += "VALUES "
    for i in range(len(objects)):
      query += "({})".format(str(objects[i]))
      query += "" if (i+1) == len(objects) else ","
    return query