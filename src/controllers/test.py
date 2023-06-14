from rich.console import Console

console = Console()


def patternTheFourCornersOfTheSquare(boxYellow):

    boxPattern = [[0, 0], [0, 0], [0, 0], [0, 0]]

    strCondition = ""
    strConditionX = ""
    strConditionY = ""

    for nXY in boxYellow:

        console.rule("X: {:0>2} / Y: {:0>2}".format(nXY[0], nXY[1]))

        vn = 0

        while (vn < 4):
            strCondition = ""
            strConditionX = ""
            strConditionY = ""

            # 01
            if ((nXY[0] < boxYellow[vn][0]) & (nXY[1] < boxYellow[vn][1])):
                boxPattern[0][0] = nXY[0]
                boxPattern[0][1] = nXY[1]

                strCondition += "F01"
                strConditionX += "<"
                strConditionY += "<"

            # 02
            if ((nXY[0] > boxYellow[vn][0]) & (nXY[1] < boxYellow[vn][1])):
                boxPattern[1][0] = nXY[0]
                boxPattern[1][1] = nXY[1]

                strCondition += "F02"
                strConditionX += ">"
                strConditionY += "<"

            # 03
            if ((nXY[0] > boxYellow[vn][0]) & (nXY[1] > boxYellow[vn][1])):
                boxPattern[2][0] = nXY[0]
                boxPattern[2][1] = nXY[1]

                strCondition += "F03"
                strConditionX += ">"
                strConditionY += ">"

            # 04
            if ((nXY[0] < boxYellow[vn][0]) & (nXY[1] > boxYellow[vn][1])):
                boxPattern[3][0] = nXY[0]
                boxPattern[3][1] = nXY[1]

                strCondition += "F04"
                strConditionX += "<"
                strConditionY += ">"

            console.print(("Vn:{:0>2}"
                           "|STR:{:0>3}"
                           "|X:{:0>2} - {:#>1} - X:{:0>2}"
                           "|Y:{:0>2} - {:#>1} - Y:{:0>2}").format(
                vn,
                strCondition,
                nXY[0], strConditionX, boxYellow[vn][0],
                nXY[1], strConditionY, boxYellow[vn][1],
            ))

            vn += 1

    return boxPattern


# boxYellow = [[10,10],[20,10],[20,20],[10,20]]
# boxYellow = [[20,10],[10,10],[10,20],[20,20]]
boxYellow = [[11, 10], [20, 10], [20, 20], [13, 20]]

console.print(patternTheFourCornersOfTheSquare(boxYellow))
