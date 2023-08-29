import random
import csv

players = [["Josh", 0], ["Luke", 0], ["Kate", 0], ["Mark", 0], ["Mary", 0]]
score = "hw-10/score_csv/score.csv"


def create_csv(players: list, number_rounds: int) -> str:
    with open(score, "w") as file:
        writer = csv.writer(file)
        writer.writerow(["Player name", "Score"])
        writer = csv.writer(file)
        for _ in range(number_rounds):
            for player in players:
                player[1] += random.randint(1, 15)
            for name in players:
                writer.writerow(name)
    print("File 'score.csv' was created.")


create_csv(players, number_rounds=100)
