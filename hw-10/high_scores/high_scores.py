import csv

score = "hw-10/score_csv/score.csv"
hi_scores = "hw-10/high_scores/high_scores.csv"


def create_csv(score, hi_scores):
    with open(score, "r") as file, open(hi_scores, "w") as hi_file:
        csv_reader = csv.reader(file)
        lines = list(csv_reader)
        top_scopes = sorted(lines[-5:], key=lambda top: top[1], reverse=True)
        writer = csv.writer(hi_file)
        writer.writerow(["Player name", "Highest score"])
        writer.writerows(top_scopes)
    print("File 'high_scores.csv' was created.")


create_csv(score, hi_scores)
