# data_processor.py
import json
from collections import defaultdict

# Step 1: Load JSON data from local files
def load_json_data(current_file_path, historical_file_path):
    try:
        with open(current_file_path, 'r') as current_file:
            current_data = json.load(current_file)
        
        with open(historical_file_path, 'r') as historical_file:
            historical_data = json.load(historical_file)

        return current_data, historical_data
    except FileNotFoundError:
        print("Error: One or both files are missing.")
        return None, None

# Step 2: Analyze the Data
def analyze_performance(current_data, historical_data):
    current_stats = {
        "score": current_data.get("score", 0),
        "accuracy": float(current_data.get("accuracy", "0 %").strip(" %")) / 100,
        "correct_answers": current_data.get("correct_answers", 0),
        "incorrect_answers": current_data.get("incorrect_answers", 0),
        "total_questions": current_data.get("quiz", {}).get("questions_count", 0),
        "topics": current_data.get("topics", {}),
        "response_map": current_data.get("response_map", {})
    }

    historical_stats = []
    for quiz in historical_data:
        historical_stats.append({
            "score": quiz.get("score", 0),
            "accuracy": float(quiz.get("accuracy", "0 %").strip(" %")) / 100,
            "correct_answers": quiz.get("correct_answers", 0),
            "incorrect_answers": quiz.get("incorrect_answers", 0),
            "topics": quiz.get("topics", {}),
            "response_map": quiz.get("response_map", {})
        })

    return current_stats, historical_stats
