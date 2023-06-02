lst = ['yuval 50 \n', 'dany 30 \n', 'yossi 90 \n']
sorted_list = sorted(lst, key=lambda x: int(x.split()[1]))
print(sorted(lst[0].split())[0])
