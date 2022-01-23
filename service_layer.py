from repository_layer import *

class ServiceLayer():

  def __init__(self):
    self.db = RepositoryLayer("stack.db")
    self.db.create_tables()

  def insert_data(self, objects):
    self.db.insert_data(objects)

  def run_select_query(self, query):
    return list(self.db.read_query(query))