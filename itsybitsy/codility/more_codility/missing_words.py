def find_missing(main_s, lost_s):
    my_dict = dict()
    result = []
    main_s = main_s.strip().split(' ')
    lost_s = lost_s.strip().split(' ')
    for item in lost_s:
        if item not in my_dict:
            my_dict[item] = 1
    for item in main_s:
        if item not in my_dict:
            result.append(item)
    print(result)
    return result

# main_string = "I am using HackerRank to improve programming"
# lost_string = "am HackerRank to improve"

main_string = "I love programming"
lost_string = "programming"

find_missing(main_string, lost_string)
