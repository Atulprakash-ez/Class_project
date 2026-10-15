# Student Performance Predictor & Risk Analyzer

A command-line Python program that takes a student's past test scores, attendance and assignment submission rate, then prints a performance report with a predicted next score and a risk level.

## Requirements

- Python 3.8 or newer
- No third-party libraries (standard library only)
- A terminal (no GUI needed)

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/{github-username}/{repo-name}.git
   cd {repo-name}
   ```
2. Check Python is installed:
   ```
   python --version
   ```
   (Use `python3` instead of `python` if that is how it is installed on your system.)
3. Optional: create a virtual environment.
   ```
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```
4. Dependencies: none to install. No configuration files or environment variables are needed.

## Run

```
python student_performance.py
```

## Inputs

The program asks for, in order:

1. Number of past scores (2 to 20)
2. Each score (0 to 100)
3. Attendance percentage (0 to 100)
4. Assignments submitted percentage (0 to 100)

If a value is out of range, the program asks again. Enter numbers only.

## Sample session

```
=== Student Performance Predictor & Risk Analyzer ===
How many past scores? (2-20): 4
Score 1 (0-100): 60
Score 2 (0-100): 65
Score 3 (0-100): 70
Score 4 (0-100): 75
Attendance % : 90
Assignments submitted % : 80
```

The output is a report with the scores, average, highest/lowest, trend per test, predicted next score with its category, risk score and level, and recommendations.

## How it works

- **Average**: mean of all scores.
- **Trend**: average change between consecutive tests.
- **Prediction**: last score plus the trend, clamped to 0-100.
- **Category**: Excellent (85+), Good (70+), Average (50+), otherwise At Risk.
- **Risk score**: `0.4*(100-attendance) + 0.4*(100-average) + 0.2*(100-assignments)`
- **Risk level**: LOW (< 25), MEDIUM (< 50), HIGH (50 or more).
- **Recommendations**: rule-based tips based on attendance, average, assignments and trend.

## Files

- `student_performance.py` - the full program
- `README.md` - this file
