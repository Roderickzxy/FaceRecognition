from numpy import *

A = mat([[1,2,3,4,5,],[2,3,4,5,6,],[3,4,5,6,7,],[4,5,6,7,8,],[5,6,7,8,9,]])
print ("del(A):",linalg.det(A))

print(linalg.inv(A))

B=[8,1,6]
normA = linalg.norm(B)
print(normA)

vector1 = mat([1,2,3,4])
vector2 = mat([4,7,5,5])
# 欧式距离（L2范式）
print(sqrt((vector1-vector2)*((vector1-vector2).T)))

# 哈曼顿距离（L1范式）
print(sum(abs(vector1-vector2)))

# 切比雪夫距离（L∞范式）
print(abs(vector1-vector2).max())

#cos(θ)
print(dot(vector1,vector2)/(linalg.norm(vector1)*linalg.norm(vector2)))
