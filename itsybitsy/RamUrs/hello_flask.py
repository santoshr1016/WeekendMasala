# from flask import Flask, jsonify, request
#
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():
#     return "Hello World"
#
# @app.route('/add', methods=["POST"])
# def add_numbers():
#     # Structure of Response
#     # 1.  Status, Boss, what happened to the Req, you must tell the user
#     # 2.  Prepare the response which user wants and for that
#     # 2.1 Get the inputs from the the request object (json data)
#     # 2.2 Do some operation to that input
#     # 2.3 Prepare the response in nice json and
#     # 2.4 Send to the user
#
#     # Step 1
#     data_dict = request.get_json()
#     num1 = data_dict["x"]
#     num2 = data_dict["y"]
#
#     # Step 2.2
#     result = num1 + num2
#
#     # Step 2.3
#     ret_json = {
#         "result": result
#     }
#
#     # Step 2.4
#     return jsonify(ret_json), 200
#
#
# @app.route('/hi')
# def hi_function():
#     return "Hello there"
#
# @app.route('/bye')
# def bye():
#     ret_json = {
#         'key1' : "value1",
#         'key2' : "value2"
#     }
#
#     return jsonify(ret_json)
#
# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

usersList = ['Aaron', 'Bianca', 'Cat', 'Danny', 'Elena']


class UsersList(Resource):
    def get(self):
        return {'users': [user for user in usersList]}, 200


class UserById(Resource):
    def get(self, id):
        return {'username': usersList[id]}


class UserByName(Resource):
    def post(self, name):
        usersList.append(name)

        return { 'message': 'New user added'}


api.add_resource(UsersList, '/users')
api.add_resource(UserById, '/users/<int:id>')
api.add_resource(UserByName, '/users/<string:name>')

app.run()
