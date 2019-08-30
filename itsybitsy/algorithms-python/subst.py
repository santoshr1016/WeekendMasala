def function(s, ss):
    i = 0
    j = 0
    sl = len(s)
    ssl = len(ss)

    while i < sl:
        while j < ssl:
            if s[i] == s[j]:
                i += 1
                j += 1
        if j == ssl:
            print("Found")
        j = 0



function("This is Tokyo", "is is")