import numpy as np
import netCDF4 as nc
import h5py
import matplotlib as mpl
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import scipy.io as scio
from random import random
from matplotlib import colors

dataFile = 'files/month_12_origin.mat' #写入mat文件的位置和名称用/隔开
data = scio.loadmat(dataFile) #data为对应文件的字典
x = data['X']  # 经度
# 只选择第一行所有列的数据 7201
x = x[1, :]
y = data['Y']  # 纬度
# 第一列的所有行 3601
y = y[:, 1]
lon =[]
lat =[]
not_nan = ~np.isnan(z)
index_array = np.argwhere(not_nan)
for index in index_array:
    # print(index)
    (row, col) = index
    lon.append(x[col])
    lat.append(y[row])
z = z[not_nan]
# 创建图形对象（画布） 指定画布大小
fig = plt.figure(num='month_12_original', figsize=(4, 4), dpi=200)
# 创建绘图区域(通过投影方式指定为地理坐标轴)
# geo_axes = plt.axes(projection=ccrs.PlateCarree())  # 全球图像的中央位于太平洋180度经线处
geo_axes = fig.add_subplot(projection=ccrs.PlateCarree())
# 添加经纬度坐标
x_extent = [-120, -60, 0, 60, 120]  # 东西经
y_extent = [-60, -30, 0, 30, 60]  # 南北纬
geo_axes.set_xticks(x_extent, crs=ccrs.PlateCarree())
geo_axes.set_yticks(y_extent, crs=ccrs.PlateCarree())
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)
# 格式化经纬度刻度标签
lon_formatter = LongitudeFormatter()
lat_formatter = LatitudeFormatter()
geo_axes.xaxis.set_major_formatter(lon_formatter)  # x轴表示经线刻度（东经-西经）
geo_axes.yaxis.set_major_formatter(lat_formatter)  # y轴表示纬线刻度（南纬-北纬）
# 添加海岸线 指定线宽 分辨率
geo_axes.coastlines(lw=0.5, resolution='10m')
geo_axes.set_global()
# 添加网格  dotted
gl = geo_axes.gridlines(linestyle=':', color='k', linewidth=0.5)
# 设置刻度朝向和颜色
geo_axes.tick_params(direction='in')
# 添加标题
geo_axes.set_title('month_12_original')
# 处理数据，
z=z[(~np.isnan(z))]
z*=100000
# print(min(z))
# print(max(z))
# 设置的数据范围的最小值和最大值
norm = colors.Normalize(vmin=0.1, vmax=0.5)
# 将色彩c中的数值，对应到色图cmap中
plt.scatter(lon, lat, c=z, s=2, norm=norm, cmap='jet')
cb = plt.colorbar(orientation='horizontal', shrink=0.6, extend='both')
cb.ax.tick_params(labelsize=5)
cb.set_label(label='10^(-5)', loc='right', fontsize=5)
plt.show()
