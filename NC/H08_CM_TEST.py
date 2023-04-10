import netCDF4 as nc
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cf
import matplotlib as mpl
import numpy as np
import h5py
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

# lon_data = data_set.variables['lon'][:]
# lat_data = data_set.variables['lat'][:]
# (rows, cols) = cm_data.shape
# 获取经纬度
lon_lat_data = h5py.File('cm_lon_lat.h5', 'r')
lon = lon_lat_data['lon'][:]  # [80 ~ 200]
lat = lon_lat_data['lat'][:]  # [-60 ~ 60]
# 处理CM数据, 0=None不显示
file_path = 'H08_20170131_0000_CM.nc'
data_set = nc.Dataset(file_path)
cm_data = data_set.variables['CM'][:]
cm_data = np.where(cm_data == 0, np.nan, cm_data)
# 创建图形对象（画布） 指定画布大小
fig = plt.figure(num='CM', figsize=(4, 4), dpi=200)
# 创建绘图区域(通过投影方式指定为地理坐标轴)
# geo_axes = plt.axes(projection=ccrs.PlateCarree())  # 全球图像的中央位于太平洋180度经线处
geo_axes = fig.add_subplot(projection=ccrs.PlateCarree())
# # 添加特征
# geo_axes.add_feature(cf.LAND)  # 添加陆地
# geo_axes.add_feature(cf.RIVERS, lw=0.3)  # 添加河流，粗细
# geo_axes.add_feature(cf.OCEAN)  # 添加海洋, 加载分辨率50m
# geo_axes.add_feature(cf.LAKES)  # 添加湖泊 颜色：blue
# 添加经纬度坐标
x_extent = [-180, -135, -90, -45, 0, 45, 90, 135, 180]  # 东西经
y_extent = [-90, -60, -30, 0, 30, 60, 90]  # 南北纬
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
geo_axes.set_title('H08_20170131_0000_CM')
bounds = np.arange(1, 6.5, 0.5)
# # 填充轮廓线
filled_cf = plt.contourf(lon, lat, cm_data,
                         extend='both',
                         levels=bounds,
                         cmap=mpl.cm.jet,
                         transform=ccrs.PlateCarree())
color_bar = fig.colorbar(filled_cf, orientation='horizontal', extend='both', shrink=0.7)
# cmap = mpl.cm.jet
# geo_axes.contourf(lon, lat, cm_data,
#                   extend='both',
#                   cmap=cmap,
#                   transform=ccrs.PlateCarree()
#                   )
# norm = mpl.colors.Normalize(vmin=1, vmax=6)
# sm = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)
# color_bar = plt.colorbar(sm, orientation='horizontal', extend='both', shrink=0.7)
color_bar.ax.tick_params(labelsize=4)
# 图像显示
plt.show()
