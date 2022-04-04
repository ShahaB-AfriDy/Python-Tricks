def Digital_Root(Numbers):
	# SUM = str(sum(map(int,Numbers)))
	SUM = str(sum([int(u) for u in Numbers]))
	return Digital_Root(SUM) if len(SUM) > 1 else SUM

print(Digital_Root('12345972'))
