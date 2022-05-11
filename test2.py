def pluralize(l):
    set_plural = set()
    set_singular = set()
    final_set = set()

    for elem in l:
        if l.count(elem) > 1:
            set_plural.add(elem)
        else:
            set_singular.add(elem)

    for elem in set_plural:
        elem = elem + 's'
        final_set.add(elem)

    final_set = final_set.union(set_singular)

    return final_set



result = pluralize(["cow", "pig", "cow", "cow", 'me', 'me', 'he'])
# l = ["cow", "pig", "cow", "cow", 'me', 'he']

print(result)