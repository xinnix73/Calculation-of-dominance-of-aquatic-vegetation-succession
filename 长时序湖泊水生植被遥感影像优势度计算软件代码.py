#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from osgeo import gdal
import cv2
import numpy as np
import os
#import numpy as np 
class Ui_Window1(object):
    def setupUi(self, Window1):
        Window1.setObjectName("Window1")
        Window1.resize(800, 670)
        self.centralwidget = QtWidgets.QWidget(Window1)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 170, 51, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 10, 61, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 10, 51, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 180, 721, 481))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 10, 151, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_9 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout.addWidget(self.pushButton_9)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(640, 20, 121, 131))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_10 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_3.addWidget(self.pushButton_10)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(380, 10, 171, 162))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_4.addWidget(self.pushButton_5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_4.addWidget(self.pushButton_8)
        self.pushButton_11 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_4.addWidget(self.pushButton_11)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 90, 82, 73))
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_5.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_5.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_5.addWidget(self.radioButton_3)
        Window1.setCentralWidget(self.centralwidget)

        self.retranslateUi(Window1)
        
        self.pushButton.clicked.connect(self.bt)
        self.pushButton_2.clicked.connect(self.bt2)
        self.pushButton_3.clicked.connect(self.bt3)
        self.pushButton_4.clicked.connect(self.bt4)
        self.pushButton_5.clicked.connect(self.bt5)
        self.pushButton_8.clicked.connect(self.bt8)
        self.pushButton_9.clicked.connect(self.bt9)
        self.pushButton_10.clicked.connect(self.bt10)
        self.pushButton_11.clicked.connect(self.bt11)
        self.radioButton.clicked.connect(self.rbt1)
        self.radioButton_2.clicked.connect(self.rbt2)
        self.radioButton_3.clicked.connect(self.rbt3)
        
    
        QtCore.QMetaObject.connectSlotsByName(Window1)

    def retranslateUi(self, Window1):
        _translate = QtCore.QCoreApplication.translate
        Window1.setWindowTitle(_translate("Window1", "MainWindow"))
        self.label.setText(_translate("Window1", "结果："))
        self.label_2.setText(_translate("Window1", "独立分类"))
        self.label_3.setText(_translate("Window1", "总分类"))
        self.pushButton.setText(_translate("Window1", "沉水植被影像"))
        self.pushButton_2.setText(_translate("Window1", "挺水浮叶植被影像"))
        self.pushButton_3.setText(_translate("Window1", "计算"))
        self.pushButton_9.setText(_translate("Window1", "保存频率图"))
        self.pushButton_10.setText(_translate("Window1", "选择矢量文件"))
        self.pushButton_4.setText(_translate("Window1", "批量裁剪并保存"))
        self.pushButton_5.setText(_translate("Window1", "水生植被分类影像"))
        self.label_5.setText(_translate("Window1", "沉水植被值"))
        self.label_6.setText(_translate("Window1", "浮叶挺水值"))
        self.pushButton_8.setText(_translate("Window1", "计算"))
        self.pushButton_11.setText(_translate("Window1", "保存频率图"))
        self.radioButton.setText(_translate("Window1", "伪彩色1"))
        self.radioButton_2.setText(_translate("Window1", "伪彩色2"))
        self.radioButton_3.setText(_translate("Window1", "伪彩色3"))

    #def bttt(self):
    #    txt = self.lineEdit.text()
    #    txt2 = int(txt)
    #    print(txt2)
    def rbt1(self):
        global false_color
        false_color = cv2.COLORMAP_BONE
        
    def rbt2(self):
        global false_color
        false_color = cv2.COLORMAP_PINK
        
    def rbt3(self):
        global false_color
        false_color = cv2.COLORMAP_JET
            
    def bt(self):
        global csfname
        csfname,_=QtWidgets.QFileDialog.getOpenFileNames(self, '选择沉水植被影像')
        
        
    def bt2(self):
        global fyfname
        fyfname,_=QtWidgets.QFileDialog.getOpenFileNames(self, '选择挺水浮叶植被影像')
        
    
    def bt3(self):
        global image
        def read_image(path):
            image_matrix = gdal.Open(path).ReadAsArray()
            return image_matrix
        def cal_image_matrix_mean(filename_list):
            image_matrix_list = list(map(read_image,filename_list))
            image_matrix_sum = 0
            for i in image_matrix_list:
                image_matrix_sum+=i
            image_matrix_mean = image_matrix_sum/(len(image_matrix_list))
            return image_matrix_mean
        cs = cal_image_matrix_mean(csfname)
        fy = cal_image_matrix_mean(fyfname)
        image = fy-cs
        final_img=cv2.resize(src=image, dsize=None, fx=0.2, fy=0.2)
        final_img = ((image-(image.min()))/((image.max())-(image.min())))*255
        final_img2 = np.array(final_img,np.uint8)
        final_img3 = cv2.applyColorMap(final_img2, false_color) #COLORMAP_RAINBOW COLORMAP_OCEAN COLORMAP_WINTER
        final_img4=cv2.cvtColor(final_img3,cv2.COLOR_BGR2RGB)
        self.final_image = QtGui.QImage(final_img4[:],final_img4.shape[1], final_img4.shape[0],final_img4.shape[1] * 3, QtGui.QImage.Format_RGB888)                      
        #
        self.label_4.setPixmap(QtGui.QPixmap(self.final_image))#scaled(self.label.width(), self.label.height())
        self.label_4.setScaledContents (True)
        
        #self.final_image = QtGui.QImage(final_img[:], final_img.shape[1], final_img.shape[0], QtGui.QImage.Format_Grayscale16)#final_img.shape[1]
        #self.label_4.setPixmap(QtGui.QPixmap.fromImage(self.final_image).scaled(self.label.width(), self.label.height()))
        #self.label_4.setScaledContents (True)
        
    def bt9(self):
        save_path,_= QtWidgets.QFileDialog.getSaveFileName(self, '保存频率图')
        dataset = gdal.Open(csfname[0])
        im_width = dataset.RasterXSize    
        im_height = dataset.RasterYSize   
        im_geotrans = dataset.GetGeoTransform()  
        im_proj = dataset.GetProjection() 
        im_data = dataset.ReadAsArray()
        driver = gdal.GetDriverByName("GTiff")                
        dataset2 = driver.Create(save_path, im_width, im_height, 1, gdal.GDT_Float32)
        dataset2.SetGeoTransform(im_geotrans)              
        dataset2.SetProjection(im_proj)
        dataset2.GetRasterBand(1).WriteArray(image)
        del dataset2
        
        
    def bt5(self):
        global allfname
        allfname,_=QtWidgets.QFileDialog.getOpenFileNames(self, '选择水生分类植被影像')
        
    def bt8(self):
        global image2
        cs_value = int(self.lineEdit.text()) 
        fy_value = int(self.lineEdit_2.text())
        def baoliu_cs(path):
            image_matrix = gdal.Open(path).ReadAsArray()
            cs_matrix = np.copy(image_matrix)
            cs_matrix[cs_matrix!=cs_value]= 0
            return cs_matrix
        
        def baoliu_fy(path):
            image_matrix = gdal.Open(path).ReadAsArray()
            fy_matrix = np.copy(image_matrix)
            fy_matrix[fy_matrix!=fy_value]= 0
            return fy_matrix
        
        def cal_image_matrix_mean(image_matrix_list):
            image_matrix_sum = 0
            for i in image_matrix_list:
                image_matrix_sum+=i
            image_matrix_mean = image_matrix_sum/(len(image_matrix_list))
            return image_matrix_mean
        cs_image_list = list(map(baoliu_cs,allfname))
        fy_image_list = list(map(baoliu_fy,allfname))
        cs = cal_image_matrix_mean(cs_image_list)
        fy = cal_image_matrix_mean(fy_image_list)
        image2 = fy-cs
        final_img = ((image2-(image2.min()))/((image2.max())-(image2.min())))*255
        final_img2 = np.array(final_img,np.uint8)
        final_img3 = cv2.applyColorMap(final_img2, cv2.COLORMAP_BONE) #COLORMAP_RAINBOW COLORMAP_OCEAN COLORMAP_WINTER
        final_img4=cv2.cvtColor(final_img3,cv2.COLOR_BGR2RGB)
        self.final_image = QtGui.QImage(final_img4[:],final_img4.shape[1], final_img4.shape[0],final_img4.shape[1] * 3, QtGui.QImage.Format_RGB888)                      
        self.label_4.setPixmap(QtGui.QPixmap(self.final_image))#scaled(self.label.width(), self.label.height())
        self.label_4.setScaledContents (True)
        
        
    def bt11(self):
        save_path,_= QtWidgets.QFileDialog.getSaveFileName(self, '保存频率图')
        dataset = gdal.Open(allfname[0])
        im_width = dataset.RasterXSize    
        im_height = dataset.RasterYSize   
        im_geotrans = dataset.GetGeoTransform()  
        im_proj = dataset.GetProjection() 
        im_data = dataset.ReadAsArray()
        driver = gdal.GetDriverByName("GTiff")                
        dataset2 = driver.Create(save_path, im_width, im_height, 1, gdal.GDT_Float32)
        dataset2.SetGeoTransform(im_geotrans)              
        dataset2.SetProjection(im_proj)
        dataset2.GetRasterBand(1).WriteArray(image2)
        del dataset2        
            
        
    
    
    
    
    
    def bt10(self):
        global shpfname
        shpfname,_=QtWidgets.QFileDialog.getOpenFileNames(self, '选择矢量文件')  
    def bt4(self):
        clip_file_savedir= QtWidgets.QFileDialog.getExistingDirectory(self, '选择裁剪结果保存文件夹')
        print(clip_file_savedir)
        def read_clip_image(i):
            input_raster = gdal.Open(i)
            filename_basename = os.path.basename(i)
            name_clip = os.path.splitext(filename_basename)
            output_raster = clip_file_savedir+'/'+name_clip[0]+'_clip'+name_clip[1]
            ds = gdal.Warp(output_raster,
                      input_raster,
                      format = 'GTiff',
                      cutlineDSName = shpfname[0],      
                      cutlineWhere="FIELD = 'whatever'",
                      cropToCutline=True, 
                      dstNodata = 0)
        list(map(read_clip_image,csfname))
        list(map(read_clip_image,fyfname))
        list(map(read_clip_image,allfname))
        
        
class CoperQt(QtWidgets.QMainWindow,Ui_Window1):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_Window1.__init__(self)
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CoperQt()
    window.show()
    sys.exit(app.exec_())           
        
        


# In[ ]:




