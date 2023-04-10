import numpy as np
import scipy.io as scio
import matplotlib.pyplot as plt
import matplotlib as mpl
import sklearn.datasets as skdata
import cv2
import rawpy
import imageio
import imageio.v3 as iiv3

# GF5_AHSI_SWIR_Spectralresponse
# GF5_AHSI_SWIR_RadCal
file_path = 'D:\work_file\geo_files\GF5_AHSI_E34.27_N60.83_20190614_005849_L10000047825\GF5_AHSI_SWIR_RadCal.raw'
raw_data = np.fromfile(file_path, dtype='uint8')
# print(raw_data)
# print(raw_data.shape)
# 3780(60*63) 1606(22*73)
img_data = raw_data.reshape(22, 73, 1)  # 数组重新排列 三维组合
print(img_data.shape)
# 图像展示
cv2.imshow('test_raw', img_data)
cv2.imwrite('D:/temp_file/GF5_AHSI_SWIR_RadCal.png', img_data)
# dst = cv2.cvtColor(img_data, cv2.COLOR_BAYER_BG2BGR)
# cv2.imshow('test_dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()

# file = 'D:\download_file\edge_files\lena512.raw'
# im = iiv3.imopen(file, 'r')
# print(im.__dict__)
# im = imageio.read(file)
# image = imageio.get_reader(file)
# print(image.__dir__())
# print(im)
# rows = 512
# cols = 512
# channels = 1
# file = 'D:\download_file\edge_files\lena512.raw'
# img = np.fromfile(file, dtype='uint8')
# # print(img)
# img = img.reshape(rows, cols, channels)
# # print(img)
# print(img.shape)
# cv2.imshow('raw_test', img)
# cv2.waitKey()
# cv2.destroyAllWindows()

# raw = rawpy.imread(file_path)
# print(raw)
# bayer = raw.raw_image_visible
# print(bayer.shape)
# rgb = raw.postprocess(use_camera_wb=True, half_size=True, no_auto_bright=True, output_bps=16)
# raw.close()
# print(rgb.dtype, rgb.shape)
# plt.imshow(rgb)
# plt.pause(10)

# dataFile = 'files/matlab.mat'  # 写入mat文件的位置和名称用/隔开
# data = scio.loadmat(dataFile)  # data为对应文件的字典
# z = data['Z']  # 通过 字典【‘矩阵名’】的形式读取矩阵
# x = data['X']  # 经度
# # 只选择第一行所有列的数据 7201
# x = x[1, :]
# y = data['Y']  # 纬度
# # 第一列的所有行 3601
# y = y[:, 1]
# lon =[]
# lat =[]
# not_nan = ~np.isnan(z)
# index_array = np.argwhere(not_nan)
# for index in index_array:
#     # print(index)
#     (row, col) = index
#     lon.append(x[col])
#     lat.append(y[row])
# z = z[not_nan]
# print(lon)
# print(lat)
# print(len(lon))
# print(len(lat))
# # Fixing random state for reproducibility
# np.random.seed(19680801)
# N = 50
# x = np.random.rand(N)
# y = np.random.rand(N)
# colors = np.random.rand(N)
# area = (30 * np.random.rand(N))**2  # 0 to 15 point radii
# plt.scatter(x, y, s=None, alpha=0.5, vmin=0, vmax=7e-5, cmap=mpl.cm.jet)
# plt.show()
# file_path = 'files/CO2_SSP119_2015_2150.nc'
# data_set = nc.Dataset(file_path)
# # print(data_set.variables.keys())
# co2_ssp_data = data_set.variables['CO2'][:]
# print(co2_ssp_data.shape)  # (1632, 180, 360) = (month, lat, lon)
# 矩阵转置（360，180） 第61条数据对应2020-01
# co2 = co2_ssp_data[20, :, :].T
# # print(co2.shape)
# lon = np.zeros(co2.shape)
# lon_data = data_set.variables['longitude'][:]
# # 经度：某一行每一列数值相同(360行，每行重复180列)
# for i in range(len(lon_data)):
#     lon[i, :] = lon_data[i]
# # print(lon)
# # print(lon.shape)
# lat = np.zeros(co2.shape)
# lat_data = data_set.variables['latitude'][:]
# # 纬度：某一列每一行数值相同（180列，每列重复360行）
# for j in range(len(lat_data)):
#     lat[:, j] = lat_data[j]
# print(lat)
# print(lat.shape)
# 写入HDF
# h5_data = h5py.File('files/co2ssp_lon_lat.h5', 'w')
# h5_data['lon'] = lon
# h5_data['lat'] = lat
