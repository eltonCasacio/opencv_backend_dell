import cv2
import imutils
import numpy as np
import controllers.adjustmentPanel
import controllers.frames
import controllers.plc
from services.clearPixelNoise import clearPixelLine, clearPixelColum


#
# Fonts
#
font = cv2.FONT_HERSHEY_SIMPLEX

#
# List of coordinate Partial
#
listCoordinatePartial = []

#
# Comunication PLC
#
# controllers.plc.comunicationPlc()


def detect_motion(cap):
    print("thread detect_motion chamada")

    def convertPixelToMm_X(pxX):
        return pxX * 1.04

    def convertPixelToMm_Y(pxY):
        return pxY * 1.1225

    def convertMmToPixel_X(mmX):
        return mmX / 1.04

    def convertMmToPixel_Y(mmY):
        return mmY / 1.1225

    def convertPixelToMm(Px):
        return Px * 1.0

    def convertMmToPixel(mm):
        return mm / 1.0

    def calculateGreatestLineDistanceInRectangle(retangulo):
        coordenadas_x = [ponto[0] for ponto in retangulo]
        coordenadas_y = [ponto[1] for ponto in retangulo]
        distancia_x = max(coordenadas_x) - min(coordenadas_x)
        distancia_y = max(coordenadas_y) - min(coordenadas_y)
        return distancia_x, distancia_y

    def calcular_inclinacao(retangulo):

        reta01 = [retangulo[0], retangulo[1]]

        x1, y1 = reta01[0]
        x2, y2 = reta01[1]

        return (y2 - y1) / (x2 - x1)

    def checkingBoxSize(boxYellow, topAndBottomLine, sideLine, range):

        lineX, lineY = calculateGreatestLineDistanceInRectangle(boxYellow)

        withinRange = ((lineX <= topAndBottomLine + range)
                       and (lineX >= topAndBottomLine - range)
                       and (lineY <= sideLine + range)
                       and (lineY >= sideLine - range)
                       )

        return withinRange, lineX, lineY

    def findTheCenter(forma_geometrica):
        soma_x = 0
        soma_y = 0

        for ponto in forma_geometrica:
            soma_x += ponto[0]
            soma_y += ponto[1]

        centro_x = int(soma_x / len(forma_geometrica))
        centro_y = int(soma_y / len(forma_geometrica))

        return centro_x, centro_y

    def orderCoordenates():
        listCoordinatePartial.sort()

    def dibujar(mask, color):

        listCoordinatePartial.clear()

        controllers.plc.Id_Det = 0

        contornos = cv2.findContours(
            mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        counterContornos = 0
        for c in contornos:
            area = cv2.contourArea(c)
            counterContornos = counterContornos + 1
            if len(c) > 0:
                if (area > controllers.adjustmentPanel.varTrackbar_TamMin
                        and area < controllers.adjustmentPanel.varTrackbar_TamMax):

                    rectYellow = cv2.minAreaRect(c)
                    boxYellow = cv2.boxPoints(rectYellow)
                    boxYellow = np.int0(boxYellow)
                    if (controllers.adjustmentPanel.varTrackbar_LineHorizontal > 0
                        and controllers.adjustmentPanel.varTrackbar_LineVertical > 0
                            and controllers.adjustmentPanel.varTrackbar_LineRange > 0):

                        checkingBoxSize_r_withinRange, withinRange_r_line01, withinRange_r_line02 = checkingBoxSize(
                            boxYellow,
                            controllers.adjustmentPanel.varTrackbar_LineHorizontal,
                            controllers.adjustmentPanel.varTrackbar_LineVertical,
                            controllers.adjustmentPanel.varTrackbar_LineRange)

                        if (checkingBoxSize_r_withinRange):

                            x, y = findTheCenter(boxYellow)

                            # Console.print("X{:0>2}/Y{:0>2}".format(x, y))

                            cv2.circle(frame, (x, y), 7, (0, 255, 0), -1)
                            cv2.drawContours(
                                frame, [boxYellow], 0, (0, 255, 255), 2)

                            px = x - 200
                            py = y - 200
                            mmX = convertPixelToMm_X(px)
                            mmY = convertPixelToMm_Y(py)

                            controllers.plc.Id_Det += 1

                            cv2.putText(frame,
                                        'IdD{:0>2}'.format(
                                            controllers.plc.Id_Det),
                                        (x - 30, y - 20), font, 0.35, (255, 0, 255), 1, cv2.LINE_AA)

                            cv2.putText(frame,
                                        'cX{:.2f}/cY{:.2f}'.format(mmX, mmY),
                                        (x - 30, y - 10), font, 0.35, (0, 255, 0), 1, cv2.LINE_AA)

                            mmL1 = convertPixelToMm_X(withinRange_r_line01)
                            mmL2 = convertPixelToMm_Y(withinRange_r_line02)

                            cv2.putText(frame,
                                        'lX{:.2f}/lY{:.2f}'.format(mmL1, mmL2),
                                        (x - 30, y + 10), font, 0.35, (0, 0, 255), 1, cv2.LINE_AA)

                            inclinacao = calcular_inclinacao(boxYellow)

                            cv2.putText(frame,
                                        'g{:.2f}'.format(inclinacao),
                                        (x - 20, y + 20), font, 0.35, (0, 0, 255), 1, cv2.LINE_AA)

                            mmRobo_X = mmX + controllers.plc.HMI_O_AR_AxisCommandPos_01
                            mmRobo_Y = mmY + controllers.plc.HMI_O_AR_AxisCommandPos_02

                            cv2.putText(frame,
                                        'rX{:.2f}/rY{:.2f}'.format(
                                            mmRobo_X, mmRobo_Y),
                                        (x - 10, y + 30), font, 0.35, (255, 0, 255), 1, cv2.LINE_AA)

                            listCoordinatePartial.append([mmRobo_X, mmRobo_Y,
                                                          mmX, mmY,
                                                          px, py,
                                                          controllers.plc.Id_trigger,
                                                          controllers.plc.Id_Det])

                    else:
                        MYellow = cv2.moments(c)
                        x = int(MYellow["m10"] / MYellow["m00"])
                        y = int(MYellow["m01"] / MYellow["m00"])
                        cv2.circle(frame, (x, y), 7, (0, 255, 0), -1)
                        cv2.drawContours(
                            frame, [boxYellow], 0, (0, 255, 255), 2)
                        # print("N: {} / X: {} / Y: {}".format(
                        # counterContornos,
                        # x, y))

                        checkingBoxSize_r_withinRange, withinRange_r_line01, withinRange_r_line02 = checkingBoxSize(
                            boxYellow,
                            controllers.adjustmentPanel.varTrackbar_LineHorizontal,
                            controllers.adjustmentPanel.varTrackbar_LineVertical,
                            controllers.adjustmentPanel.varTrackbar_LineRange)

                        # cv2.putText(frame,
                        # 'cX{:.2f}}/cY{:.2f}'.format(x,y),
                        # (x+10,y), font, 0.35,(0,255,0),1,cv2.LINE_AA)

                        cv2.putText(frame,
                                    'lX{:.2f}/lY{:.2f}'.format(
                                        withinRange_r_line01, withinRange_r_line02),
                                    (x + 10, y + 15), font, 0.35, (0, 0, 255), 1, cv2.LINE_AA)

                        listCoordinatePartial.append([x, y])

        if (controllers.plc.CP_O_TriggerCamera and not controllers.plc.CP_I_TriggerCamera_Return_OK):
            controllers.plc.Id_trigger += 1

            print('DM - #01 Executano processo TriggerCamera')
            orderCoordenates()

            print('DM - #01 (Lista Ordenada)')
            print(listCoordinatePartial)
            controllers.plc.ListCoordenate(listCoordinatePartial)

            print('DM - #01 Trigger camera return OK')
            controllers.plc.mWrite_TriggerReturnOK()
            controllers.plc.CP_I_TriggerCamera_Return_OK = True

    while (True):

        # time.sleep(1)
        noneFrame = any

        _, frame = cap.read()
        # frame_dibujar 		= frame.copy()
        # frame = cv2.imread("./testeCut.jpg")

        l_h = controllers.adjustmentPanel.varTrackbar1
        l_s = controllers.adjustmentPanel.varTrackbar2
        l_v = controllers.adjustmentPanel.varTrackbar3
        u_h = controllers.adjustmentPanel.varTrackbar4
        u_s = controllers.adjustmentPanel.varTrackbar5
        u_v = controllers.adjustmentPanel.varTrackbar6

        lower = np.array([l_h, l_s, l_v])
        upper = np.array([u_h, u_s, u_v])

        frame = imutils.resize(frame, width=400, height=400)
        frame = cv2.erode(frame,
                          None,
                          iterations=controllers.adjustmentPanel.varTrackbar_iterations_erode)
        # hsv 	= cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mask = cv2.inRange(frame, lower, upper)
        # result 	= cv2.bitwise_and(frame, frame, mask=mask)

        # camada_erode = cv2.erode(mask, None, iterations=0)
        # camada_dilate = cv2.dilate(mask, None, iterations=0)

        cutLine = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)
        clearPixelLine.cutLineBySize(cutLine,
                                     controllers.adjustmentPanel.varTrackbar_TamMinLv,
                                     controllers.adjustmentPanel.varTrackbar_TamMaxLv)
        clearPixelColum.cutColumBySize(cutLine,
                                       controllers.adjustmentPanel.varTrackbar_TamMinLh,
                                       controllers.adjustmentPanel.varTrackbar_TamMaxLh)

        dbj = cv2.cvtColor(cutLine, cv2.COLOR_BGR2GRAY)
        dibujar(dbj, (255, 0, 0))  # mask

        controllers.frames.changeState_outputVideoLayer01(mask)
        controllers.frames.changeState_outputVideoLayer02(dbj)
        controllers.frames.changeState_outputVideoLayer03(frame)
        controllers.frames.changeState_outputVideoLayer04(noneFrame)
        controllers.frames.changeState_outputVideoLayer05(noneFrame)
