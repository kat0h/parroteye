import PySimpleGUI as sg
import pyautogui


def get_cursorpos():
    return pyautogui.position()


def get_winpos(window):
    return window.CurrentLocation()


sg.theme('Default1')

layout = [
        [sg.T(size=(20, 1), justification='center', key='-mousepos-')],
        [sg.T(size=(20, 1), justification='center', key='-winpos-')],
        ]

window = sg.Window('Watch', layout)

while True:
    event, values = window.read(timeout=1000/60, timeout_key='-timeout-')

    if event in (None,):
        break
    elif event in '-timeout-':
        window['-mousepos-'].update(get_cursorpos())
        window['-winpos-'].update(get_winpos(window))
