import data
from service_layer import ServiceLayer

test = ServiceLayer()
# test.insert_data(data.people)
# test.insert_data(data.technology_stack_values)
# test.insert_data(data.technologies)
# test.insert_data(data.knowledges)

print(test.run_select_query("""
SELECT DISTINCT Name FROM PERSON
INNER JOIN ( 
    SELECT k.P_id FROM KNOWLEDGE as k
    INNER JOIN TECHNOLOGY
    WHERE TECHNOLOGY.Name = 'Packer'
    ) as temp
ON PERSON.ID = temp.P_id
"""))