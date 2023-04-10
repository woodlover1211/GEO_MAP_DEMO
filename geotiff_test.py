from osgeo import gdal
import numpy as np
import pandas as pd
# file_name = 'GF5_AHSI_E34.27_N60.83_20190614_005849_L10000047825.tif'
file_name = 'E:/test/GF5/GF5_AHSI_E34.27_N60.83_20190614_005849_L10000047825/GF5_AHSI_E34.27_N60.83_20190614_005849_L10000047825.geotiff'
data_set = gdal.Open(file_name)
# print(dir(data_set))
# print(data_set.GetMetadata())
# print(data_set.RasterCount)  # 获得栅格数据集的波段数 180
# print(data_set.RasterXSize)  # 栅格数据的宽度 (X 方向上的像素个数) 2011
# print(data_set.RasterYSize)  # 栅格数据的高度 (Y 方向上的像素个数) 2180
# print(data_set.GetGeoTransform())  # 地理空间
# print(data_set.GetRasterBand(1))
# (2180*2011)
# x_size = data_set.RasterXSize  # 2011 column列数
# y_size = data_set.RasterYSize  # 2180 row行数
# bandCount = data_set.RasterCount
band1 = data_set.GetRasterBand(1)  # XSize=2011, YSize=2180
data = band1.ReadAsArray()  # (2180,2011)二维数组像素值 narray
print(data)
# print(np.max(data))
# print(np.min(data))
# print(data.shape) (2180,2011)
# df = pd.DataFrame(data)
# df.to_csv('band90.csv')

# # 输出数据集,指定格式
# geotiff_driver = gdal.GetDriverByName('GTiff')
# out_ds = geotiff_driver.Create('band90_out.tif', col, row)
# # 地理投影
# out_ds.SetProjection(data_set.GetProjection())
# geo_transform = list(data_set.GetGeoTransform())
# # 像素为原来的1/4
# geo_transform[1] /= 2
# geo_transform[5] /= 2
# out_ds.SetGeoTransform(geo_transform)
# # 数据缓冲
# 像素大小减半
# row = band1.YSize*2
# col = band1.XSize*2
# data = band1.ReadAsArray(buf_xsize=col, buf_ysize=row)
# # 输出光栅数据
# out_band1 = out_ds.GetRasterBand(1)
# out_band1.WriteArray(data)
# # 构建概视图
# out_band1.FlushCache()
# # out_band1.ComputeStatistics(False)
# out_ds.BuildOverviews('average', [2, 4, 8, 16, 32, 64])
