# This script will generate an error due to too many files open.
files = []
for i in range(10000):
#     files.append(open('some_file.txt', 'r'))
    f = open('some_file.txt', 'r')
    f.close()
    files.append(f)
    print(i)
