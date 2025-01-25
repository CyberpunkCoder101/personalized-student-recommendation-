# Quiz Performance Analysis

## Project Overview

The **Quiz Performance Analysis** project is designed to evaluate a student's quiz performance using historical data. The system provides:

- **Performance Insights**: Highlights weak areas, improvement trends, and performance gaps.
- **Actionable Recommendations**: Suggests steps for improvement based on data analysis.
- **Visualization**: Generates a trendline of quiz scores over time.
- **Text Report**: Outputs a detailed summary of insights and recommendations.

## Features

- **Load and Analyze Data**:
  - Reads current and historical quiz data from JSON files.
  - Filters data by quiz ID.
- **Insights**:
  - Analyzes accuracy, topics, and trends to identify strengths and weaknesses.
- **Recommendations**:
  - Provides improvement strategies tailored to the user.
- **Visualization**:
  - Creates a PNG file showing score trends.
- **Text Report**:
  - Outputs insights and recommendations to a `.txt` file.

## Setup Instructions

### Prerequisites

- Python 3.8 or later Download Imported libraries


## Usage

### Running the Script

1. Place your JSON files in the `data/` directory:

   - `current_quiz_data.json`: Contains details of the latest quiz submission.
   - `historical_quiz_data.json`: Contains performance data of past quizzes.

2. Execute the script:

```bash
python main.py
```

### Outputs

- **Performance Report**: A detailed summary saved as `outputs/performance_report_<quiz_id>.txt`.
- **Visualization**: A PNG file saved as `outputs/performance_plot_<quiz_id>.png`.

## Example Data Format

### Current Quiz Data

```json
{
  "id": 336566,
  "score": 32,
  "accuracy": "80 %",
  "correct_answers": 8,
  "incorrect_answers": 2,
  "response_map": {
    "1837": 7363,
    "1848": 7407
  },
  "quiz": {
    "questions_count": 10
  }
}
```

### Historical Quiz Data

```json
[
  {
    "id": 336566,
    "score": 28,
    "accuracy": "70 %",
    "correct_answers": 7,
    "incorrect_answers": 3,
    "response_map": {
      "1837": 7363,
      "1848": 7407
    }
  },
  {
    "id": 336566,
    "score": 35,
    "accuracy": "90 %",
    "correct_answers": 9,
    "incorrect_answers": 1
  }
]
```

## Screenshots

- **Insights Example**:&#x20;

- **Visualization Example**:&#x20;

## Demo Video

A 2-5 minute video demonstrating the functionality is included as `demo_video.mp4` in the repository.

## Approach Description

1. **Load Data**:

   - Use `data_loader.py` to read JSON files containing quiz data.

2. **Analyze Performance**:

   - The `performance_analyzer.py` module extracts insights based on trends, weak areas, and accuracy.

3. **Generate Recommendations**:

   - Provide actionable feedback for improvement using data-driven insights.

4. **Visualization**:

   - Plot score trends using `visualizer.py`.

5. **Text Report**:

   - Summarize insights and recommendations in a user-friendly format with `report_generator.py`.

---

For additional questions or clarifications, feel free to reach out!

