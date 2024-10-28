from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in-memory database
questions_db = [
    {"id": 1, "question": "What is the capital of France?", "options": ["Paris", "Berlin", "Madrid", "Rome"], "answer": "Paris"},
    {"id": 2, "question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"},
]

# GET all questions
@app.route('/questions', methods=['GET'])
def get_questions():
    return jsonify(questions_db), 200

# GET a question by ID
@app.route('/questions/<int:id>', methods=['GET'])
def get_question(id):
    question = next((q for q in questions_db if q["id"] == id), None)
    return jsonify(question) if question else ("Question not found", 404)

# POST a new question
@app.route('/questions', methods=['POST'])
def add_question():
    data = request.get_json()
    new_question = {
        "id": len(questions_db) + 1,
        "question": data["question"],
        "options": data["options"],
        "answer": data["answer"]
    }
    questions_db.append(new_question)
    return jsonify(new_question), 201

# PUT (update) a question
@app.route('/questions/<int:id>', methods=['PUT'])
def update_question(id):
    data = request.get_json()
    question = next((q for q in questions_db if q["id"] == id), None)
    if question:
        question.update(data)
        return jsonify(question), 200
    else:
        return "Question not found", 404

# DELETE a question
@app.route('/questions/<int:id>', methods=['DELETE'])
def delete_question(id):
    global questions_db
    questions_db = [q for q in questions_db if q["id"] != id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
