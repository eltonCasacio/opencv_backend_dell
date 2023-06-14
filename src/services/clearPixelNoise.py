from services.pixel import *

def checkIfTheColorIsWhite(img, x, y):
	azul, verde, vermelho = pixelColor.getColor(img, x, y)
	return (azul >= 250) and (verde >= 250) and (vermelho >= 250)

def checkIfTheColorIsBlack(img, x, y):
	azul, verde, vermelho = pixelColor.getColor(img, x, y)
	return (azul >= 0) and (verde >= 0) and (vermelho >= 0)

def checkIfSizeOfItem(countTheSizeOfTheFoundItem, minimumSizeOfItemFound, maximumSizeOfItemFound):
	return (	countTheSizeOfTheFoundItem <= maximumSizeOfItemFound
			and countTheSizeOfTheFoundItem >= minimumSizeOfItemFound)

def setPixelLineAsList(img, x_Start, x_End, y):
	while (x_Start < x_End):
		pixelColor.setColor(img, x_Start, y, 0, 0, 0) #setColor(img, x_Start, y, 255, 0, 0) azul
		x_Start = x_Start + 1

def setPixelColumnAsList(img, y_Start, y_End, x):
	while (y_Start < y_End):
		pixelColor.setColor(img, x, y_Start, 0, 0, 0) #setColor(img, x_Start, y, 255, 0, 0) azul
		y_Start = y_Start + 1

class clearPixelLine:
    def cutLineBySize(img, minimumSizeVerticalLine, maximumSizeVerticalLine):
        minimumSizeOfItemFound 		= minimumSizeVerticalLine
        maximumSizeOfItemFound 		= maximumSizeVerticalLine
        countTheSizeOfTheFoundItem 	= 0
        y_insideTheWhite			= False
        y_start 					= 0
        y_end 						= 0

        altura, largura, cor = img.shape

        for x in range(0, largura):
            y_insideTheWhite			= False
            y_start 					= 0
            y_end						= 0
            countTheSizeOfTheFoundItem 	= 0

            for y in range (0, altura):

                if (#checkIfTheColorIsBlack(img, x, y)
                     checkIfTheColorIsWhite(img, x, y)
                     ):
                    countTheSizeOfTheFoundItem = countTheSizeOfTheFoundItem + 1
                    
                    if (not y_insideTheWhite):
                        y_insideTheWhite 	= True
                        y_start 			= y

                    if (y >= largura - 1 and y_insideTheWhite):
                        y_insideTheWhite 	= False	
                        if (checkIfSizeOfItem(countTheSizeOfTheFoundItem, minimumSizeOfItemFound, maximumSizeOfItemFound)):
                            y_end						= y
                            setPixelColumnAsList(img, y_start, y_end, x)

                        y_start 					= 0
                        y_end						= 0
                        countTheSizeOfTheFoundItem 	= 0


                else:
                    if (y_insideTheWhite):
                        y_insideTheWhite 	= False	
                        if (checkIfSizeOfItem(countTheSizeOfTheFoundItem, minimumSizeOfItemFound, maximumSizeOfItemFound)):
                            y_end						= y
                            setPixelColumnAsList(img, y_start, y_end, x)

                        y_start 					= 0
                        y_end						= 0
                        countTheSizeOfTheFoundItem 	= 0

class clearPixelColum:
    def cutColumBySize(img, minimumSizehorizontalLine, maximumSizeHorizontalLine):
        minimumSizeOfItemFound 		= minimumSizehorizontalLine
        maximumSizeOfItemFound 		= maximumSizeHorizontalLine
        countTheSizeOfTheFoundItem 	= 0
        x_insideTheWhite			= False
        x_start 					= 0
        x_end 						= 0

        altura, largura, cor = img.shape

        for y in range(0, altura):
            x_insideTheWhite			= False
            x_start 					= 0
            x_end						= 0
            countTheSizeOfTheFoundItem 	= 0

            for x in range (0, largura):

                if (checkIfTheColorIsWhite(img, x, y)):
                    countTheSizeOfTheFoundItem = countTheSizeOfTheFoundItem + 1
                    
                    if (not x_insideTheWhite):
                        x_insideTheWhite 	= True
                        x_start 			= x

                    if (x >= largura - 1 and x_insideTheWhite):
                        x_insideTheWhite 	= False	
                        if (checkIfSizeOfItem(countTheSizeOfTheFoundItem, minimumSizeOfItemFound, maximumSizeOfItemFound)):
                            x_end						= x
                            setPixelLineAsList(img, x_start, x_end, y)

                        x_start 					= 0
                        x_end						= 0
                        countTheSizeOfTheFoundItem 	= 0


                else:
                    if (x_insideTheWhite):
                        x_insideTheWhite 	= False	
                        if (checkIfSizeOfItem(countTheSizeOfTheFoundItem, minimumSizeOfItemFound, maximumSizeOfItemFound)):
                            x_end						= x
                            setPixelLineAsList(img, x_start, x_end, y)

                        x_start 					= 0
                        x_end						= 0
                        countTheSizeOfTheFoundItem 	= 0

