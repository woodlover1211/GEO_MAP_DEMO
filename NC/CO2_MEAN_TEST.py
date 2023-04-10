import numpy as np
import netCDF4 as nc
import h5py
import matplotlib as mpl
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
# CO2_mon_2020.nc
file_path = 'CO2_mean_2020.nc'
data_set = nc.Dataset(file_path)
co2 = data_set.variables['CO2'][:]
h5_data = h5py.File('co2_lon_lat.h5', 'r')
lon = h5_data['lon'][:]
lat = h5_data['lat'][:]
# lat = -lat
# 创建图形对象（画布） 指定画布大小
fig = plt.figure(num='CO2', figsize=(4, 4), dpi=200)
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
geo_axes.set_title('CO2_mean_2020')
bounds = np.arange(380, 450, 10)
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





