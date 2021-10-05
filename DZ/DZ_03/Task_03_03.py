def thesaurus(*args):
    dict_names = {}
    for i in range(len(args)):
        val = args[i]
        key = val[0]
        if key not in dict_names:
            dict_names[key] = [val]
        else:
            dict_names[key] = list(filter (lambda x : x[0] == key, args ))

    return dict_names

print (thesaurus ("Иван", "Мария", "Петр", "Илья", "Игнат", "Игорь", "Михаил", "Алексей"))

