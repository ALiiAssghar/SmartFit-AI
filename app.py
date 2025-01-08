from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

workout_plans = {
    "beginner": ["Walking", "Light Yoga", "Basic Stretching", "Bodyweight Squats"],
    "intermediate": ["Push-ups", "Pull-ups", "Lunges", "Cycling"],
    "advanced": ["Deadlifts", "Bench Press", "Sprint Intervals", "Advanced Pilates"]
}

@app.route('/recommend', methods=['POST'])
def recommend_workout():
    try:
        data = request.json
        level = data.get('level', '').lower()

        if level not in workout_plans:
            return jsonify({"error": "Invalid fitness level provided."}), 400

        recommended_plan = workout_plans[level]
        return jsonify({"level": level, "workout_plan": recommended_plan})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
