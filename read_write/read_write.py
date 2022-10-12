def read_graph(file_name, families):
    with open(file_name, "r", encoding='utf-8') as file:
        test_len = 1
        for line in file:
            if test_len == 1:
                for line in file:
                    a, b = line.split(" ")
                    a = int(a)
                    b = int(b)
                    families.append((a, b))
                return families


def read_len_of_graph(file_name):
    with open(file_name, "r", encoding='utf-8') as file:
        test_len = 1
        for line in file:
            if test_len == 1:
                a = (line.split(" "))
                a = int(a[0])
                return a


def write_file(result):
    f = open("wedding.out", "w+")
    f.write(str(result))
    f.close()
