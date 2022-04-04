print()
List = [1, 2, 3, 4, 2, 3, 3, 1, 4, 3, 4]
print(List)


Common_occur = max(set(List),key=List.count)
print(f'Most Frequently came occur Element: ',Common_occur)
print('Time occur in List: ',List.count(Common_occur))


help(max)