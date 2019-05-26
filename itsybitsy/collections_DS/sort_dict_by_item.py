from operator import itemgetter


rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

rows_by_uid = sorted(rows, key=itemgetter('uid'))
rows_by_fname = sorted(rows, key=itemgetter('fname'))
print(rows_by_uid)
print(rows_by_fname)

'''
# This solution often works just fine. However, the solution involving itemgetter()
# typically runs a bit faster. Thus, you might prefer it if performance is a concern.

rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'],r['fname']))
'''
