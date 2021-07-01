def create(options, active_window):
    import os
    import time
    import keyboard
    import win32gui
    global menu_position
    global menu_pressed
    global menu_options
    global menu_active_window
    os.system('HideCursor.bat 0')
    print('\u001B[1A', end='\r')
    menu_active_window = active_window
    menu_options = options
    menu_position = 0
    menu_pressed = False
    # keyboard on_press_key doesnt allow passing arguments
    # so have to use global -_-

    def process_key(key):
        global menu_position
        global menu_pressed
        global menu_options
        global menu_active_window
        if win32gui.GetForegroundWindow() == menu_active_window:
            if key.scan_code == 72:
                menu_position -= 1
            elif key.scan_code == 80:
                menu_position += 1
            elif key.scan_code == 28:
                menu_pressed = True

            if menu_position > len(menu_options)-1:
                menu_position = 0
            if menu_position < 0:
                menu_position = len(menu_options)-1
        else:
            keyboard.send(key.scan_code)

    h72 = keyboard.on_press_key('up', process_key, suppress=True)  # up
    h80 = keyboard.on_press_key('down', process_key, suppress=True)  # down
    henter = keyboard.on_press_key(
        'enter', process_key, suppress=True)  # enter

    while True:
        time.sleep(0.05)

        for i in range(0, len(menu_options)):
            if i == menu_position:
                print(' -> ' + str(menu_options[i]))
            else:
                print('    ' + str(menu_options[i]) + '   ')

        if menu_pressed:
            os.system('HideCursor.bat 1')
            print('\u001B[1A', end='\r')
            keyboard.unhook(h72)
            keyboard.unhook(h80)
            keyboard.unhook(henter)
            return (menu_options[menu_position], menu_position)

        print('\u001B[' + str(len(menu_options)) + 'A', end='\r')
