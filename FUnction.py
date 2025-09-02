tom_exp_list = [2100, 3400, 3500]
joe_exp_list = [5600, 4300, 1200]

def total_exp(exp):
    total = 0
    for i in exp:
        total += i
    return  total

print("tom_exp_list total is:", total_exp(tom_exp_list))
print("joe_exp_list total is:", total_exp(joe_exp_list))
