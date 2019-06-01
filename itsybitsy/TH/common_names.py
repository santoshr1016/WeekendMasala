class CommonNames:

    @staticmethod
    def find_common(names1, names2):
        common = set()
        for name in names1:
            common.add(name)
        print(common)
        for name in names2:
            common.add(name)

        return common



names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(CommonNames.find_common(names1, names2)) # should print Ava, Emma, Olivia, Sophia