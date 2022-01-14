import pyperclip,re

def principal_period(s):
    i = (s+s).find(s, 1, -1)
    return None if i == -1 else s[:i]

info = open('password.txt')
passwordRegex = re.compile("^((?=.*[a-z])(?=.*[A-Z])(?=.*\d))(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{10,}$")
num_lines = sum(1 for line in open('password.txt'))
strong = 0
weak = 0
for i in range(num_lines):
    text = info.readline()
    password = passwordRegex.search(text)
    if password != None:
        strong = strong + 1
        print(password.group(),"Strong")
    else:
        weak = weak + 1
        print(text.strip(), "Weak")
print("Out of ", num_lines," passwords ", strong, " are strong and ", weak, " are too weak")
