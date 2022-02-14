number = 0

def on_button_pressed_a():
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global number
    number = randint(1, 6)
    if number == 1:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
    elif number == 2:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        # . . . #
                        . . . . .
                        . . . . .
        """)
    elif number == 3:
        basic.show_leds("""
            . . . . #
                        . . . . .
                        . . # . .
                        . . . . .
                        # . . . .
        """)
    elif number == 4:
        basic.show_leds("""
            # . . . #
                        . . . . .
                        . . . . .
                        . . . . .
                        # . . . #
        """)
    elif number == 5:
        basic.show_leds("""
            # . . . #
                        . . . . .
                        . . # . .
                        . . . . .
                        # . . . #
        """)
    else:
        basic.show_leds("""
            # . . . #
                        . . . . .
                        # . . . #
                        . . . . .
                        # . . . #
        """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
