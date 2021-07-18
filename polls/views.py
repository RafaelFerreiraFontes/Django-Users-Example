import collections
from re import template
from django.http import HttpResponse, response, Http404
from django.shortcuts import render
from bson.json_util import dumps,loads
from pymongo import client_options
import mongoUltis


# Create your views here.
def index(request):

    db, client = mongoUltis.get_db().users, mongoUltis.get_db()

    collection = db.Users

    rst = loads( dumps( list( collection.find({}) ) ) )

    client.close()

    print(rst)

    return render(request, 'polls/index.html', { 'users' : rst})


def detail(request):
    try:
        db, client = mongoUltis.get_db().users, mongoUltis.get_db()

        collection = db.Users

        users = loads( dumps( list( collection.find({}) ) ) )

        client.close()
    
    except:
        raise Http404("Users does not Exist")

    return render(request, 'polls/detail.html', { 'users' : users })


def results(request):
    return HttpResponse(f"You're looking at the results question")


def vote(request):
    return HttpResponse(f"You're voting on question")
