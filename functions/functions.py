def family_sorter(fellas_list, length):
    families = []

    for fella in fellas_list:
        if length >= 1000:
            print("bruh, too many, i don`t care")
            return "system32 deleted successfully"

        for family in families:
            if fella[0] in family:
                family.add(fella[1])
                break

            elif fella[1] in family:
                family.add(fella[0])
                break

        else:
            families.append({fella[0], fella[1]})

    return families


def duplicates(males_in_tribes, females_in_tribes):
    return (male * female for male, female in zip(males_in_tribes, females_in_tribes))


def males_in_family(tribe):
    return len({male_count for male_count in tribe if male_count % 2})


def females_in_family(tribes):
    return len({female_count for female_count in tribes if not female_count % 2})
