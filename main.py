from flask import Flask, jsonify, request, Response
from models.students import Student
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)


@app.route('/addStudent', methods=['POST'])
def add_student():
    data = request.get_json()
    name = data.get('name')
    group = data.get('group')
    year = data.get('year')
    vals = "('{}', '{}', '{}')".format(name, group, year)
    student = Student.insert('"name", "group", "year"', vals)
    try:
        return jsonify(result='OK')
    except:
        return jsonify(result='fail')


@app.route('/getById', methods=['GET'])
def getById():
    stud_id = request.args.get('id')
    try:
        stuff = Student.get_by_attrs(cols=('id', 'name', '"group"', 'year'), attr_cols=('id'), attr_values=(stud_id))
        return jsonify(stuff)
    except:
        return jsonify(result='bad')


@app.route('/getAll', methods=['GET'])
def getAll():
    try:
        stuff = Student.get_all()
        return jsonify(stuff)
    except:
        return jsonify(result='bad')


@app.route('/remove', methods=['DELETE'])
def remove():
    post_data = request.get_json()
    try:
        Student.delete_by_attrs(post_data.get('id'))
        return jsonify(result='good')
    except:
        return jsonify(result='bad')


if __name__ == '__main__':
    app.run(debug=True)
