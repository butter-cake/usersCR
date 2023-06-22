from flask_app.config.mysqlconnection import connectToMySQL

class User:
    DB = "mydb"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM user;"
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def add_user(cls, data):
        query = """
        INSERT INTO user (first_name, last_name, email) 
        VALUES (%(first_name)s, %(last_name)s, %(email)s);
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results

    @classmethod
    def delete(cls, user_id):
        query = "DELETE FROM user WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query, {'id': user_id})


    @classmethod
    def get_user(cls, user_id):
        query = "SELECT * FROM user WHERE id = %(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, {'id': user_id})
        if result:
            return cls(result[0])
        return None

    @classmethod
    def update(cls, data):
        query = """
        UPDATE user
        SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW()
        WHERE id = %(id)s;
        """
        return connectToMySQL(cls.DB).query_db(query, data)
