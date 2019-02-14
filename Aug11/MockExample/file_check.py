import os


def check_dir_exists(path):
    return os.path.exists(path)


def check_file_exists(filename):
    full = os.path.join(os.getcwd() + "/" + filename)
    val = os.path.isfile(full)
    return val


def create_file(target_directory, new_file_name):
    if check_dir_exists(target_directory) and not check_file_exists(new_file_name):
        new_file_name = os.path.join(target_directory, new_file_name)
        with open(new_file_name, 'w') as f:
            f.write("tests content, newly added")
            return True

    return False


create_file("/Users/rsantoshkumar/workspace/WeekendMasala/Aug11/MockExample", "new_file.txt")
