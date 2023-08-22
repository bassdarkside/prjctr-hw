def loop(cats):
    cats_on_hats_indices = [True] * (cats + 1)
    count = 2
    result = ()
    while count <= cats:
        for i in range(count, cats + 1, count):
            cats_on_hats_indices[i] = not cats_on_hats_indices[i]
        count += 1
    for cat_index in range(1, cats + 1):
        if cats_on_hats_indices[cat_index]:
            result += (cat_index,)
    return result


cats_with_hats = loop(100)
print(cats_with_hats)
