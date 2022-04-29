list_df = ()
for a in range(1, 50):
    for b in range(1, 50):
        if a != b:
            for c in range(1, 50):
                if a != b and a != c and b != c:
                    for d in range(1, 50):
                        if a != b and a != c and a != d and b != c and b != d and c != d:
                            x = (a ** 3 + b ** 3)
                            y = (c ** 3 + d ** 3)
                            if x == y:
                                list_df += x,
#                    print(y)
list_df = set(list_df)
list_df = sorted(list_df)
print(list_df)