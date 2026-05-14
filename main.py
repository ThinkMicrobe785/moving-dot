def on_button_pressed_a():
    global PlatformX
    PlatformX += -1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global PlatformX
    PlatformX += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

PlatformX = 2
BallX = 3
BallY = 0
BallMoveX = 1
BallMoveY = 1

def on_forever():
    global PlatformX
    if BallY < 5:
        if PlatformX > 3:
            PlatformX = 3
        if PlatformX < 0:
            PlatformX = 0
        led.unplot(PlatformX - 1, 4)
        led.unplot(PlatformX + 2, 4)
        led.plot(PlatformX, 4)
        led.plot(PlatformX + 1, 4)
    else:
        basic.show_string("GAME OVER")
basic.forever(on_forever)

def on_every_interval():
    global BallMoveY, BallY, BallX, BallMoveX
    if (BallX == PlatformX or BallX == PlatformX + 1) and BallY == 3:
        BallMoveY = BallMoveY * -1
    elif (BallX + BallMoveX == PlatformX or BallX + BallMoveX == PlatformX + 1) and BallY == 3:
        led.unplot(BallX, BallY)
        BallY += -1
    BallX += BallMoveX
    BallY += BallMoveY
    led.unplot(BallX - BallMoveX, BallY - BallMoveY)
    led.plot(BallX, BallY)
    if BallX == 0 or BallX == 4:
        BallMoveX = -1 * BallMoveX
    if BallY == 0:
        BallMoveY = -1 * BallMoveY
loops.every_interval(200, on_every_interval)
