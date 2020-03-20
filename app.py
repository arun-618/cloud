# Flask, mongodb, configparser, logging, pymongo

from flask import Flask, jsonify, request
from configparser import ConfigParser
from flask_pymongo import PyMongo
from pymongo import MongoClient
from mongoengine import *
import logging
from marshmallow import Schema, fields, post_load, validates, validate

app = Flask(__name__)

app = Flask(__name__)

parser = ConfigParser()
parser.read('dev.ini')

password = parser.get('settings', 'pwd')
user = parser.get('settings', 'username')

client = MongoClient(
    "mongodb+srv://%s:%s@cluster0-uyety.mongodb.net/test?retryWrites=true&w=majority" % (user, password))
db = client.get_database('student_db')
mongo = db.framework

logging.basicConfig(filename='test.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(module)s')


@app.route('/framework', methods=['GET'])
def get_all_frameworks():
    framework = mongo.db.framework

    output = []

    for q in db.framework.find():
        output.append({'name': q['name'], 'language': q['language']})
    list(framework.find())

    mongo.find()

    return jsonify({'result': output})


@app.route('/framework/<name>', methods=['GET'])
def get_one_framework(name):
    framework = mongo.db.framework

    q = db.framework.find_one({'name': name})

    if q:
        output = {'name': q['name'], 'language': q['language']}
    else:
        output = 'No results found'

    return jsonify({'result': output})


@app.route('/framework', methods=['POST'])
def add_framework():
    framework = mongo.db.framework

    name = request.json['name']
    language = request.json['language']

    a = validator(name, language)

    framework_id = db.framework.insert({'name': name, 'language': language})
    new_framework = db.framework.find_one({'_id': framework_id})

    output = {'name': new_framework['name'], 'language': new_framework['language']}

    return jsonify({'result': output})


def validator(name, language):
    a = {'name': name, 'language': language}
    schema = PersonSchema()
    person = schema.load(a)
    res = schema.dump(person)
    return res


class PersonSchema(Schema):
    name = fields.String(validate=validate.Length(max=20))
    language = fields.String(validate=validate.Length(max=20))


@app.route('/delete/<name>', methods=['DELETE'])
def delete_framework(name):
    framework = mongo.db.framework

    q = db.framework.delete_one({'name': name})
    print(q)

    response = jsonify("Framework named {} is Deleted Successfully".format(name))
    response.status_code = 200
    return response


@app.route('/update/<name>', methods=['PUT'])
def update_framework(name):
    name1 = request.json['name']
    language = request.json['language']
    a = validator(name1, language)
    print(a)

    framework = mongo.db.framework

    db.framework.update_one({'name': name},
                            {'$set': {'name': name1, 'language': language}})
    response = jsonify("Framework updated successfully")
    response.status_code = 200
    return response


if __name__ == '__main__':
    app.run(debug=True)
