import collections
from re import template
from django.http import HttpResponse, response, Http404
from django.shortcuts import render
from bson.json_util import dumps,loads
from bson.objectid import ObjectId
from pymongo import client_options
import mongoUltis


def index(request):

    db, client = mongoUltis.get_db().users, mongoUltis.get_db()

    collection = db.Users

    users = loads( dumps( list( collection.find({}) ) ) )

    client.close()

    for i in range(0, len(users)):
        users[i]['id'] = str(users[i]['_id'])  

    return render(request, 'Users/index.html', { 'users' : users})


def users(request):
    try:
        db, client = mongoUltis.get_db().users, mongoUltis.get_db()

        collection = db.Users

        users = loads( dumps( list( collection.find({}) ) ) )

        client.close()
    
    except:
        raise Http404("Can't load db info")

    return render(request, 'Users/users.html', { 'users' : users })

def user(request, _id):
    try:
        db, client = mongoUltis.get_db().users, mongoUltis.get_db()

        collection = db.Users
        user = loads( dumps( collection.find_one( {'_id' : ObjectId(_id) , } ) ) )

        user['id'] = str(user['_id'])

        client.close()

    except:
        raise Http404("User does not Exist")

    return render(request, 'Users/user.html', { 'user' : user})
