import argparse

from numpy import delete, array, ones


def find_par(x):
    n, m = len(x), len(x[1])
    s = ones(n, int)
    for i in range(n):
        if s[i]:
            for j in range(n):
                if i != j:
                    if s[j] and all([x[j][k] >= x[i][k] for k in range(m)]) and any(
                            [x[j][k] > x[i][k] for k in range(m)]):
                        s[j] = 0
    return array([x[i] for i in range(n) if s[i]])


def find_sleiter(x):
    n, m = len(x), len(x[1])
    s = ones(n, int)
    for i in range(n):
        if s[i]:
            for j in range(n):
                if i != j:
                    if s[j] and all([x[j][k] > x[i][k] for k in range(m)]):
                        s[j] = 0
    return array([x[i] for i in range(n) if s[i]])


def find_majority(x):
    n, m = len(x), len(x[1])
    s = ones(n, int)
    for i in range(n):
        if s[i]:
            for j in range(n):
                if i != j:
                    if s[j]:
                        p, w = 0, 0
                        for k in range(m):
                            if x[j][k] > x[i][k]:
                                p += 1
                            if x[i][k] > x[j][k]:
                                w += 1
                        if p > w:
                            s[j] = 0
                        if w > p:
                            s[i] = 0
    return array([x[i] for i in range(n) if s[i]])


def find_lex(x, indexes):
    n, m = len(x), len(x[1])
    s = ones(n, int)
    slices = []
    for i in range(n):
        tmp = [x[i][j - 1] for j in indexes]
        slices.append(tmp)
    for i in range(n):
        if s[i]:
            for j in range(n):
                if i != j and s[j]:
                    q = 0
                    for k in range(m):
                        if slices[i][k] != slices[j][k]:
                            q = k
                            break
                    if slices[i][q] < slices[j][q]:
                        s[j] = 0
                    else:
                        s[i] = 0
    return array([x[i] for i in range(n) if s[i]])


def read_x(file_name):
    with open(file_name, encoding='UTF-8') as file:
        x = file.read().split('\n')
        for i in range(len(x)):
            x[i] = array([int(j) for j in x[i].split()])
        return array(x)


file_name = input('входной файл ')
method = int(input('метод(1: Паретто, 2: Слейтера, 3: лексикографический, 4: мажоритарный) '))
ind = input('Введите номера критериев в порядке их важности ') if method == 3 else []

ind = [int(i) for i in ind.split()] if ind else []

if method not in range(1, 5):
    print('Некоректный метод')
    exit(-1)

x = read_x(file_name)

answer = find_par(x) if method == 1 else find_sleiter(x) if method == 2 else \
        find_lex(x, ind) if method == 3 else find_majority(x) if method == 4 else []

for i in answer:
    print(*i, sep=' ')
