
from data_processor import load_json_data, analyze_performance
from insights_generator import generate_insights
from recommender import create_recommendations
from visualization import visualize_performance

def define_persona(current_stats, insights):
    if current_stats["accuracy"] >= 0.85:
        return "High Achiever"
    elif current_stats["accuracy"] >= 0.70:
        return "Consistent Performer"
    else:
        return "Needs Focus"

def main(current_file_path, historical_file_path):
    current_data, historical_data = load_json_data(current_file_path, historical_file_path)

    if current_data is None or historical_data is None:
        return

    current_stats, historical_stats = analyze_performance(current_data, historical_data)
    insights = generate_insights(current_stats, historical_stats)
    recommendations = create_recommendations(insights)
    persona = define_persona(current_stats, insights)

    
    visualize_performance(historical_stats)

  
    print("Performance Insights:", insights)
    print("Recommendations:", recommendations)
    print("Student Persona:", persona)
    print("Visualization saved as 'performance_plot.png'")

if __name__ == "__main__":
    current_file_path = "current_quiz_data.json"
    historical_file_path = "historical_quiz_data.json"
    main(current_file_path, historical_file_path)
