#!/usr/bin/python3
import urllib, requests, bs4

url = 'https://old.reddit.com/r/formula1/'

dic = {'Fri': 'Friday', 'Sat': 'Saturday', 'Sun': 'Sunday'}

def removeNewLine(string):
   return string.replace('\n', '')

def removeWeirdChar(string):
    r = []
    for i in range(0, 3):
        r += string[i]
    r += ':'
    for i in range(7, len(string)):
        r += string[i]

    return "".join(r)

def printEvent(string):
    limit = 16
    print(string, end = ':')
    print(' '.center(limit - len(string)), end = '')

def printDay(string):
    print(dic[string[:3]], end = ', ')
    print(string[8:13])

def remove1stChar(string):
    r = []
    for i in range(1, len(string)):
        r += string[i]

    return "".join(r)

def select1stLine(string):
    r = []
    for i in range(len(string)):
        if string[i] != '\n':
            r += string[i]
        else:
            break;

    return "".join(r)

def printDriver(driver, bool, pos):
    s = '#' + str(pos)
    if bool:
        print(' '.center(28), end = ''), print(s.center(21, ' '), end = '\n')
        print(' '.center(28), end = ''), print('_'.center(21, '_'), end = '\n')
    else:
        print(' '.center(2), end = ''), print(s.center(21, ' '), end = '\n')
        print(' '.center(2), end = ''), print('_'.center(21, '_'), end = '\n')

    for j in range(1, len(driver)):
        if j == 1:
            if bool:
                print(' '.center(28), end = '|'), print(remove1stChar(driver[j].getText()).center(19), end = '|\n')
            else:
                print(' '.center(2), end = '|'), print(remove1stChar(driver[j].getText()).center(19), end = '|\n')
        else:
            if bool:
                print(' '.center(28), end = '|'), print(driver[j].getText().center(19), end = '|\n')
            else:
                print(' '.center(2), end = '|'), print(driver[j].getText().center(19), end = '|\n')

def printFinishLine(bool):
    for i in range(50):
        if bool:
            bool = False
            print("#", end = '')
        else:
            bool = True
            print(" ", end = '')
    print()


page = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/91.0.2'})
infile = urllib.request.urlopen(page).read()
data = infile.decode('ISO-8859-1')
soup = bs4.BeautifulSoup(data, "html.parser")

print('| FORMULA 1 |'.center(86, '='), end = '\n\n')

elems = soup.findAll("li")
elems2 = elems[65].findAll("li")
elems3 = soup.findAll("tbody")
drivers = elems3[2].findAll("tr")
teams = elems3[3].findAll("tr")

print('CONSTRUCTORS TABLE'.center(50, '-'))
print('-'.center(50, '-'), end = '\n')
print('|', end='')
print('TEAM'.center(30), end='|')
print('POINTS'.center(17), end='|\n')
print('-'.center(50, '-'), end = '\n')

for i in range(len(teams)):
    team = teams[i].findAll('td')
    print('|', end='')
    for j in range(1, len(team)):
        if j == 1:
            print(remove1stChar(team[j].getText().center(31)), end='|')
        else:
            print(team[j].getText().center(17), end='|\n')
    print('-'.center(50, '-'), end = '\n')
print()

print('DRIVERS TABLE'.center(50, '-'))
print()
printFinishLine(True)
printFinishLine(False)
print()
for i in range(len(drivers)):
    driver = drivers[i].findAll('td')
    if i % 2 == 0:
        bool = False
    else:
        bool = True
    printDriver(driver, bool, i + 1)

print('\n')
print(select1stLine(elems[65].getText()).center(50, '-'))
print('LOCAL:'.ljust(16), end = ' ')
print(elems2[0].getText())
print('COUNTDOWN:'.ljust(16), end = ' ')
print(elems2[1].getText())

elems2 = elems[69].findAll("tr")
print()
for i in range(1, len(elems2)):
    elems3 = elems2[i].findAll("td")
    for j in range(len(elems3)):
        if j == 0:
            printEvent(elems3[j].getText())
        else:
            printDay(elems3[j].getText())

print()
print('| FORMULA 1 |'.center(86, '='), end = '\n\n')
