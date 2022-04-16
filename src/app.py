from flask import Flask, jsonify, request
import json
app=Flask(__name__)


todos = [
    { "label": "My first task", "done": False }
]


@app.route('/todos', methods=['GET'])
def hello_world():
    json_text=jsonify(todos)
    return json_text
    
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    decoded_object = json.loads(request.data)
    todos.append(decoded_object)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)   #'Response for the POST todo'


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    todos.pop(position)
    
    return jsonify(todos)  #'something'



# Estas dos líneas siempre seben estar al final de tu archivo app.py.

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)