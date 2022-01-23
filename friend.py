# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL

# model the class after the friend table from our database
class Friend:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.ocupation = data['ocupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod # Now we use class methods to query our database
    def get_all(cls):
        query = "SELECT * FROM friends;"
        results = connectToMySQL('friend').query_db(query) # make sure to call the connectToMySQL function with the schema you are targeting.
        friends = [] # Create an empty list to append our instances of friends
        for friend in results: # Iterate over the db results and create instances of friends with cls.
            friends.append( cls(friend) )
        return friends

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO friends ( first_name , last_name , ocupation , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(occ)s , NOW() , NOW() );"
        return connectToMySQL('friend').query_db( query, data ) # data is a dictionary that will be passed into the save method from server.py
