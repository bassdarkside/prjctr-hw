# Time complexity O(n^2)
def loop(cats):
    all_cats = [True] * (cats + 1)
    for i in range(2, cats + 1):
        for j in range(i, cats + 1, i):
            all_cats[j] = not all_cats[j]
    return [
        cat_index for cat_index in range(1, cats + 1) if all_cats[cat_index]
    ]


cats_with_hats = loop(100)
print(cats_with_hats)
