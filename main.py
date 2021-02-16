import math
import PySimpleGUI as sg
import pyautogui


def get_cursorpos():
    return pyautogui.position()


def get_winpos(window):
    pos = window.CurrentLocation()
    ret = []
    ret.append(pos[0] + window.Size[0] // 2)
    ret.append(pos[1] + window.Size[1] // 2)
    return ret


def calc_angle(x, y, x2, y2):
    angle = math.degrees(-math.atan2(y2-y, x2-x))
    return angle if angle > 0 else angle + 360


sg.theme('Default1')

layout = [
        [sg.Image(key='-image-')],
        ]

window = sg.Window('Parroteye', layout)

images = [
        './img/0.gif',
        './img/1.gif',
        './img/2.gif',
        './img/3.gif',
        './img/4.gif',
        './img/5.gif',
        './img/6.gif',
        './img/7.gif',
        './img/8.gif',
        './img/9.gif',
        ]
while True:
    event, values = window.read(timeout=1000/60, timeout_key='-timeout-')

    if event in (None,):
        break
    elif event in '-timeout-':
        cursorpos = get_cursorpos()
        winpos = get_winpos(window)
        angle = calc_angle(winpos[0], winpos[1], cursorpos[0], cursorpos[1])
        window['-image-'].update(images[int((angle-1)//36)])
