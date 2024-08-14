import pymongo

# MongoDB URI and client setup
MONGODB_URI = 'mongodb+srv://kishanvaghasiya:kishan.123@30daysofpython.r5ful.mongodb.net/?retryWrites=true&w=majority&appName=30DaysOfPython'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python']
students_collection = db['students']

# Static data to insert
student_list = [
    {
        'name': 'kishan',
        'country': 'Finland',
        'city': 'Helsinki',
        'skills': ['HTML', 'CSS', 'JavaScript', 'Python']
    },
    {
        'name': 'vinesh',
        'country': 'UK',
        'city': 'London',
        'skills': ['Python', 'MongoDB']
    },
    {
        'name': 'zamir',
        'country': 'Sweden',
        'city': 'Stockholm',
        'skills': ['Java', 'C#']
    }
]

# Insert data into MongoDB
try:
    result = students_collection.insert_many(student_list)
    print(f'Data inserted with record ids: {result.inserted_ids}')
except Exception as e:
    print(f'Error inserting data: {e}')
