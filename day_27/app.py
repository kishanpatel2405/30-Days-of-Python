#
# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
#
#
# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))
#
# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)
#
# app = Flask(__name__)
# if __name__ == '__main__':
#     # for deployment we use to environ
#     # to make it work for both production and development
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)
#
#
