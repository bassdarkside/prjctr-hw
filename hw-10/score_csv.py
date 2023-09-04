import random
import csv

players = [["Josh", 0], ["Luke", 0], ["Kate", 0], ["Mark", 0], ["Mary", 0]]
path = "git_repo/hw-10/"


def create_scores_csv(path, players, number_rounds):
    with open(f"{path}score.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["Player name", "Score"])
        for _ in range(number_rounds):
            for player in players:
                player[1] = random.randint(1, 1000)
            for name in players:
                writer.writerow(name)


create_scores_csv(path, players, number_rounds=100)
