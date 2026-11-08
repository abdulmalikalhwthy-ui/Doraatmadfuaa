from flask import Flask, request, jsonify

app = Flask(__name__)
courses_db = []

@app.route('/add_course', methods=['POST'])
def add_course():
    data = request.json
    course = {
        "id": len(courses_db) + 1,
        "title": data.get('title'),
        "teacher": data.get('teacher'),
        "price": data.get('price'),
        "link": data.get('link')
    }
    courses_db.append(course)
    return jsonify({"status": "success", "message": "Course added successfully"})

@app.route('/get_courses', methods=['GET'])
def get_courses():
    return jsonify(courses_db)

if __name__ == '__main__':
    print("Server is running on port 5000...")
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)