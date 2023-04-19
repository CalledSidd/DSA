# [14,28,20,40,32,64]
def n_nums(f, n):
    print(f)
    first = True
    for i in range(n):
        if first:
                f = f * 2
                first = False
        else:
                f = f-8
                first = True
        print(f)


num_li = [14,28,20,40,32,64]
f = 14
n_nums(f, 10)