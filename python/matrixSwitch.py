class Demo:
	def demo(self, list1, list2):
		tmp_list = list1
		for i in zip(range(len(list1))):
			for j in range(len(list1[0])):
				# list2[i][j] = list1[j][i]
				list1[j][i] = tmp_list[i][j]

		return list2

	def demo1(self, list1):
		new_list = list(map(list, zip(*list1)))
		return new_list


list1 = [[7, 0, 0, 0, 0],
		 [3, 8, 0, 0, 0],
		 [8, 1, 0, 0, 0],
		 [2, 7, 4, 4, 0],
		 [4, 5, 2, 6, 5],
		 [1, 2, 3, 4, 5]]
# list1 = [[7, 0, 0, 0, 0],
# 		 [3, 8, 0, 0, 0],
# 		 [8, 1, 0, 0, 0],
# 		 [2, 7, 4, 4, 0],
# 		 [4, 5, 2, 6, 5]]


how = Demo()

# list2 = zip(*list1)

# list3 = list(map(list, list2))
# print(list3)

for i in range(len(list1)):
	print(list1[i])
print("=" * 30)

new_list = how.demo1(list1)

# print(new_list)

for i in range(len(new_list)):
	print(new_list[i])
# print("=" * 30)

# new_list2 = [[0 for i in range(len(list1))] for i in range(len(list1[0]))]
# how.demo(list1, new_list2)

# for i in range(len(list1)):
# 	print(list1[i])

# for i in range(len(new_list2)):
# 	print(new_list2[i])

