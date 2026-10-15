def read_number(prompt, low, high):
    while True:
        value = float(input(prompt))
        if low <= value <= high:
            return value
        print(f"Enter a value between {low} and {high}.")


def get_marks():
    marks = []
    n = int(read_number("How many past scores? (2-20): ", 2, 20))
    for i in range(n):
        marks.append(read_number(f"Score {i+1} (0-100): ", 0, 100))
    return marks


def average(marks):
    total = 0
    for m in marks:
        total += m
    return total / len(marks)


def average_change(marks):
    total = 0
    for i in range(1, len(marks)):
        total += marks[i] - marks[i - 1]
    return total / (len(marks) - 1)


def predict_next(marks):
    p = marks[-1] + average_change(marks)
    if p > 100:
        p = 100
    elif p < 0:
        p = 0
    return p


def classify(score):
    if score >= 85:
        return "Excellent"
    elif score >= 70:
        return "Good"
    elif score >= 50:
        return "Average"
    return "At Risk"


def risk_score(att, avg, asg):
    return 0.4 * (100 - att) + 0.4 * (100 - avg) + 0.2 * (100 - asg)


def risk_level(score):
    if score < 25:
        return "LOW"
    elif score < 50:
        return "MEDIUM"
    return "HIGH"


def recommendations(att, avg, asg, trend):
    tips = []
    if att < 75:
        tips.append("Attendance is below 75%. Attend more classes.")
    if avg < 60:
        tips.append("Average is low. Revise weak topics.")
    if asg < 70:
        tips.append("Submit assignments on time.")
    if trend < 0:
        tips.append("Scores are declining. Find out why.")
    if not tips:
        tips.append("Keep up the consistent performance.")
    return tips


def main():
    print("=== Student Performance Predictor & Risk Analyzer ===")
    marks = get_marks()
    att = read_number("Attendance % : ", 0, 100)
    asg = read_number("Assignments submitted % : ", 0, 100)

    avg = average(marks)
    trend = average_change(marks)
    pred = predict_next(marks)
    score = risk_score(att, avg, asg)

    print("\n------ REPORT ------")
    print("Scores        :", marks)
    print(f"Average       : {avg:.2f}")
    print(f"High / Low    : {max(marks)} / {min(marks)}")
    print(f"Trend         : {trend:+.2f} per test")
    print(f"Predicted next: {pred:.2f} ({classify(pred)})")
    print(f"Risk          : {score:.2f} -> {risk_level(score)}")
    print("\nRecommendations:")
    for t in recommendations(att, avg, asg, trend):
        print(" -", t)


main()
