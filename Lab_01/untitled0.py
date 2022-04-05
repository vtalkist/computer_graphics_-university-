from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication

import matplotlib.pyplot as plt 

from os import path
import sys
import array as arr
from PyQt5.uic import loadUiType

FROM_CLASS,_=loadUiType(path.join(path.dirname('__file__'),"main.ui"))

def f(x):
    return {
        0 : "points",
        1 : "lines",
        2 : "triangle"
    }[x]

class Main(QMainWindow, FROM_CLASS):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Buttons()

        
    def Handel_Buttons(self):
        self.convert.clicked.connect(self.PROCESS)
        pass
    

    def PLOT(self, points_x, points_y, points_x_calculated, points_y_calculated, figure_type):
        points_x_buf = arr.array('f', []) # масив точок типу флоат
        points_y_buf = arr.array('f', []) # масив точок типу флоат
        
        points_x_calculated_buf = arr.array('f', []) # масив точок типу флоат
        points_y_calculated_buf = arr.array('f', []) # масив точок типу флоат
        
        fig = plt.figure()                                              #створення зовнішнього вікна
        ax = fig.add_subplot(111)                                       #створення осей X, Y
        
        ax.set(facecolor ='#bbbbbb',                                    #колір області значень
               xlim      = [-10,10],                                      #межі області по X
               ylim      = [-10,10],                                      #межі області по Y
               title     = '<Лабораторна робота №> <ПІБ> <група>',    #заголовок роботи
               xlabel    = 'Вісь абцис X',
               ylabel    = 'Вісь ординат Y')                            #назви осей координат
        
        ax.plot(   [0, 0],
                   [-30, 30],                                           #побудова відрізка
                   color = 'black',                                     #колір
                   linewidth = 1,                                       #ширина лінії
                   linestyle = '--')                                    #вісь y
        ax.plot(   [-30, 30],
                   [0, 0],                                              #побудова відрізка
                   color = 'black',                                     #колір
                   linewidth = 1,                                       #ширина лінії
                   linestyle = '--')                                    #вісь x ("--" - пунктирна лінія)
        print("figure type num == ", figure_type)
        if figure_type == 0:
            ax.plot(points_x_calculated, points_y_calculated, 'ro', markersize=10)
            ax.plot(points_x, points_y, 'bo')
        elif figure_type == 1:
            ax.plot(points_x_calculated, points_y_calculated, 'r', linewidth=3)
            ax.plot(points_x, points_y, 'b')
        elif figure_type == 2:
            print("type triangle")
  
            ax.plot(points_x_calculated, points_y_calculated, 'r', linewidth=3)

            points_x_calculated_buf.append(points_x_calculated[0])
            points_y_calculated_buf.append(points_y_calculated[0])
            points_x_calculated_buf.append(points_x_calculated[2])
            points_y_calculated_buf.append(points_y_calculated[2])
            #print(points_x_calculated_buf)
            #print(points_y_calculated_buf)
            ax.plot(points_x_calculated_buf, points_y_calculated_buf, 'r', linewidth=4)
            #===================================================================
            plt.plot(points_x, points_y, 'b')

            points_x_buf.append(points_x[0])
            points_y_buf.append(points_y[0])
                
            points_x_buf.append(points_x[2])
            points_y_buf.append(points_y[2])
            
            #print(points_x_calculated_buf)
            #print(points_y_calculated_buf)
            plt.plot(points_x_buf, points_y_buf, 'b')        
        

        plt.show()


    def CALCULATE_POINTS(self, points_x, points_y, matrix, points_x_calculated, points_y_calculated):
       
        if len(matrix) > 4:
            for i in range(0, len(points_x), 1):
                points_x_calculated.append(points_x[i] + matrix[4])
                points_y_calculated.append(points_y[i] + matrix[5])
        print("================================")
        print(points_x_calculated)
        print(points_y_calculated)
        
        if len(matrix) < 5:
            for i in range(0, len(points_x), 1):
                points_x_calculated.append(points_x[i] * matrix[0] + points_y[i] * matrix[2])
                points_y_calculated.append(points_x[i] * matrix[1] + points_y[i] * matrix[3])
        
        print("calculated")
        print(points_x_calculated)
        print(points_y_calculated)
        
        
    def PROCESS(self):
        points_x = arr.array('f', []) # масив точок типу флоат
        points_y = arr.array('f', []) # масив точок типу флоат
        matrix = arr.array('f', []) # масив матриці типу флоат
        
        points_x_calculated = arr.array('f', []) # масив точок типу флоат
        points_y_calculated = arr.array('f', []) # масив точок типу флоат
        #transformed = arr.array('f', []) # масив опрацьованих точок флоат
        
        points_list_fields = [] # список об'єктів для точок
        matrix_list_fields = [] # список об'єктів для матриці
        #figure_type_radiobuttons = [] #сипсок об'єктів радіобатонів
        
        points_list_fields.extend([self.Point_0_0, self.Point_0_1,\
                                  self.Point_1_0, self.Point_1_1,\
                                  self.Point_2_0, self.Point_2_1,\
                                  self.Point_3_0, self.Point_3_1])
        
        for i in range(0, len(points_list_fields), 2):
            if len(points_list_fields[i].text()) > 0:
                print("index", i)
                points_x.append(float(points_list_fields[i].text()))
                points_y.append(float(points_list_fields[i+1].text()))
        
        print("points x:")
        print(points_x)
        
        print("points y:")
        print(points_y)
        
        matrix_list_fields.extend([self.Matrix_0_1, self.Matrix_0_2,\
                                   self.Matrix_1_1, self.Matrix_1_2,\
                                   self.Matrix_2_0, self.Matrix_2_1])
        
        for i in range(len(matrix_list_fields)):
            if len(matrix_list_fields[i].text()) > 0:
                matrix.append(float(matrix_list_fields[i].text()))
        
        print("matrix: ")
        print(matrix)
        
        figure_type = 0
        if self.radioButton_1.isChecked():
            figure_type = 0
        elif self.radioButton_2.isChecked():
            figure_type = 1
        elif self.radioButton_3.isChecked():
            figure_type = 2
        
        self.CALCULATE_POINTS(points_x, points_y, matrix, points_x_calculated, points_y_calculated)
        self.PLOT(points_x, points_y, points_x_calculated, points_y_calculated, figure_type)
        
        
        print("passed points")
        print(points_y_calculated)


        
        
def main():

    app=QApplication(sys.argv)
    window=Main()
    window.show()
    app.exec_()
        
    
if __name__=='__main__':
    main()
    