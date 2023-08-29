import string
import random

path = "hw-10/generate_txt/files/"
sum_path = "hw-10/generate_txt/summary.txt"
alpha = string.ascii_uppercase
rand_range = 100


def make_rand_num(data_len, rand_range):
    return random.sample(range(rand_range), data_len)


def file_gen(alphabet, path, sum_path, rand_range):
    int_list = make_rand_num(len(alphabet), rand_range)
    with open(sum_path, "w") as summary:
        for i, letter in enumerate(alphabet):
            file_name = f"{letter}.txt"
            random_num = str(int_list[i])
            with open(f"{path}{file_name}", "w") as file:
                file.write(random_num)
                summary.write(f"{file_name}: {random_num} ")
    print(f"Creating {len(alphabet)} txt files and summary.txt is done!")


file_gen(alpha, path, sum_path, rand_range)
