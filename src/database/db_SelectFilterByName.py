import controllers.adjustmentPanel

from flask import redirect
from db import mysql


class db_SelectFilterByName():
    def Select(name):
        with mysql.cursor() as cur:
            cur.execute(
                "SELECT * FROM parametersAdjustFilterImg WHERE name = %s", name)
            data = cur.fetchone()
            if data != None:
                controllers.adjustmentPanel.varname = data[1]
                controllers.adjustmentPanel.varTrackbar1 = data[2]
                controllers.adjustmentPanel.varTrackbar2 = data[3]
                controllers.adjustmentPanel.varTrackbar3 = data[4]
                controllers.adjustmentPanel.varTrackbar4 = data[5]
                controllers.adjustmentPanel.varTrackbar5 = data[6]
                controllers.adjustmentPanel.varTrackbar6 = data[7]
                controllers.adjustmentPanel.varTrackbar_iterations_erode = data[8]
                controllers.adjustmentPanel.varTrackbar_iterations_dilate = data[9]
                controllers.adjustmentPanel.varTrackbar_TamMinLv = data[10]
                controllers.adjustmentPanel.varTrackbar_TamMaxLv = data[11]
                controllers.adjustmentPanel.varTrackbar_TamMinLh = data[12]
                controllers.adjustmentPanel.varTrackbar_TamMaxLh = data[13]
                controllers.adjustmentPanel.varTrackbar_TamMin = data[14]
                controllers.adjustmentPanel.varTrackbar_TamMax = data[15]
                controllers.adjustmentPanel.varTrackbar_LineHorizontal = data[16]
                controllers.adjustmentPanel.varTrackbar_LineVertical = data[17]
                controllers.adjustmentPanel.varTrackbar_LineRange = data[18]
            return data
