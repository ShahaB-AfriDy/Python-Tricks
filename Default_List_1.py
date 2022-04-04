def MyList(element,List = None):
	if List  is None:
		List = []
	List.append(element)
	print(List)
	List.pop()

List = [1,2]

MyList(3,List)
MyList(4,List)
MyList(5,List)


#-------------------Return Types---------------
# def MyList(element,List = None):
# 	if List  is None:
# 		List = []
# 	List.append(element)
# 	Store = List.copy()
# 	List.pop()
# 	return Store

# List = [1,2]

# print(MyList(3,List))
# print(MyList(4,List))
# print(MyList(5,List))