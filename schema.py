from apiflask.schemas import Schema
from apiflask import fields

# Schema converts our files to json files

"""
    class Task:
        id int
        content str
        date_added datetime
        is_complete Boolean
"""

class TaskOutputSchema(Schema):                            #Output is for a get method. Asin getting stuff from the db
    id = fields.Integer()
    content = fields.String()
    date_added = fields.DateTime()
    is_completed = fields.Boolean()
    
class TaskCreateSchema(Schema):
    content = fields.String(required=True)
        
class TaskUpdateSchema(Schema):
    content = fields.String(required=True)
    is_completed = fields.Boolean(required=True)