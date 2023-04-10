import sklearn.datasets as skdata
import matplotlib.pyplot as plt
import sklearn.model_selection as skmodel  # 模型评估
import sklearn.neighbors as skneighbors  # 聚类算法
import sklearn.preprocessing as skprep  # 特征处理
import scipy.io as scio
import seaborn as sbn
import pandas as pd

# 加载数据集
iris_data = skdata.load_iris()
# print(dir(iris_data))
# print(iris_data.DESCR)
# print(iris_data.feature_names)
# print(iris_data.target_names)
# print(iris_data.target)



