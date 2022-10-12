from functions.functions import family_sorter
from functions.functions import duplicates
from functions.functions import males_in_family
from functions.functions import females_in_family
from read_write.read_write import read_graph
from read_write.read_write import read_len_of_graph
from read_write.read_write import write_file


def wedding(people_list, len_of_graph):
    print(people_list)

    families = family_sorter(people_list, len_of_graph)

    male_amount_in_each_family = [males_in_family(family) for family in families]

    female_amount_in_each_family = [females_in_family(family) for family in families]
    print(families)
    print(male_amount_in_each_family)
    print(female_amount_in_each_family)

    all_pair = sum(male_amount_in_each_family) * sum(female_amount_in_each_family)

    duplicate_pair = sum(duplicates(male_amount_in_each_family, female_amount_in_each_family))

    write_file(all_pair - duplicate_pair)

    return all_pair - duplicate_pair


if __name__ == '__main__':
    graph = []
    graph = read_graph("in.txt", graph)

    print("How much group: " + str(len(graph)) + " ;")
    res = wedding(graph, read_len_of_graph("in.txt"))
    print(res)