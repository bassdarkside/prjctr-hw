import string
import random

path = "git_repo/hw-10/"
alpha = string.ascii_uppercase
rand_range = 100


def files_gen(alph, path, rand_range):
    int_list = random.sample(range(rand_range), len(alph))
    with open(f"{path}summary.txt", "w") as summary:
        for i, letter in enumerate(alph):
            file_name = f"{letter}.txt"
            random_num = str(int_list[i])
            with open(f"{path}{file_name}", "w") as file:
                file.write(random_num)
                summary.write(f"{file_name}: {random_num} ")
    print(f"Creating {len(alph)} txt files and summary.txt is done!")


files_gen(alpha, path, rand_range)
