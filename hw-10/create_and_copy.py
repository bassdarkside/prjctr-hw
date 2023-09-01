import pathlib

data = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

filename = pathlib.Path("git_repo/hw-10/zen.txt")


def write_read_copy(filename, data):
    try:
        if not filename.exists():
            with open(filename, "w") as file:
                file.write(data)
        with open(filename, "r") as file:
            r_data = file.read()
        with open(f"copy_{filename}", "w") as file:
            file.write(r_data.upper())
    except IOError as e:
        print(e)


write_read_copy(filename, data)
