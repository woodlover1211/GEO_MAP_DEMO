import numpy as np
import matplotlib.pyplot as plt
import scipy.io as scio
import netCDF4 as nc
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import cmaps
import warnings
warnings.filterwarnings('ignore')


# dataFile = 'files/matlab.mat'  # 写入mat文件的位置和名称用/隔开
# data = scio.loadmat(dataFile)  # data为对应文件的字典
# z = data['Z']  # 通过 字典【‘矩阵名’】的形式读取矩阵
# x = data['X']
# y = data['Y']
# pcolormesh([X,Y],C,kwargs)
# C:此参数包含2D数组中的值为color-mapped的值。
# X, Y:这些参数是四边形角的坐标。
# cmap:此参数是颜色图实例或注册的颜色图名称。
# norm:此参数是Normalize实例，将数据值缩放到规范的颜色图范围[0，1]以映射到颜色
# vmin, vmax:这些参数本质上是可选的，它们是颜色栏范围。
# alpha:此参数是颜色的强度。
# snap:此参数用于将网格捕捉到像素边界。
# edgecolors:此参数是边的颜色。 {‘none’，无，‘face’，颜色，颜色顺序}
# shading:此参数是填充样式。它平整或古拉乌德。
#
# x = np.linspace(-10, 10, 5)  # -10, -5, 0, 5, 10
# y = np.linspace(-1, 5, 4)  # -1, 1, 3, 5
# # print(x)
# # print(y)
# X, Y = np.meshgrid(x, y)  # narray
# # X = np.meshgrid(x)  # list
# # Y = np.meshgrid(y)
# print(X)
# print(Y)
# Z = np.zeros((5, 4))
# for i, val_x in enumerate(x):
#     for j, val_y in enumerate(y):
#         Z[i, j] = np.sin(val_x + val_y)
#
# print(Z.T)
# cm = plt.cm.get_cmap('jet')
# plt.pcolormesh(X, Y, Z.T, cmap=cm)
# plt.show()

ds = nc.Dataset('files/41558_2021_1011_MOESM14_ESM.nc', 'r')
# print(ds.variables.keys())
# 一维数组
lon = ds['lon'][:]
lat = ds['lat'][:]
otd = ds['OTD'][:]
# print(lon)
# print(lat)
# 二维网格数据
lon, lat = np.meshgrid(lon, lat)
# print(lon)  # 某行每列不同
# print(lat)  # 某列每行不同
# print(otd)  # lat*lon 17*37
# 可视化-画布(图形对象)-坐标(绘图区域对象)
fig, ax = plt.subplots(1, 1, figsize=(8, 6), dpi=100, subplot_kw={'projection': ccrs.PlateCarree()})
# 经纬度范围170W,140W,55N,70N
extent = [-170, -140, 55, 70]
# 海岸线
ax.add_feature(cfeature.COASTLINE.with_scale('110m'), linewidth=0.5, zorder=2, color='k')
# 设置经纬度(根据经纬度截取显示范围)
ax.set_extent(extent, crs=ccrs.PlateCarree())
# 设置经纬度坐标
x_extent = np.arange(extent[0], extent[1] + 1, 10)  # 东西经
y_extent = np.arange(extent[-2], extent[-1] + 1, 5)  # 南北纬
ax.set_xticks(x_extent, crs=ccrs.PlateCarree())
ax.set_yticks(y_extent, crs=ccrs.PlateCarree())
# 格式化经纬度 显示N-S-W-E
ax.xaxis.set_major_formatter(LongitudeFormatter())
ax.yaxis.set_major_formatter(LatitudeFormatter())
# 绘图 色图范围[0, 0.15]
cf = plt.pcolormesh(lon, lat, otd, transform=ccrs.PlateCarree(), cmap=cmaps.MPL_BuPu, vmin=0, vmax=0.15)

# 调整子区的展示效果，以画布fig为参考系，子区右边的位置
plt.subplots_adjust(right=0.8)
# 添加color bar
cax = fig.add_axes([0.875, 0.135, 0.02, 0.70])  # 绘图区 轴域对象【left，bottom，width，height】画布中矩形区域的左下角坐标和宽高
# 设置color bar信息
cb = plt.colorbar(cf, cax=cax, shrink=0.60, orientation='vertical', extend='both', ticks=np.arange(0.01, 0.20, 0.02))
cb.ax.set_ylabel('test')
plt.show()


