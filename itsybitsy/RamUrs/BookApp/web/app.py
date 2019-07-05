from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient


app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.aNewDB
UserNum = db["UserNum"]

UserNum.insert({
    'number_of_user': 0
})


class Visit(Resource):
    def get(self):
        prev_num = UserNum.find({})[0]['number_of_user']
        new_num = prev_num + 1
        UserNum.update({}, {"$set": {"number_of_user": new_num}})
        return str("Hello") + str(new_num)


def check_validity_of_posted_data(pd, fn):
    if fn == "add" or fn == "sub" or fn == "mul":
        if "x" not in pd and "y" not in pd:
            return 301
        else:
            return 200
    elif fn == "div":
        if "x" not in pd and "y" not in pd:
            return 301
        elif int(pd["y"]) == 0:
            return 302
        else:
            return 200


# Define resource , The class is our resource
class Add(Resource):
    def post(self):
        # If I am here, The resource is was requested using POST

        # STEP 1 GET Posted data
        posted_data = request.get_json()
        st_code = check_validity_of_posted_data(posted_data, "add")

        if st_code != 200:
            ret_json = {
                "Message": "An error happened",
                "Status code": st_code
            }
            return ret_json

        num1 = int(posted_data["x"])    # Make sure they are int
        num2 = int(posted_data["y"])

        # STEP 2 Operate on the data
        result = num1 + num2

        # Step 3 Prepare the return json
        ret_dict = {
            "Message": result,
            "Status Code": 200
        }

        # Step 4 Return the json
        return jsonify(ret_dict)

    def get(self):
        # If I am here, The resource is was requested using GET
        pass

    def put(self):
        # If I am here, The resource is was requested using PUT
        pass

    def delete(self):
        # If I am here, The resource is was requested using DELETE
        pass


class Subtract(Resource):
    def post(self):
        # If I am here, The resource is was requested using POST

        # STEP 1 GET Posted data
        posted_data = request.get_json()
        st_code = check_validity_of_posted_data(posted_data, "sub")

        if st_code != 200:
            ret_json = {
                "Message": "An error happened",
                "Status code": st_code
            }
            return ret_json

        num1 = int(posted_data["x"])    # Make sure they are int
        num2 = int(posted_data["y"])

        # STEP 2 Operate on the data
        result = num1 - num2

        # Step 3 Prepare the return json
        ret_dict = {
            "Message": result,
            "Status Code": 200
        }

        # Step 4 Return the json
        return jsonify(ret_dict)


class Divide(Resource):
    def post(self):
        # If I am here, The resource is was requested using POST

        # STEP 1 GET Posted data
        posted_data = request.get_json()
        st_code = check_validity_of_posted_data(posted_data, "div")

        if st_code != 200:
            ret_json = {
                "Message": "An error happened",
                "Status code": st_code
            }
            return ret_json

        num1 = int(posted_data["x"])    # Make sure they are int
        num2 = int(posted_data["y"])

        # STEP 2 Operate on the data
        result = num1 / num2

        # Step 3 Prepare the return json
        ret_dict = {
            "Message": result,
            "Status Code": 200
        }

        # Step 4 Return the json
        return jsonify(ret_dict)


class Multiply(Resource):
    def post(self):
        # If I am here, The resource is was requested using POST

        # STEP 1 GET Posted data
        posted_data = request.get_json()
        st_code = check_validity_of_posted_data(posted_data, "mul")

        if st_code != 200:
            ret_json = {
                "Message": "An error happened",
                "Status code": st_code
            }
            return ret_json

        num1 = int(posted_data["x"])    # Make sure they are int
        num2 = int(posted_data["y"])

        # STEP 2 Operate on the data
        result = num1 * num2

        # Step 3 Prepare the return json
        ret_dict = {
            "Message": result,
            "Status Code": 200
        }

        # Step 4 Return the json
        return jsonify(ret_dict)


api.add_resource(Add, '/api/v1/books')
api.add_resource(Subtract, '/sub')
api.add_resource(Multiply, '/mul')
api.add_resource(Divide, '/div')
api.add_resource(Visit, '/hello')


@app.route("/")
def hello_world():
    return "Welcome to Bookstore App"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

