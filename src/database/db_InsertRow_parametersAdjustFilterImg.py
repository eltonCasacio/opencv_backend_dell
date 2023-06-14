import controllers.adjustmentPanel

from flask import redirect
from db import mysql


class Insert_parametersAdjustFilterImg():
    def salvar():
        name = controllers.adjustmentPanel.varname
        parameter01 = controllers.adjustmentPanel.varTrackbar1
        parameter02 = controllers.adjustmentPanel.varTrackbar2
        parameter03 = controllers.adjustmentPanel.varTrackbar3
        parameter04 = controllers.adjustmentPanel.varTrackbar4
        parameter05 = controllers.adjustmentPanel.varTrackbar5
        parameter06 = controllers.adjustmentPanel.varTrackbar6
        parameter07 = controllers.adjustmentPanel.varTrackbar_iterations_erode
        parameter08 = controllers.adjustmentPanel.varTrackbar_iterations_dilate
        parameter09 = controllers.adjustmentPanel.varTrackbar_TamMinLv
        parameter10 = controllers.adjustmentPanel.varTrackbar_TamMaxLv
        parameter11 = controllers.adjustmentPanel.varTrackbar_TamMinLh
        parameter12 = controllers.adjustmentPanel.varTrackbar_TamMaxLh
        parameter13 = controllers.adjustmentPanel.varTrackbar_TamMin
        parameter14 = controllers.adjustmentPanel.varTrackbar_TamMax
        parameter15 = controllers.adjustmentPanel.varTrackbar_LineHorizontal
        parameter16 = controllers.adjustmentPanel.varTrackbar_LineVertical
        parameter17 = controllers.adjustmentPanel.varTrackbar_LineRange
        parameter18 = 0
        parameter19 = 0
        parameter20 = 0

        with mysql.cursor() as cur:
            # try:
            cur.execute("INSERT INTO parametersAdjustFilterImg VALUE"
                        "(0, %s, "
                        "%s, %s, %s, %s, %s, "
                        "%s, %s, %s, %s, %s, "
                        "%s, %s, %s, %s, %s, "
                        "%s, %s, %s, %s, %s"
                        ")",
                        (name,
                         parameter01, parameter02, parameter03, parameter04, parameter05,
                         parameter06, parameter07, parameter08, parameter09, parameter10,
                         parameter11, parameter12, parameter13, parameter14, parameter15,
                         parameter16, parameter17, parameter18, parameter19, parameter20)
                        )
            cur.connection.commit()
            #    print('PARAMETROS SALVO COM SUCESSO', 'success')
            #    flash('PARAMETROS SALVO COM SUCESSO', 'success')
            # except:
            #    print('ERRO AO SALVAR PARAMETROS', 'error')
            #    flash('ERRO AO SALVAR PARAMETROS', 'error')
        return redirect('base.html')
