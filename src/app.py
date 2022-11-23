from flask import Flask, jsonify, request, json
app = Flask(__name__)

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    detached_code = json.loads(request.data)
    todos.append(detached_code)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if (position > 0):
        todos.pop(position-1)
        return jsonify(todos)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False },
    { "label": "My third task", "done": False }
]

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)