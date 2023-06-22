import json
import controllers.adjustmentPanel

from flask import Response
from flask import render_template, request
from flask_cors import CORS
from database.db_DeleteFilter import db_DeleteFilter
from database.db_InsertRow_parametersAdjustFilterImg import Insert_parametersAdjustFilterImg
from database.db_SelectFilterByName import db_SelectFilterByName
from database.db_SelectFiltersName import db_SelectFiltersName
from database.db_SelectRow_nameParameters import SelectRow_NameParametersAdjustFilterImg
from database.db_SelectRow_SeachForID import selectRow_SearchForID

import controllers.controller
import controllers.frames


def init_app(app):
    CORS(app, resources={"*": {"origins": "*"}})

    @app.route("/loeheight", methods=["POST"])
    def l():
        request_data = request.get_json()
        color = request_data["color"]
        low = request_data["low"]
        hight = request_data["hight"]

        if (low != None and hight != None):
            match color:
                case "vermelho":
                    if (controllers.adjustmentPanel.varTrackbar1 != int(low)):
                        controllers.adjustmentPanel.varTrackbar1 = int(low)
                    if (controllers.adjustmentPanel.varTrackbar4 != int(hight)):
                        controllers.adjustmentPanel.varTrackbar4 = int(hight)
                case "verde":
                    if (controllers.adjustmentPanel.varTrackbar2 != int(low)):
                        controllers.adjustmentPanel.varTrackbar2 = int(low)
                    if (controllers.adjustmentPanel.varTrackbar5 != int(hight)):
                        controllers.adjustmentPanel.varTrackbar5 = int(hight)
                case "azul":
                    if (controllers.adjustmentPanel.varTrackbar3 != int(low)): 
                        controllers.adjustmentPanel.varTrackbar3 = int(low)
                    if (controllers.adjustmentPanel.varTrackbar6 != int(hight)):
                        controllers.adjustmentPanel.varTrackbar6 = int(hight)
        return 'ok'
    
    @app.route("/tamminmaxlvlh", methods=["POST"])
    def tamminmaxlvlh():
        request_data = request.get_json()
        lvlh = request_data["attr"]
        min = request_data["min"]
        max = request_data["max"]

        if (min != None and max != None):
            match lvlh:
                case "lv":
                    if (controllers.adjustmentPanel.varTrackbar_TamMinLv != int(min)):
                        controllers.adjustmentPanel.varTrackbar_TamMinLv = int(min)
                    if (controllers.adjustmentPanel.varTrackbar_TamMaxLv != int(max)):
                        controllers.adjustmentPanel.varTrackbar_TamMaxLv = int(max)    
                case "lh":
                    if (controllers.adjustmentPanel.varTrackbar_TamMinLh != int(min)):
                        controllers.adjustmentPanel.varTrackbar_TamMinLh = int(min)
                    if (controllers.adjustmentPanel.varTrackbar_TamMaxLh != int(max)):
                        controllers.adjustmentPanel.varTrackbar_TamMaxLh = int(max)
        return 'ok'

    @app.route("/tamminmax", methods=["POST"])
    def tamminmax():
        request_data = request.get_json()
        min = request_data["min"]
        max = request_data["max"]

        if (min != None and max != None):
           if (controllers.adjustmentPanel.varTrackbar_TamMin != int(min)):
                controllers.adjustmentPanel.varTrackbar_TamMin = int(min)
           if (controllers.adjustmentPanel.varTrackbar_TamMax != int(max)):
                controllers.adjustmentPanel.varTrackbar_TamMax = int(max)
        return 'ok'
    
    
    @app.route("/iterations_erode", methods=["POST"])
    def iterations_erode():
        request_data = request.get_json()
        value = request_data["value"]

        if (value != None):
           if (controllers.adjustmentPanel.varTrackbar_iterations_erode != int(value)):
                    controllers.adjustmentPanel.varTrackbar_iterations_erode = int(value)
        return 'ok'
    
    
    @app.route("/iterations_dilate", methods=["POST"])
    def iterations_dilate():
        request_data = request.get_json()
        value = request_data["value"]

        if (value != None):
           if (controllers.adjustmentPanel.varTrackbar_iterations_dilate != int(value)):
                    controllers.adjustmentPanel.varTrackbar_iterations_dilate = int(value)
        return 'ok'

    
    @app.route("/trackbar_LineVertical", methods=["POST"])
    def trackbar_LineVertical():
        request_data = request.get_json()
        value = request_data["value"]

        if (value != None):
           if (controllers.adjustmentPanel.varTrackbar_LineVertical != int(value)):
                    controllers.adjustmentPanel.varTrackbar_LineVertical = int(value)
        return 'ok'
    

    @app.route("/trackbar_LineHorizontal", methods=["POST"])
    def trackbar_LineHorizontal():
        request_data = request.get_json()
        value = request_data["value"]

        if (value != None):
           if (controllers.adjustmentPanel.varTrackbar_LineHorizontal != int(value)):
                    controllers.adjustmentPanel.varTrackbar_LineHorizontal = int(value)
        return 'ok'
    

    @app.route("/trackbar_LineRange", methods=["POST"])
    def trackbar_LineRange():
        request_data = request.get_json()
        value = request_data["value"]

        if (value != None):
           if (controllers.adjustmentPanel.varTrackbar_LineRange != int(value)):
                    controllers.adjustmentPanel.varTrackbar_LineRange = int(value)
        return 'ok'
    

    @app.route("/save-filter", methods=["POST"])
    def saveFilter():
        request_data = request.get_json()
        fileName = request_data['fileName']
        controllers.adjustmentPanel.varname = fileName
        Insert_parametersAdjustFilterImg.salvar()
        return 'ok'
    

    @app.route("/filter", methods=["POST"])
    def filter():
        request_data = request.get_json()
        fileName = request_data['fileName']
        if len(fileName) <= 0:
            return ''
       
        data = db_SelectFilterByName.Select(fileName)
        if data == None:
            return ''

        return {
            'id': data[0],
            'name': data[1],
            'lvermelho': data[2],
            'lverde': data[3],
            'lazul': data[4],
            'hvermelho': data[5],
            'hverde': data[6],
            'hazul': data[7],
            'erode': data[8],
            'dilate': data[9],
            'tamMinLv': data[10],
            'tamMaxLv': data[11],
            'tamMinLh': data[12],
            'tamMaxLh': data[13],
            'tamMin': data[14],
            'tamMax': data[15],
            'lineHorizontal': data[16],
            'lineVertical': data[17],
            'lineRange': data[18],
        }


    @app.route("/filters", methods=["GET"])
    def filtersName():
        filters = db_SelectFiltersName.Select()
        if len(filters) > 0:
            arrayFilters = []
            for i in list(filters):
                arrayFilters.append(i[0])
            return arrayFilters
        return []
    
    
    @app.route("/delete-filter", methods=["POST"])
    def deletefilter():
        request_data = request.get_json()
        name = request_data["name"]
        try:
            db_DeleteFilter.Delete(name)
        except:
            return 'Erro ao excluir filtro'
        return 'ok'
    
    @app.route("/", methods=["GET", "POST"])
    def index():
        nameParameters = SelectRow_NameParametersAdjustFilterImg.Select()

        if request.method == "POST":
            if (request.form.get("parametrosSelect") != None):
                print("chamada de parametrosSelect")
                print(request.form.get("parametrosSelect"))
                selectRow_SearchForID.Select(
                    int(request.form.get("parametrosSelect")))

            # if (request.form.get("trackbar1") != None):
            #     if (controllers.adjustmentPanel.varTrackbar1 != int(request.form.get("trackbar1"))):
            #         controllers.adjustmentPanel.varTrackbar1 = int(
            #             request.form.get("trackbar1"))
            #     elif (controllers.adjustmentPanel.varTrackbar1 != int(request.form.get("number1"))):
            #         controllers.adjustmentPanel.varTrackbar1 = int(
            #             request.form.get("number1"))

            # if (request.form.get("trackbar2") != None):
            #     if (controllers.adjustmentPanel.varTrackbar2 != int(request.form.get("trackbar2"))):
            #         controllers.adjustmentPanel.varTrackbar2 = int(
            #             request.form.get("trackbar2"))
            #     elif (controllers.adjustmentPanel.varTrackbar2 != int(request.form.get("number2"))):
            #         controllers.adjustmentPanel.varTrackbar2 = int(
            #             request.form.get("number2"))

            # if (request.form.get("trackbar3") != None):
            #     if (controllers.adjustmentPanel.varTrackbar3 != int(request.form.get("trackbar3"))):
            #         controllers.adjustmentPanel.varTrackbar3 = int(
            #             request.form.get("trackbar3"))
            #     elif (controllers.adjustmentPanel.varTrackbar3 != int(request.form.get("number3"))):
            #         controllers.adjustmentPanel.varTrackbar3 = int(
            #             request.form.get("number3"))

            # if (request.form.get("trackbar4") != None):
            #     if (controllers.adjustmentPanel.varTrackbar4 != int(request.form.get("trackbar4"))):
            #         controllers.adjustmentPanel.varTrackbar4 = int(
            #             request.form.get("trackbar4"))
            #     elif (controllers.adjustmentPanel.varTrackbar4 != int(request.form.get("number4"))):
            #         controllers.adjustmentPanel.varTrackbar4 = int(
            #             request.form.get("number4"))

            # if (request.form.get("trackbar5") != None):
            #     if (controllers.adjustmentPanel.varTrackbar5 != int(request.form.get("trackbar5"))):
            #         controllers.adjustmentPanel.varTrackbar5 = int(
            #             request.form.get("trackbar5"))
            #     elif (controllers.adjustmentPanel.varTrackbar5 != int(request.form.get("number5"))):
            #         controllers.adjustmentPanel.varTrackbar5 = int(
            #             request.form.get("number5"))

            # if (request.form.get("trackbar6") != None):
            #     if (controllers.adjustmentPanel.varTrackbar6 != int(request.form.get("trackbar6"))):
            #         controllers.adjustmentPanel.varTrackbar6 = int(
            #             request.form.get("trackbar6"))
            #     elif (controllers.adjustmentPanel.varTrackbar6 != int(request.form.get("number6"))):
            #         controllers.adjustmentPanel.varTrackbar6 = int(
            #             request.form.get("number6"))

            # if (request.form.get("trackbar_TamMinLv") != None):
            #     if (controllers.adjustmentPanel.varTrackbar_TamMinLv != int(request.form.get("trackbar_TamMinLv"))):
            #         controllers.adjustmentPanel.varTrackbar_TamMinLv = int(
            #             request.form.get("trackbar_TamMinLv"))
            #     elif (controllers.adjustmentPanel.varTrackbar_TamMinLv != int(request.form.get("number_TamMinLv"))):
            #         controllers.adjustmentPanel.varTrackbar_TamMinLv = int(
            #             request.form.get("number_TamMinLv"))

            # if (request.form.get("trackbar_TamMaxLv") != None):
            #     if (controllers.adjustmentPanel.varTrackbar_TamMaxLv != int(request.form.get("trackbar_TamMaxLv"))):
            #         controllers.adjustmentPanel.varTrackbar_TamMaxLv = int(
            #             request.form.get("trackbar_TamMaxLv"))
            #     elif (controllers.adjustmentPanel.varTrackbar_TamMaxLv != int(request.form.get("number_TamMaxLv"))):
            #         controllers.adjustmentPanel.varTrackbar_TamMaxLv = int(
            #             request.form.get("number_TamMaxLv"))

            # if (request.form.get("trackbar_TamMinLh") != None):
            #     if (controllers.adjustmentPanel.varTrackbar_TamMinLh != int(request.form.get("trackbar_TamMinLh"))):
            #         controllers.adjustmentPanel.varTrackbar_TamMinLh = int(
            #             request.form.get("trackbar_TamMinLh"))
            #     elif (controllers.adjustmentPanel.varTrackbar_TamMinLh != int(request.form.get("number_TamMinLh"))):
            #         controllers.adjustmentPanel.varTrackbar_TamMinLh = int(
            #             request.form.get("number_TamMinLh"))

            # if (request.form.get("trackbar_TamMaxLh") != None):
            #     if (controllers.adjustmentPanel.varTrackbar_TamMaxLh != int(request.form.get("trackbar_TamMaxLh"))):
            #         controllers.adjustmentPanel.varTrackbar_TamMaxLh = int(
            #             request.form.get("trackbar_TamMaxLh"))
            #     elif (controllers.adjustmentPanel.varTrackbar_TamMaxLh != int(request.form.get("number_TamMaxLh"))):
            #         controllers.adjustmentPanel.varTrackbar_TamMaxLh = int(
            #             request.form.get("number_TamMaxLh"))

            # if (request.form.get("trackbar_TamMin") != None):
            #     if (controllers.adjustmentPanel.varTrackbar_TamMin != int(request.form.get("trackbar_TamMin"))):
            #         controllers.adjustmentPanel.varTrackbar_TamMin = int(
            #             request.form.get("trackbar_TamMin"))
            #     elif (controllers.adjustmentPanel.varTrackbar_TamMin != int(request.form.get("number_TamMin"))):
            #         controllers.adjustmentPanel.varTrackbar_TamMin = int(
            #             request.form.get("number_TamMin"))

            # if (request.form.get("trackbar_TamMax") != None):
            #     if (controllers.adjustmentPanel.varTrackbar_TamMax != int(request.form.get("trackbar_TamMax"))):
            #         controllers.adjustmentPanel.varTrackbar_TamMax = int(
            #             request.form.get("trackbar_TamMax"))
            #     elif (controllers.adjustmentPanel.varTrackbar_TamMax != int(request.form.get("number_TamMax"))):
            #         controllers.adjustmentPanel.varTrackbar_TamMax = int(
            #             request.form.get("number_TamMax"))

            # if (request.form.get("trackbar_iterations_erode") != None):
            #     if (controllers.adjustmentPanel.varTrackbar_iterations_erode != int(request.form.get("trackbar_iterations_erode"))):
            #         controllers.adjustmentPanel.varTrackbar_iterations_erode = int(
            #             request.form.get("trackbar_iterations_erode"))
            #     elif (controllers.adjustmentPanel.varTrackbar_iterations_erode != int(request.form.get("number_iterations_erode"))):
            #         controllers.adjustmentPanel.varTrackbar_iterations_erode = int(
            #             request.form.get("number_iterations_erode"))

            # if (request.form.get("trackbar_iterations_dilate") != None):
            #     if (controllers.adjustmentPanel.varTrackbar_iterations_dilate != int(request.form.get("trackbar_iterations_dilate"))):
            #         controllers.adjustmentPanel.varTrackbar_iterations_dilate = int(
            #             request.form.get("trackbar_iterations_dilate"))
            #     elif (controllers.adjustmentPanel.varTrackbar_iterations_dilate != int(request.form.get("number_iterations_dilate"))):
            #         controllers.adjustmentPanel.varTrackbar_iterations_dilate = int(
            #             request.form.get("number_iterations_dilate"))

            # if (request.form.get("trackbar_LineHorizontal") != None):
            #     if (controllers.adjustmentPanel.varTrackbar_LineHorizontal != int(request.form.get("trackbar_LineHorizontal"))):
            #         controllers.adjustmentPanel.varTrackbar_LineHorizontal = int(
            #             request.form.get("trackbar_LineHorizontal"))
            #     elif (controllers.adjustmentPanel.varTrackbar_LineHorizontal != int(request.form.get("number_LineHorizontal"))):
            #         controllers.adjustmentPanel.varTrackbar_LineHorizontal = int(
            #             request.form.get("number_LineHorizontal"))

            # if (request.form.get("trackbar_LineVertical") != None):
            #     if (controllers.adjustmentPanel.varTrackbar_LineVertical != int(request.form.get("trackbar_LineVertical"))):
            #         controllers.adjustmentPanel.varTrackbar_LineVertical = int(
            #             request.form.get("trackbar_LineVertical"))
            #     elif (controllers.adjustmentPanel.varTrackbar_LineVertical != int(request.form.get("number_LineVertical"))):
            #         controllers.adjustmentPanel.varTrackbar_LineVertical = int(
            #             request.form.get("number_LineVertical"))

            # if (request.form.get("trackbar_LineRange") != None):
            #     if (controllers.adjustmentPanel.varTrackbar_LineRange != int(request.form.get("trackbar_LineRange"))):
            #         controllers.adjustmentPanel.varTrackbar_LineRange = int(
            #             request.form.get("trackbar_LineRange"))
            #     elif (controllers.adjustmentPanel.varTrackbar_LineRange != int(request.form.get("number_LineRange"))):
            #         controllers.adjustmentPanel.varTrackbar_LineRange = int(
            #             request.form.get("number_LineRange"))

            if (request.form.get("parameters_name") != None):
                controllers.adjustmentPanel.varname = request.form.get("parameters_name")
                print(controllers.adjustmentPanel.varname)

        return render_template("base.html",
                               nameParameters=nameParameters,
                               varname=controllers.adjustmentPanel.varname,
                               varTrackbar1=controllers.adjustmentPanel.varTrackbar1,
                               varTrackbar2=controllers.adjustmentPanel.varTrackbar2,
                               varTrackbar3=controllers.adjustmentPanel.varTrackbar3,
                               varTrackbar4=controllers.adjustmentPanel.varTrackbar4,
                               varTrackbar5=controllers.adjustmentPanel.varTrackbar5,
                               varTrackbar6=controllers.adjustmentPanel.varTrackbar6,

                               varTrackbar_TamMin=controllers.adjustmentPanel.varTrackbar_TamMin,
                               varTrackbar_TamMax=controllers.adjustmentPanel.varTrackbar_TamMax,

                               varTrackbar_TamMinLv=controllers.adjustmentPanel.varTrackbar_TamMinLv,
                               varTrackbar_TamMaxLv=controllers.adjustmentPanel.varTrackbar_TamMaxLv,
                               varTrackbar_TamMinLh=controllers.adjustmentPanel.varTrackbar_TamMinLh,
                               varTrackbar_TamMaxLh=controllers.adjustmentPanel.varTrackbar_TamMaxLh,

                               varTrackbar_iterations_erode=controllers.adjustmentPanel.varTrackbar_iterations_erode,
                               varTrackbar_iterations_dilate=controllers.adjustmentPanel.varTrackbar_iterations_dilate,

                               varTrackbar_LineHorizontal=controllers.adjustmentPanel.varTrackbar_LineHorizontal,
                               varTrackbar_LineVertical=controllers.adjustmentPanel.varTrackbar_LineVertical,
                               varTrackbar_LineRange=controllers.adjustmentPanel.varTrackbar_LineRange,

                               get_video_nameLayer01="Camada 01",
                               get_video_nameLayer02="Camada 02",
                               get_video_nameLayer03="Camada 03",
                               get_video_nameLayer04="Camada 04",
                               get_video_nameLayer05="Camada 05",
                               get_video_nameLayer06="Camada 06"
                               )

    @app.route("/base2", methods=["GET"])
    def base2():
        return render_template("base2.html", get_video_nameLayer03="Camada 03")

    @app.route("/printPointsCoordinates", methods=["GET", "POST"])
    def console():
        return render_template("public/printPointsCoordinates.html",
                               varOutputItemCoordinatesVector=controllers.frames.outputItemCoordinatesVector
                               )

    @app.route("/videolayer01")
    def videolayer01():
        print("chamada de rota videolayer01")
        return Response(controllers.controller.generate_FrameLayer01("videolayer01"),
                        mimetype="multipart/x-mixed-replace; boundary=videolayer01")

    @app.route("/videolayer02")
    def videolayer02():
        return Response(controllers.controller.generate_FrameLayer02("videolayer02"),
                        mimetype="multipart/x-mixed-replace; boundary=videolayer02")

    @app.route("/videolayer03")
    def videolayer03():
        return Response(controllers.controller.generate_FrameLayer03("videolayer03"),
                        mimetype="multipart/x-mixed-replace; boundary=videolayer03")

    @app.route("/videolayer04")
    def videolayer04():
        return Response(controllers.controller.generate_FrameLayer04("videolayer04"),
                        mimetype="multipart/x-mixed-replace; boundary=videolayer04")

    @app.route("/videolayer05")
    def videolayer05():
        return Response(controllers.controller.generate_FrameLayer05("videolayer05"),
                        mimetype="multipart/x-mixed-replace; boundary=videolayer05")

    @app.route("/form-salvar", methods=["get"])
    def formsalvar():
        Insert_parametersAdjustFilterImg.salvar()
        return render_template('base.html')