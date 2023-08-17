from jsonschema import validate

class GET:
    def __init__(self, db):
        self.db = db
    def route(self):
        return '/task/get'
    def method(self):
        return 'GET'
    def call(self):
        query = """SELECT * FROM `tasks`;"""
        try: 
            with self.db.cnx() as cnx:
                with cnx.cursor() as cursor:
                    print("query: ", query)
                    cursor.execute(query)
                    tasks = []
                    for (id, task, completed) in cursor:
                        tasks_item = {}
                        tasks_item['id'] = id
                        tasks_item['task'] = task
                        tasks_item['completed'] = completed == 1
                        tasks.append(tasks_item)
            return {
                'data': tasks,
                'error': None
            }
        except Exception as e:
            print("Exception: ", e)
            return {
                'data': None,
                'error': e
            }
        
class ADD:
    def __init__(self, db):
        self.db = db
        self.schema = {
            "type": "object",
            "properties": {
                "task": {"type": "string"},
            },
            "required": ["task"],
        }
    def route(self):
        return '/task/add'
    def method(self):
        return 'POST'
    def get_input(self, instance) -> str:
        validate(instance=instance, schema=self.schema)
        return instance['task']
    def call(self, input):
        query_view = """SELECT `id` FROM `tasks` ORDER BY `id` DESC;"""
        query_add = """INSERT INTO `tasks` (`id`, `task`, `completed`) VALUES (%s, %s, %s);"""
        try:             
            with self.db.cnx() as cnx:
                with cnx.cursor() as cursor:
                    cursor.execute(query_view)
                    ids = []
                    for (id,) in cursor:
                        ids.append(id)
                    max_id = max(ids) if len(ids) > 0 else 0
                    cursor.execute(query_add, (max_id + 1, input, 0))
                    cnx.commit()
                    print("query: ", query_add)
            return {
                'data': True,
                'error': None
            }
        except Exception as e:
            print("Exception: ", e)
            return {
                'data': False,
                'error': e
            }
        
class EDIT:
    def __init__(self, db):
        self.db = db
        self.schema = {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "number"},
                    "completed": {"type": "boolean"},
                    "deleted": {"type": "boolean"}
                },
                "required": ["id", "completed", "deleted"]
            }
        }
    def route(self):
        return '/task/edit'
    def method(self):
        return 'PUT'
    def get_input(self, instance):
        validate(instance=instance, schema=self.schema)
        return instance
    def call(self, input):
        query_update = """UPDATE `tasks` SET `completed` = %s WHERE `id` = %s;"""
        query_delete = """DELETE FROM `tasks` WHERE `id` = %s;"""
        try: 
            with self.db.cnx() as cnx:
                with cnx.cursor() as cursor:
                    for item in input:
                        if item['deleted']:
                            cursor.execute(query_delete, (item['id'],))
                            cnx.commit()
                            print("query: ", query_delete)
                        else:
                            cursor.execute(query_update, (item['completed'], item['id']))
                            cnx.commit()
                            print("query: ", query_update)
            return {
                'data': True,
                'error': None
            }
        except Exception as e:
            print("Exception: ", e)
            return {
                'data': False,
                'error': e
            }