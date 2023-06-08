"""
    Create on 2021
    Author: Bazen
    Describe: This is a function for reading spectral data.
    Changed on 2023-06-08
    Author: Bazen
"""

import time
import gdal
import os
import sys
import numpy as np
import pandas as pd


"""路径、参数"""
inputdir = R'F:\test'  # 需要进行光谱数据读取的文件夹
suffix = '.raw'  # 你要读取的光谱数据文件后缀, 如.raw, .bil, .spe

"""测试用主程序"""

def main():
    # 循环读取文件, 请勿包含文件夹, 易出问题

    # 遍历文件夹下所有包含后缀的 光谱文件
    for (root, dirs, files) in os.walk(inputdir):  # 输入路径，需包含光谱文件
        for file in files:  # files为所有文件名，循环读取每一个文件名
            filename = os.path.basename(file)  # 文件名
            json_name = os.path.splitext(os.path.split(file)[-1])[0]  # 文件名 (无后缀)

            if file.endswith(suffix):  # 判断是否为.json标签文件
                start_time = time.clock()

                # 打开对应光谱文件
                spectral_data_path = os.path.join(root, file)
                # 读取光谱源数据及参数
                dataset, spec_data0, proj, geotrans, bands_value = read_spectral(spectral_data_path, True)

                print("数据读取用时: %.4fs" % (time.clock() - start_time))



# 读光谱文件
def read_spectral(filename, if_show_data=False):  # self,
    """
    example: dataset, proj, geotrans, spec_data = read_spectral("E:/.../newdata.spe")
    """

    # print("Loading spectral data ......")

    dataset = gdal.Open(filename)        # 打开文件
    spec_width = dataset.RasterXSize     # 栅格矩阵的列数
    spec_height = dataset.RasterYSize    # 栅格矩阵的行数
    spec_proj = dataset.GetProjection()  # 地图投影信息
    spec_geotrans = dataset.GetGeoTransform()  # 仿射矩阵
    # 将数据写成数组, 对应栅格矩阵
    spec_data = dataset.ReadAsArray(0, 0, spec_width, spec_height)
    spec_data = np.array(spec_data, dtype=np.float64)

    if if_show_data:
        # 打印数据参数
        print("数据集描述: " + str(dataset))
        print("数据文件描述: " + str(dataset.GetDescription()))
        print("波段数  : " + str(dataset.RasterCount))
        print("图像长度: " + str(dataset.RasterXSize))
        print("图像宽度: " + str(dataset.RasterYSize))
        print("投影信息: " + str(dataset.GetProjection()))
        print("图像宽度: " + str(dataset.GetGeoTransform()))

    # 获取每个波段的值, nm, 此部分待完善
    bands_value = np.empty(shape=(spec_data.shape[0]),dtype=np.float64)
    # wavelength = dataset.GetMetadata("ENVI").get(u"wavelength")
    # # 分离波长的字符
    # str_bands_value = wavelength.replace(u"{", u"").replace(u"}", u"").split(u",")
    # # 每个波段的波长转换为float类型
    # for band in range(len(str_bands_value)):
    #     bands_value[band] = float(str_bands_value[band])
    #     band += 1
    # print ('{}nm 处近红外光谱反射率为: {}'.format(bands_value[1], data[1, points['y1'], points['x1']]))

    # del dataset
    return dataset, spec_data, spec_proj, spec_geotrans, bands_value


if __name__ == '__main__':
    main()
