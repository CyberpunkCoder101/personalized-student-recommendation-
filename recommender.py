# recommender.py

def create_recommendations(insights):
    recommendations = []

    if insights["trend"] == "Needs Improvement":
        recommendations.append("Practice more quizzes on similar topics.")

    recommendations.append(insights["weak_areas"])

    topic_focus = [
        topic for topic, stats in insights["topic_performance"].items()
        if stats["accuracy"] < 70
    ]

    if topic_focus:
        recommendations.append("Focus on these weak topics: {}.".format(", ".join(topic_focus)))

    common_mistakes = insights.get("common_mistakes", {})
    if common_mistakes:
        recommendations.append("Review these frequently incorrect questions: {}.".format(", ".join(common_mistakes.keys())))

    return recommendations
