import pyautogui

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
ordersProcessed = 0
ordersList = []

while True:
	
	# Store the order number and serial number to a list.
	orderNum = str.lower(input('Ready? Scan order number and press enter '))
	serialNum = str.lower(input('Now scan serial number of the terminal, and press enter '))
	ordersList.append(orderNum)
	ordersList.append(serialNum) 
	# Write the order number and serial number to a text file for later use.
	orderFile = open('orderList.txt', 'a')
	orderFile.write(orderNum)
	orderFile.write('\n')
	orderFile.write(serialNum)
	orderFile.write('\n')
	orderFile.close()
	print('Orders processed today = ' , ordersProcessed)
	#print(ordersList)
	ordersProcessed += 1 
	pyautogui.click(563, 327, button='left') 
	pyautogui.PAUSE = 2
	pyautogui.doubleClick(749, 371, button= 'left' ) 
	pyautogui.PAUSE = 3
	pyautogui.click(858, 781, button='left') 
	pyautogui.PAUSE = 3
	pyautogui.doubleClick(535, 397, button= 'left' )
	if pyautogui.pixelMatchesColor(523, 515, (0, 0, 0)) == True:
		pyautogui.PAUSE = 3
		pyautogui.click(505, 766, button='left')
		if pyautogui.pixelMatchesColor(558, 524, (0, 0, 0)) != True:
			pyautogui.click(522, 1031, button='left')
			print('THIS ORDER IS STILL OPEN OR IS MISSING A TRACKING NUMBER')
			print('THIS ORDER IS STILL OPEN OR IS MISSING A TRACKING NUMBER')
			print('THIS ORDER IS STILL OPEN OR IS MISSING A TRACKING NUMBER')
			userInput = str.lower(input('Ready? Press Enter to continue '))
		pyautogui.PAUSE = 3
		pyautogui.click(942, 698, button='left')
		pyautogui.PAUSE = 3
		pyautogui.click(1342, 293, button='left')
		pyautogui.PAUSE = 3
		pyautogui.click(522, 1031, button='left')
	else:
		pyautogui.PAUSE = 3
		pyautogui.click(633, 830, button='left') 
		if pyautogui.pixelMatchesColor(446, 509, (0, 0, 0)) != True:
			pyautogui.click(522, 1031, button='left')
			print('THIS ORDER IS STILL OPEN OR IS MISSING A TRACKING NUMBER')
			print('THIS ORDER IS STILL OPEN OR IS MISSING A TRACKING NUMBER')
			print('THIS ORDER IS STILL OPEN OR IS MISSING A TRACKING NUMBER')
			userInput = str.lower(input('Ready? Press Enter to continue '))
		pyautogui.PAUSE = 3
		pyautogui.click(883, 684, button='left') 
		pyautogui.PAUSE = 3
		pyautogui.click(1477, 368, button='left') 
		pyautogui.PAUSE = 3
		pyautogui.click(522, 1031, button='left')
	