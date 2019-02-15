"""
Author: R Santosh
Prob: Convert 12 hour clock to military time
"""


class SolutionProb2(object):

    def get_am_pm(self, sec):
        pos = [i for i, e in enumerate(sec) if e.isalpha()]
        return int(sec[:pos[0]]), sec[pos[0]:]

    def convert_24hr_military(self, input_hour):
        hh, mm, ss = input_hour.split(':')
        ss, period = self.get_am_pm(ss)
        hh = int(hh) % 12

        if period.upper() == 'PM':
            hh = hh + 12

        return str(hh).zfill(2) + ":" + str(mm).zfill(2) + ":" + str(ss).zfill(2)

if __name__ == '__main__':
    solution = SolutionProb2()
    print(solution.convert_24hr_military(input()))
