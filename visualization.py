# visualization.py
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

def visualize_performance(historical_stats):
    if not historical_stats:
        print("No historical data available for visualization.")
        return

    scores = [h["score"] for h in historical_stats]
    attempts = list(range(1, len(historical_stats) + 1))

    # Create a scatter plot
    plt.figure(figsize=(10, 6))
    plt.plot(attempts, scores, marker='o', label='Scores Over Time')

    # Fit a regression line
    X = np.array(attempts).reshape(-1, 1)
    y = np.array(scores)
    model = LinearRegression()
    model.fit(X, y)
    predicted_scores = model.predict(X)

    plt.plot(attempts, predicted_scores, linestyle='--', color='red', label='Trendline')

    # Highlight key performance points
    plt.scatter([attempts[np.argmax(scores)]], [max(scores)], color='green', label='Best Score', zorder=5)
    plt.scatter([attempts[np.argmin(scores)]], [min(scores)], color='orange', label='Lowest Score', zorder=5)

    plt.title('Quiz Performance Over Time')
    plt.xlabel('Attempt Number')
    plt.ylabel('Score')
    plt.legend()
    plt.grid(True)
    plt.savefig('performance_plot.png')
    plt.close()
