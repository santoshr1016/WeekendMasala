from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient


app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.aNewDB
BooksDB = db["Books"]


def check_validity_of_posted_data(pd, fn):
    if fn == "add" or fn == "sub" or fn == "mul":
        if set(pd.keys()) == set("name", "isbn", "authors", "country", "number_of_pages", "publisher", "release_date"):
            return 301
        else:
            return 200
    # elif fn == "div":
    #     if "x" not in pd and "y" not in pd:
    #         return 301
    #     elif int(pd["y"]) == 0:
    #         return 302
    #     else:
    #         return 200

"""
('978-0143125471','The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics','Daniel James Brown','Penguin Books','2014-12-12,3',3,9.49,'Paperback','Canoeing','Sports & Outdoors',3,'bookstore/static/assets/coverimages/12343.png')
,('978-1476764832','The Time Traveler"s Wife','Audrey Niffenegger', 'Scribner','2004-12-12',6, 14.28 , 'Paperback', 'Time Travel', 'Science Fiction',1,'bookstore/static/assets/coverimages/45656.png')
,('978-1400033805','The Closing of the Western Mind: The Rise of Faith and the Fall of Reason','Charles Freeman','Vintage', '2005-12-12', 4,13.32,'Paperback', 'Culture','Religion',1,'bookstore/static/assets/coverimages/45656.png')
,('978-0452299030','The Sign: The Shroud of Turin and the Secret of the Resurrection','Thomas de Wesselow','Plume','2012,10,16',4,12.00,'Hardcover','Christian','History',3,'bookstore/static/assets/coverimages/67878.png')

"""
# Define resource , The class is our resource
class Create(Resource):
    def post(self):
        # If I am here, The resource is was requested using POST

        # STEP 1 GET Posted data
        posted_data = request.get_json()
        # st_code = check_validity_of_posted_data(posted_data, "add")
        #
        # if st_code != 200:
        #     ret_json = {
        #         "Message": "An error happened",
        #         "Status code": st_code
        #     }
        #     return ret_json
        book = posted_data

        BooksDB.insert(book)
        # Step 3 Prepare the return json
        bd = dict()
        bd["book"] = book
        data = list()
        ret_dict = {
            "status_code": 201,
            "status": "success",
            "data": data.append(bd)
            }

        # Step 4 Return the json
        return jsonify(ret_dict)


class Read(Resource):
    def get(self):
        output = []
        for item in BooksDB.find():
            output.append({"name": item["name"], "isbn": item["isbn"], "authors": item["authors"],
                           "number_of_pages": item["number_of_pages"], "publisher": item["publisher"],
                           "country": item["country"], "release_date": item["release_date"]})

        ret_json = {
            "status_code": 200,
            "status": "sucess",
            "data": output,
        }
        return jsonify(output)


class ReadBookById(Resource):
    def get(self, book_id):
        pass


class Update(Resource):
    def post(self, book_id):
        pass


class Delete(Resource):
    def post(self, book_id):
        pass


api.add_resource(Create, '/api/v1/books')
api.add_resource(Read, '/api/v1/books')
api.add_resource(ReadBookById, '/api/v1/books/<int:book_id>')
api.add_resource(Update, '/api/v1/books/<int:book_id>')
api.add_resource(Delete, '/api/v1/books/<int:book_id>')


@app.route("/")
def hello_world():
    return "Welcome to Bookstore App"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

