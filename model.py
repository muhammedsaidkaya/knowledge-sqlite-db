class AbstractEntity():

  def __init__(self, id):
    self.id = id

  def get_variables_dict(cls):
    variables = cls.__dict__
    return { 
        "keys":list(map(lambda key: key.capitalize(), variables.keys())), 
        "values":list(variables.values())
    }

  def get_column_names(cls):
    return cls.get_variables_dict()["keys"]

  def __repr__(self):
    string = ""
    values = self.get_variables_dict()["values"]
    for i in range(len(values)):
      if type(values[i]) is str:
        string += " '{}' ".format(values[i])
      else:
        string += " {} ".format(values[i])
      string += "" if (i+1) == len(values) else ","
    return string

class Person(AbstractEntity):

  def __init__(self, id, name, circle):
    super().__init__(id)
    self.name = name
    self.circle = circle

class TechnologyStack(AbstractEntity):

  def __init__(self, id, name):
    super().__init__(id)
    self.name = name

class Technology(AbstractEntity):

  def __init__(self, id, name, ts_id):
    super().__init__(id)
    self.name = name
    self.ts_id = ts_id

class Knowledge(AbstractEntity):

  def __init__(self, id, p_id, t_id):
    super().__init__(id)
    self.p_id = p_id
    self.t_id = t_id