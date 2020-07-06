exp="8(6)"
if '(' in exp:
    exp=exp.replace('(','*')
    print(exp)
if ')' in exp:
    exp=exp.replace(')','')
    print(exp)
print(exp)
