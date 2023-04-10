from sklearn import datasets  # 机器学习库
from sklearn.model_selection import train_test_split  # 从样本中随机的按比例选取train_data和test_data
from sklearn.tree import DecisionTreeClassifier
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
# 设置使中文正常显示
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
# 鸢尾花数据
iris = datasets.load_iris()
iris_data = iris.data  # x(特征值)
iris_target = iris.target  # y（目标值）
# print(iris_data.shape)
# 鸢尾花特征
iris_feature = ['花萼长度', '花萼宽度', '花瓣长度', '花瓣宽度']
# 目标值['setosa','vericolor','virginica'] = ['山鸢尾','变色鸢尾','维吉尼亚鸢尾']
# target_name = iris.target_names.tolist()
# train_data：所要划分的样本特征集
# train_target：所要划分的样本结果
# test_size：样本占比，如果是整数的话就是样本的数量
# random_state：是随机数的种子
# print(target_name)
# 取花萼长度[0]和花瓣长度[2]做为特征，训练决策树模型
# 训练值特征值，测试集特征值，训练集目标值，测试集目标值
# 20%用于测试，80%用于训练
x_train, x_test, y_train, y_test = train_test_split(iris_data[:, [0, 2]], iris_target, test_size=0.2, random_state=0)
# 拟合模型
model = DecisionTreeClassifier(criterion='entropy', min_samples_leaf=3)
model.fit(x_train, y_train)
# 利用样本数据点绘制分类背景
# 随机采样, 生成花萼长度[0]和花瓣长度[2]数据
# 蒙特卡洛思想, 随机模拟大量不同长度下的分类结果, 并作为分类背景
N, M = 500, 500  # 横纵各采样500个值，共250000个数据
# 在已有数据大小范围内生成数据
x1_min, x2_min = x_train.min(axis=0)
x1_max, x2_max = x_train.max(axis=0)
# 根据变量范围, 生成坐标轴
t1 = np.linspace(x1_min, x1_max, N)
t2 = np.linspace(x2_min, x2_max, M)
x1, x2 = np.meshgrid(t1, t2)  # 转换成下x,y坐标形式，生成网格采样点
x_show = np.stack((x1.flatten(), x2.flatten()), axis=1)  # x,y坐标位置分别对应输入两个变量
# 使用拟合模型验证,生成250000个数据的分类结果
y_predict = model.predict(x_show)
# 绘制网格色块背景
fig, ax = plt.subplots(figsize=(6, 4), constrained_layout=True)
# 设定颜色colormap
cm_light = mpl.colors.ListedColormap(['#A0FFA0', '#FFA0A0', '#A0A0FF'])  # 背景图
cm_dark = mpl.colors.ListedColormap(['green', 'red', 'purple'])  # 散点图
# 绘制低饱和度色彩分类背景
ax.pcolormesh(x1, x2, y_predict.reshape(x1.shape), cmap=cm_light)
# 更改坐标范围
ax.set_xlim(x1_min, x1_max)
ax.set_ylim(x2_min, x2_max)
# 绘制散点图
# 设置参数c：设定一组变量用来对应cmap颜色；y_train为分类结果
ax.scatter(x_train[:, 0], x_train[:, 1], c=y_train, cmap=cm_dark, marker='o', edgecolors='k')
# 去除坐标轴边线
ax.spines[['top', 'bottom', 'left', 'right']].set_visible(False)
# 增加坐标轴右侧刻度，并设置粗细
ax.tick_params(labelright=True, labelsize=14)
# 设置x轴标签
ax.set_xlabel('花萼长度', fontsize=15)
ax.set_ylabel('花瓣长度', fontsize=15)
ax.set_title('鸢尾花分类', fontsize=15)
plt.grid(visible=True, axis='both', ls=':')
plt.savefig('Grid_background.jpeg')
plt.show()
