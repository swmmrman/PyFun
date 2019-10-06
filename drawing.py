"""This is a string"""
import pyautogui
# from time import sleep


def draw_spiral(startLen, stepSize):
    """Blah blah.  Here a string"""
    step = startLen
    while step > stepSize:
        pyautogui.dragRel(step, 0)
        step -= stepSize
        pyautogui.dragRel(0, step)
        pyautogui.dragRel(-step, 0)
        step -= stepSize
        pyautogui.dragRel(0, -step)


def dot_matrix(start_pos, dot_spacing, box_size):
    """Blah blah.  Here a string"""
    try:
        (xlen, ylen) = box_size
        (xstart, ystart) = start_pos
        if xlen % 2 != 0:
            xlen -= 1
        if ylen % 2 != 0:
            ylen -= 1
        pyautogui.moveTo(xstart, ystart)
        pyautogui.click()
        distance = 0
        while xlen >= dot_spacing and ylen >= dot_spacing:
            while distance < xlen:
                pyautogui.moveRel(dot_spacing, 0)
                pyautogui.click()
                distance += dot_spacing
            xlen -= dot_spacing
            distance = 0
            while distance < ylen:
                pyautogui.moveRel(0, dot_spacing)
                pyautogui.click()
                distance += dot_spacing
            ylen -= dot_spacing
            distance = 0
            while distance < xlen:
                pyautogui.moveRel(-dot_spacing, 0)
                pyautogui.click()
                distance += dot_spacing
            xlen -= dot_spacing
            distance = 0
            while distance < ylen:
                pyautogui.moveRel(0, -dot_spacing)
                pyautogui.click()
                distance += dot_spacing
            distance = 0
            ylen -= dot_spacing
    except KeyboardInterrupt:
        print("ok\n")


dot_matrix(((1920/1.3), 70), 2, (50, 50))
