# insight_generator.py
from collections import defaultdict

def generate_insights(current_stats, historical_stats):
    insights = {}

    # Topic-Wise Analysis
    topic_performance = defaultdict(lambda: {"correct": 0, "total": 0})

    for quiz in historical_stats:
        for topic, stats in quiz.get("topics", {}).items():
            topic_performance[topic]["correct"] += stats.get("correct", 0)
            topic_performance[topic]["total"] += stats.get("total", 0)

    insights["topic_performance"] = {
        topic: {
            "accuracy": (values["correct"] / values["total"] * 100) if values["total"] > 0 else 0
        }
        for topic, values in topic_performance.items()
    }

    # Creative Labels for Strengths and Weaknesses
    strengths = []
    weaknesses = []
    
    for topic, performance in insights["topic_performance"].items():
        if performance["accuracy"] >= 90:
            strengths.append(f"Outstanding in {topic} with a mastery of {performance['accuracy']:.2f}% accuracy!")
        elif performance["accuracy"] >= 70:
            strengths.append(f"Solid understanding of {topic} with a good accuracy of {performance['accuracy']:.2f}%.")
        else:
            weaknesses.append(f"Needs improvement in {topic} with an accuracy of {performance['accuracy']:.2f}%. Consider revisiting the basics.")

    insights["strengths"] = strengths
    insights["weaknesses"] = weaknesses

    # Weak Areas
    avg_accuracy = sum([h["accuracy"] for h in historical_stats]) / len(historical_stats) if historical_stats else 0
    insights["weak_areas"] = f"Your average accuracy is {avg_accuracy:.2f}. Keep up the consistency!"

    # Improvement Trends
    insights["trend"] = "🚀 You're on an upward trend!" if current_stats["accuracy"] > avg_accuracy else "⚡ Needs a little boost to get back on track."

    # Gaps (Response Map Analysis)
    incorrect_responses = defaultdict(int)
    for quiz in historical_stats:
        for question_id, selected_option in quiz.get("response_map", {}).items():
            if selected_option == "incorrect":
                incorrect_responses[question_id] += 1

    insights["common_mistakes"] = dict(sorted(incorrect_responses.items(), key=lambda x: x[1], reverse=True)[:5])

    return insights
