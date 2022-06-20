def Digital_Root(Numbers):
	# SUM = str(sum(map(int,str(Numbers))))
	SUM = str(sum([int(u) for u in str(Numbers)]))
	return Digital_Root(SUM) if len(SUM) > 1 else SUM

# print(Digital_Root('12345972'))
# print(Digital_Root(12345972))
