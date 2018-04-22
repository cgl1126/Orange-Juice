"""
	7

	3   8

	8   1   0

	2   7   4   4

	4   5   2   6   5

D(r, j) 表示第i第j列的权值

MaxSum(r, j) 表示从D(r, j)到底边的各条路径中，最佳路径（最大值）的数字之和

1 <= r < n  MaxSum(r, j) = Max(MaxSum(r+1, j), MaxSum(r+1, j+1)) + D(r, j)
r = n       MaxSum(r, j) = D(r, j)

"""

class Demo:
	def demo(self, list1, row, column):
		if row == len(list1) - 1:
			return list1[row][column]
		return max(self.demo(list1, row+1, column), self.demo(list1, row+1, column+1)) + list1[row][column]
	
	def demo1(self, list1, row, column):
		tmp_list = list1[row-1]
		for index1 in range(row-2, -1, -1):
			index = 0
			for value in [values for values in list1[index1] if values != 0]:
				tmp_list[index] = max(tmp_list[index], tmp_list[index+1]) + value
				index += 1 
				print(tmp_list)
		return tmp_list[0]




how = Demo()

list1 = [[7, 0, 0, 0, 0],
		 [3, 8, 0, 0, 0],
		 [8, 1, 0, 0, 0],
		 [2, 7, 4, 4, 0],
		 [4, 5, 2, 6, 5]]

max_sum = how.demo1(list1, 5, 5)
print(max_sum)



# print(list1)
# print(type(list1))
# print(len(list1))
# print(list1[0][0])