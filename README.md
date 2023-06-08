# 如何用python读取我的光谱数据？<br> How to read my spectral data with python?

</div>
<div align="center">
  
简体中文 | [English](README_en.md) </p>

</div>

This project is currently **primarily in Chinese**.

有很多朋友一直问我：python如何读取**光谱数据/高维度数据**？比如作者的近红外高光谱图像 (NIR-HSI, Near-infrared Hyperspectral Imaging) **↓**
![光谱图像示意图](https://github.com/Bazenr/read-spectral-data-with-python/assets/81945216/041b3c14-92db-437b-ac36-5852d08e044e "test")
<p align="center"> 高光谱图像示意图 </p>

格式主要为：**.raw+.hdr / .bil+.hdr / .tif** 为主。而这一部分的坑，我已经踩差不多了: )。因此，本项目主要用于教大家如何使用现有的库 **(gdal, tifffile, SPy, numpy, pandas)** 来读取、处理你的光谱数据。对了，光谱数据如果比较大 (几百m，有几百个，甚至需要循环读取)，那我建议你购买**固态硬盘**存放光谱数据，其读取速度会比机械硬盘高几甚至十几倍。

首先明确**数据结构**：

**.xxx+.hdr 文件的光谱数据结构** <br>
**①** 数据其实是以二进制文件存于.xxx文件中，而这个文件名.xxx不重要 (可以为 .spe / .raw / .bil，甚至为空，只要名字和 .hdr 对上就行)；<br>
**②** .hdr文件称为头文件，里面放有波段数 (**bands**)，波长值 (**wavelength**)，长或宽 (栅格行数: **lines**, 栅格列数: **samples**)，数据存储格式 (**interleave**: BIL, BIP, BSQ等) 数据存储类型 (**data type**) 等。<br>
.xxx+.hdr 结构的数据建议使用 **gdal** 库读取，或安装 **Spectral Python (SPy)**  库，安装过程比较麻烦。本项目暂时只使用 osgeo 下的 gdal 库进行教学。<br>

**.tif 文件的光谱数据结构** <br>
此类型数据和传统的 .png, .jpg 图像类似，但无法用后者常用的 pillow (PIL), imgaug, OpenCV, matplotlib等库读取，一般请直接使用 **tifffile** 库读取。

## gdal 库安装教程

**①** 我推荐安装 Anaconda3 进行python库的管理，安装时自动设置 path，安装一个你喜欢的代码编辑器 (VScode, Pycharm, Jupyter Notebook都行)，平时启动也用Anaconda启动的话问题更少，这部分网上教程很多，不做赘述。然后新建一个 **python==3.6** 的虚拟环境 (python 3.6 下的 gdal 比较稳定，其他的 python 版本下自动安装时我出过库冲突的问题)，我们姑且叫这个环境为gdal_env；<br>
**②** Win+R键 (或右键开始菜单，点击运行)，输入 cmd 回车，使用 activate gdal_env 启动虚拟环境，使用 pip install gdal 并等待自动安装完成。 <br>
至此，你就已经安装好了读取光谱数据所需要的所有东西了，没想到吧……

## gdal 库的使用

gdal 库提供了 **gdal.Open()** 函数，用于读取各种数据类型的光谱文件，但读入的文件还需解构，才能获得原始数据和各种参数信息。
而我和我师弟已经构建了一个简单的光谱读取函数 **read_spectral**，位于文件 **spectral.py** 中，可以直接测试光谱数据读取效果。
同时，你也可以通过将 **spectral.py** 和 **init.py** (空的也必须要) 放入其他项目根目录，在其他代码中使用： <br>
**from spectral import read_spectral** 的方式调用此函数。
