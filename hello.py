# import sys
# print(f"Hello, I'm Python Version {sys.version}")

from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Konfigurasi MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db_python_tester'

mysql = MySQL(app)

class User(Resource):
    def get(self, user_id=None):
        cursor = mysql.connection.cursor()
        if user_id:
            cursor.execute("SELECT * FROM users WHERE id=%s", (user_id,))
            user = cursor.fetchone()
            if user:
                return jsonify({'id': user[0], 'name': user[1], 'email': user[2]})
            return jsonify({'message': 'User not found'}), 404
        else:
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
            result = []
            for user in users:
                result.append({'id': user[0], 'name': user[1], 'email': user[2]})
            return jsonify(result)

    def post(self):
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        mysql.connection.commit()
        return jsonify({'message': 'User created successfully'})

    def put(self, user_id):
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE users SET name=%s, email=%s WHERE id=%s", (name, email, user_id))
        mysql.connection.commit()
        return jsonify({'message': 'User updated successfully'})

    def delete(self, user_id):
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
        mysql.connection.commit()
        return jsonify({'message': 'User deleted successfully'})

api.add_resource(User, '/users', '/users/<int:user_id>')

if __name__ == '__main__':
    app.run(debug=True)
