import numpy as np
import netCDF4 as nc
import h5py
import matplotlib as mpl
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

file_path = 'CO2_SSP119_2015_2150.nc'
data_set = nc.Dataset(file_path)
# print(data_set.variables.keys())
co2_ssp_data = data_set.variables['CO2'][:]
# print(co2_ssp_data.shape)  # (1632, 180, 360) = (month, lat, lon)
# 矩阵转置（360，180） 第61条数据对应2020-01
co2 = co2_ssp_data[20, :, :].T
# print(co2.shape)
lon = np.zeros(co2.shape)
lon_data = data_set.variables['longitude'][:]
# 经度：某一行每一列数值相同(360行，每行重复180列)
for i in range(len(lon_data)):
    lon[i, :] = lon_data[i]
# print(lon)
# print(lon.shape)
lat = np.zeros(co2.shape)
lat_data = data_set.variables['latitude'][:]
# 纬度：某一列每一行数值相同（180列，每列重复360行）
for j in range(len(lat_data)):
    lat[:, j] = lat_data[j]
# print(lat)
# print(lat.shape)
# 写入HDF
h5_data = h5py.File('co2ssp_lon_lat.h5', 'w')
h5_data['lon'] = lon
h5_data['lat'] = lat

# 创建图形对象（画布） 指定画布大小
fig = plt.figure(num='CO2SSP_2020', figsize=(4, 4), dpi=200)
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
geo_axes.set_title('')
bounds = np.arange(400, 416, 1)
# # 填充轮廓线
filled_cf = plt.contourf(lon, lat, co2,
                         extend='both',
                         levels=bounds,
                         cmap=mpl.cm.jet,
                         transform=ccrs.PlateCarree())
color_bar = fig.colorbar(filled_cf, orientation='horizontal', extend='both', shrink=0.7)
color_bar.ax.tick_params(labelsize=4)
# 图像显示
plt.show()

