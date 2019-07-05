class ReverseString(object):
    def reverse_method_1(self, ss="test"):
        return ss[::-1]

    def reverse_method_2(self, ss="default"):
        ss = list(ss)
        start = 0
        end = len(ss) - 1

        while start <= end:
            ss[start], ss[end] = ss[end], ss[start]
            start += 1
            end -= 1
        return "".join(ss)


