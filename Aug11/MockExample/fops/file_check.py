import os


class FileOps(object):
    def __init__(self, dirpath, fname):
        self.dirpath = dirpath
        self.fname = fname

    def check_dir_exists(self):
        return os.path.exists(self.dirpath)

    def check_file_exists(self):
        return os.path.isfile(os.path.join(os.getcwd() + "/" + self.fname))

    def create_file(self):
        if self.check_dir_exists() and not self.check_file_exists():
            new_file_name = os.path.join(self.dirpath, self.fname)
            with open(new_file_name, 'w') as f:
                f.write("tests content, newly added")
                return True

        return False

# dirpath = "/Users/rsantoshkumar/workspace/WeekendMasala/Aug11/MockExample/fops"
# fname = "new_file.txt"
# fops = FileOps(dirpath, fname)
# fops.create_file()
