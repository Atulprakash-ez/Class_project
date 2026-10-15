# Student Performance Predictor & Risk Analyzer

A command-line Python program. You enter a student's past test scores, attendance and assignment submission rate. It prints a report with the average, the trend, a predicted next score and a risk level, plus some recommendations.

## Requirements

- Python 3.8 or newer
- No third-party libraries (standard library only)
- A terminal (no GUI needed)

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/Atulprakash-ez/Class_project.git
   cd Class_project
   ```
2. Check that Python is installed:
   ```
   python --version
   ```
   (Use `python3` instead of `python` if that is how it is installed on your system.)
3. Optional: create a virtual environment.
   ```
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```
4. Install dependencies. There are none, but this command also works:
   ```
   pip install -r requirements.txt
   ```
5. Configuration: none needed. No environment variables or config files are used.

## Run

```
python main.py
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

------ REPORT ------
Scores        : [60.0, 65.0, 70.0, 75.0]
Average       : 67.50
High / Low    : 75.0 / 60.0
Trend         : +5.00 per test
Predicted next: 80.00 (Good)
Risk          : 21.00 -> LOW

Recommendations:
 - Keep up the consistent performance.
```

## How it works

- **Average:** mean of all scores.
- **Trend:** average change between consecutive tests.
- **Prediction:** last score plus the trend, limited to 0-100.
- **Category:** Excellent (85+), Good (70+), Average (50+), otherwise At Risk.
- **Risk score:** `0.4*(100-attendance) + 0.4*(100-average) + 0.2*(100-assignments)`
- **Risk level:** LOW (below 25), MEDIUM (below 50), HIGH (50 or more).
- **Recommendations:** simple rule-based tips based on attendance, average, assignments and trend.

## Files

- `main.py` - the full program
- `requirements.txt` - dependency list (empty, standard library only)
- `.gitignore` - files Git should ignore
- `README.md` - this file
