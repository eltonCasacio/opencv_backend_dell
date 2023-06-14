import threading
from pycomm3 import LogixDriver

from rich.console import Console
from rich.table import Table

listCoordinateAll = []

#
# Console Teminal Rich
#
console = Console()
console.print("Terminal OpenCV", "Root", style="bold white on blue")

table = Table(show_header=True, header_style="bold magenta")

table.add_column("R Xmm", justify="right")
table.add_column("R Ymm", justify="right")

table.add_column("C Xmm", justify="right")
table.add_column("C Ymm", justify="right")

table.add_column("C Xp", justify="right")
table.add_column("C Yp", justify="right")

table.add_column("ID Trig", justify="right")
table.add_column("ID Det", justify="right")

#
#
#
Id_trigger = 0
Id_Det = 0

#
# Read general variable do PLC.
#
NW_I_IA01_Calc_ConvDistanceToHeight = 0
NW_I_IA01_Calc_Value_Unit = 0
Recipe_Pallet_HiveMatrix_CounterPosition = 0
HMI_O_AR_AxisCommandPos_01 = 0.0
HMI_O_AR_AxisCommandPos_02 = 0.0
HMI_O_AR_AxisCommandPos_03 = 0.0

HMI_I_ImgAna_DistToolCamera_X = 0.0
HMI_I_ImgAna_DistToolCamera_Y = 0.0

CounterPositionCoordenate = 0

#
# Read comunication with system vision computer - CP
#
CP_O_ListCoordinateClear = False
CP_O_ListCoordinateClearOK_Received = False

CP_O_TriggerCamera = False
CP_O_ReturnOK_Received = False

#
# Write comunication with system vision computer - CP
#
CP_I_ListCoodinateClear_Return_OK = False

CP_I_TriggerCamera_Return_OK = False

#
# Analysis system asking to write information
#
# comunication Trigger
Write_TriggerReturn = False


def sortSecond(val):
    return val[1]


def ListCoordenate(listCoordinate):
    # listCoordinateAll.append(listCoordinate.copy())
    global listCoordinateAll
    aux = listCoordinateAll.copy()
    if (len(listCoordinateAll) <= 0):
        listCoordinateAll = listCoordinate.copy()
    else:
        listCoordinateAll = aux + listCoordinate.copy()

    listCoordinateAll.sort(key=sortSecond)
    # print('(List Coordinate All)')
    # print(listCoordinateAll)

    for row in listCoordinateAll:
        console.print((
            " / R Xmm: {:0>7} "
            " / R Ymm: {:0>7} "
            " / C Xmm: {:0>7} "
            " / C Ymm: {:0>7} "
            " / C Xp: {:0>7} "
            " / C Yp: {:0>7} "
            " / ID Trig: {:0>7} "
            " / ID Det: {:0>7} ").format(
            round(row[0], 2),
            round(row[1], 2),
            round(row[2], 2),
            round(row[3], 2),
            round(row[4], 2),
            round(row[5], 2),
            round(row[6], 2),
            round(row[7], 2),
        ), style="bold on black")


def mWrite_TriggerReturnOK():
    global Write_TriggerReturn
    Write_TriggerReturn = True


def thr_comunicationPlc():
    with LogixDriver('192.168.11.5') as micro850:
        while (True):
            #
            # Read information comunication PLC
            #
            #
            # Read mananger information
            #
            global NW_I_IA01_Calc_ConvDistanceToHeight
            global NW_I_IA01_Calc_Value_Unit
            NW_I_IA01_Calc_ConvDistanceToHeight = micro850.read(
                'NW_I_IA01_Calc_ConvDistanceToHeight').value
            NW_I_IA01_Calc_Value_Unit = micro850.read(
                'NW_I_IA01_Calc_Value_Unit').value

            global HMI_O_AR_AxisCommandPos_01
            global HMI_O_AR_AxisCommandPos_02
            global HMI_O_AR_AxisCommandPos_03
            HMI_O_AR_AxisCommandPos_01 = micro850.read(
                'HMI_O_AR_AxisCommandPos_01').value
            HMI_O_AR_AxisCommandPos_02 = micro850.read(
                'HMI_O_AR_AxisCommandPos_02').value
            HMI_O_AR_AxisCommandPos_03 = micro850.read(
                'HMI_O_AR_AxisCommandPos_03').value

            global HMI_I_ImgAna_DistToolCamera_X
            global HMI_I_ImgAna_DistToolCamera_Y
            HMI_I_ImgAna_DistToolCamera_X = micro850.read(
                'HMI_I_ImgAna_DistToolCamera_X').value
            HMI_I_ImgAna_DistToolCamera_Y = micro850.read(
                'HMI_I_ImgAna_DistToolCamera_Y').value

            global Recipe_Pallet_HiveMatrix_CounterPosition
            Recipe_Pallet_HiveMatrix_CounterPosition = micro850.read(
                'Recipe_Pallet_HiveMatrix_CounterPosition').value

            #
            # Write information comunication PLC
            #
            # Write_Coordenate
            #
            global CounterPositionCoordenate
            CounterPositionCoordenate = Recipe_Pallet_HiveMatrix_CounterPosition
            if (len(listCoordinateAll) > 0
                    and CounterPositionCoordenate < len(listCoordinateAll)):
                Write_Coordenate_x = ((listCoordinateAll[CounterPositionCoordenate][0])
                                      + HMI_I_ImgAna_DistToolCamera_X)
                Write_Coordenate_y = ((listCoordinateAll[CounterPositionCoordenate][1])
                                      + HMI_I_ImgAna_DistToolCamera_Y)
                micro850.write('CP_I_ImgAna_Xmm', Write_Coordenate_x)
                micro850.write('CP_I_ImgAna_Ymm', Write_Coordenate_y)

            #
            # Cycle automatic - Read / Write
            #
            #
            # Sequence Clear List Coordinate
            #
            # Seq. 01 - Waiting to receive list coodinate clear and clear list
            global CP_O_ListCoordinateClear
            CP_O_ListCoordinateClear = micro850.read(
                'CP_O_ListCoordinateClear').value

            global CP_I_ListCoodinateClear_Return_OK
            if (CP_O_ListCoordinateClear):
                console.print(
                    "#Seq 01 - Clear list coordinate all", style="magenta")
                listCoordinateAll.clear()
                CP_I_ListCoordinateClear_Return_OK = True
                micro850.write('CP_I_ListCoordinateClear_Return_OK',
                               CP_I_ListCoordinateClear_Return_OK)

            #
            # Seq. 02 - Send return list coodinate clear
            #
            global CP_O_ListCoordinateClearOK_Received
            CP_O_ListCoordinateClearOK_Received = micro850.read(
                'CP_O_ListCoordinateClearOK_Received').value

            if (CP_O_ListCoordinateClearOK_Received):
                console.print("#Seq 02 - Clear list - ReturnOK",
                              style="magenta")
                CP_I_ListCoordinateClear_Return_OK = False
                micro850.write('CP_I_ListCoordinateClear_Return_OK',
                               CP_I_ListCoordinateClear_Return_OK)

            #
            # Sequence Trigger
            #
            #
            # Seq. 01 - Waiting to receive trigger camera - Read trigger camera
            #
            global CP_O_TriggerCamera
            CP_O_TriggerCamera = micro850.read('CP_O_TriggerCamera').value

            #
            # Seq. 02 - Send return trigger - Write Trigger Return
            #
            global CP_I_TriggerCamera_Return_OK
            global Write_TriggerReturn
            if (Write_TriggerReturn):
                print('PLC - #02 Write Trigger Return')
                micro850.write('CP_I_TriggerCamera_Return_OK',
                               CP_I_TriggerCamera_Return_OK)
                Write_TriggerReturn = False

            #
            # Seq. 03 - Waiting to receive data signal received from PLC. - Read Return OK Received
            #
            global CP_O_ReturnOK_Received
            CP_O_ReturnOK_Received = micro850.read(
                'CP_O_ReturnOK_Received').value
            if (CP_O_ReturnOK_Received):
                print('PLC - #03 Rceived return OK')
                CP_I_TriggerCamera_Return_OK = False
                micro850.write('CP_I_TriggerCamera_Return_OK',
                               CP_I_TriggerCamera_Return_OK)


def comunicationPlc():
    t = threading.Thread(target=thr_comunicationPlc)
    t.daemon = True
    t.start()
