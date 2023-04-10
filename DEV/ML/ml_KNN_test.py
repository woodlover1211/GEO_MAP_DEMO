# 导入画图工具
import matplotlib.pyplot as plt
# 导入数组工具
import numpy as np
# 导入数据集生成器
from sklearn.datasets import make_blobs
# 导入KNN 分类器
from sklearn.neighbors import KNeighborsClassifier

# 生成样本数为500，分类数为5的数据集
data = make_blobs(n_samples=500, n_features=2, centers=5, cluster_std=1.0, random_state=8)
X, Y = data
# 将生成的数据集进行可视化
plt.scatter(X[:, 0], X[:, 1], s=80, c=Y, cmap=plt.cm.spring, edgecolors='k')
# plt.show()
clf = KNeighborsClassifier()
clf.fit(X, Y)
# 绘制图形
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
# 此处的 yy 并不是输出，而是 X 的另一列，即另一个属性值
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
# meshgrid 从坐标向量中返回坐标矩阵
xx, yy = np.meshgrid(np.arange(x_min, x_max, .02), np.arange(y_min, y_max, .02))
z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
z = z.reshape(xx.shape)
plt.pcolormesh(xx, yy, z, cmap=plt.cm.Pastel1)
# 散点图
# S 大小，c颜色 cmap散点颜色方案 edgecolors 散点的边缘线
plt.scatter(X[:, 0], X[:, 1], s=80, c=Y, cmap=plt.cm.spring, edgecolors='k')
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title("Classifier:KNN")
# 把待分类的数据点用五星表示出来
plt.scatter(0, 5, marker='*', c='red', s=200)
# 对待分类的数据点的分类进行判断
res = clf.predict([[0, 5]])
plt.text(0.2, 4.6, 'Classification flag: ' + str(res))
plt.text(3.75, -13, 'Model accuracy: {:.2f}'.format(clf.score(X, Y)))
plt.show()