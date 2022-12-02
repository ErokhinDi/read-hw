import os
import operator


def finder():
    files_lines = dict()
    names = os.listdir(os.getcwd())

    for name in names:
        fullname = os.path.join(os.getcwd(), name)
        if os.path.isfile(fullname) and fullname.endswith('.txt') and not fullname.endswith('result.txt'):
            print(fullname)
            with open(fullname, 'r', encoding='utf-8') as f:
                files_lines[fullname] = len(f.readlines())
    return dict(sorted(files_lines.items(), key=operator.itemgetter(1)))


def result_printer(files):
    with open('result.txt', 'w', encoding='utf-8') as f:
        for file in files:
            f.write(file[file.rfind("\\") + 1:] + '\n' + str(files[file]) + '\n')
            with open(file, 'r', encoding='utf-8') as current_file:
                for line in current_file:
                    f.write(line)
            f.write('\n')


result_printer(finder())
