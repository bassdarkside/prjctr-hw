import csv


def create_high_scores_csv(input_file, output_file):
    hi_scores = {}
    with open(input_file, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            player = row[0]
            score = int(row[1])
            if player in hi_scores:
                if score > hi_scores[player]:
                    hi_scores[player] = score
            else:
                hi_scores[player] = score
    sort_hi_scores = sorted(
        hi_scores.items(), key=lambda x: x[1], reverse=True
    )

    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Player name", "Highest score"])
        writer.writerows(sort_hi_scores)


input_file = "git_repo/hw-10/score.csv"
output_file = "git_repo/hw-10/high_scores.csv"

create_high_scores_csv(input_file, output_file)
