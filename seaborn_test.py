import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np

titanic = sn.load_dataset('titanic')
# print(titanic.sample(10))  # 随机的10行数据
# sn.barplot(x='class', y='survived', data=titanic)

tips = sn.load_dataset('tips', cache=True)
# print(tips.sample(10))
# # 自动根据参数选择分类显示
# # kind='line' 默认scatter
# # hue：第三个变量的颜色显示
# sn.relplot(x='total_bill', y='tip', data=tips, hue='day', col='time', row='sex')

# 功能性核磁共振成像
fmri = sn.load_dataset('fmri', cache=True)
# # 根据hue=event绘制不同颜色
# # 根据col=region个数，绘制指定个数的图
# # 根据style='event' 设置线条样式
# sn.relplot(kind='line', x='timepoint', y='signal', data=fmri, hue='event', col='region', style='event')
# print(fmri.sample(10))

# 分类散点图catplot 默认kind='strip'
# sn.catplot(x='day', y='total_bill', data=tips, hue='sex', kind='swarm')

# 统计平均数
# sn.catplot(x='day', y='total_bill', data=tips, kind='bar')

# 统计男女获救比例
# sn.catplot(x='sex', y='survived', data=titanic, kind='bar')

# 统计男女获救人数
# sn.barplot(x='sex', y='survived', data=titanic, estimator=lambda values: sum(values))

# 统计单一变量出现次数
# sn.catplot(x='sex', data=titanic, kind='count')

# 直方图-统计单一变量分布
# kde=核密度， bins=直方图数量，rug=胡须
# sn.set(color_codes=True)
# titanic = titanic[~np.isnan(titanic['age'])]
# sn.displot(titanic['age'], kde=True, bins=30, rug=True)

# 多变量分布图：两个变量之间的分布关系
# kind=reg 回归绘图和核密度曲线
# sn.jointplot(x='total_bill', y='tip', data=tips, kind='reg')

# 成对绘图：一次性绘制数据集中若干个字段之间的关系图
# iris = sn.load_dataset('iris', cache=True)
# print(iris.sample(10))
# penguins = sn.load_dataset('penguins')
# print(penguins.sample(10))
# sn.pairplot(penguins)
# plt.show()
