# 8zxx xxxx - Mobile, Data Services, New Numbers and Prepaid Numbers
# 9yxx xxxx - Mobile, Data Services and Pager (until May 2012)
# x denotes 0 to 9
# y denotes 0 to 8 only
# z denotes 1 to 8 only


min8range = 81000000
max8range = 88000000

min9range = 90000000
max9range = 98000000


eight = []
for i in range(min8range, max8range):
    eight.append(i)
    print("appended")

nine = []
for i in range(min9range, max9range):
    nine.append(i)
    print("appended")

def printnumbers():
    return nine
    return eight

printnumbers()