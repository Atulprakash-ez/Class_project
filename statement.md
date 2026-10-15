# Problem Statement

## Student Performance Predictor & Risk Analyzer

Teachers and students often only look at the latest marks. That makes it hard to notice whether a student is improving or slowly falling behind. Attendance and missed assignments also affect results, but they are rarely looked at together with marks.

## Objective

Build a command-line Python program that takes a student's past test scores, attendance and assignment submission rate, and uses them to:

1. Summarise the scores (average, highest, lowest).
2. Work out the trend, meaning how much the scores change from one test to the next.
3. Predict the score on the next test.
4. Calculate a risk score and classify it as LOW, MEDIUM or HIGH.
5. Give simple recommendations on what the student should improve.

## Input

- Number of past scores (2 to 20)
- Each score (0 to 100)
- Attendance percentage (0 to 100)
- Assignments submitted percentage (0 to 100)

Invalid or out-of-range values are rejected and the user is asked again.

## Output

A report showing the scores, average, highest and lowest score, trend per test, predicted next score with its category (Excellent, Good, Average or At Risk), the risk score and level, and a list of recommendations.

## Approach

- Prediction: last score plus the average change between tests, kept within 0-100.
- Risk score: `0.4*(100-attendance) + 0.4*(100-average) + 0.2*(100-assignments)`.
- Risk level: LOW below 25, MEDIUM below 50, HIGH otherwise.
- Recommendations come from simple rules on attendance, average, assignments and trend.

## Constraints

- Runs entirely from the command line.
- Uses only the Python standard library.
