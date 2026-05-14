input.onButtonPressed(Button.A, function () {
    PlatformX += -1
})
input.onButtonPressed(Button.B, function () {
    PlatformX += 1
})
let PlatformX = 2
let BallX = 3
let BallY = 0
let BallMoveX = 1
let BallMoveY = 1
basic.forever(function () {
    if (BallY < 5) {
        if (PlatformX > 3) {
            PlatformX = 3
        }
        if (PlatformX < 0) {
            PlatformX = 0
        }
        led.unplot(PlatformX - 1, 4)
        led.unplot(PlatformX + 2, 4)
        led.plot(PlatformX, 4)
        led.plot(PlatformX + 1, 4)
    } else {
        basic.showString("GAME OVER")
    }
})
loops.everyInterval(200, function () {
    if ((BallX == PlatformX || BallX == PlatformX + 1) && BallY == 3) {
        BallMoveY = BallMoveY * -1
    } else if ((BallX + BallMoveX == PlatformX || BallX + BallMoveX == PlatformX + 1) && BallY == 3) {
        led.unplot(BallX, BallY)
        BallY += -1
    }
    BallX += BallMoveX
    BallY += BallMoveY
    led.unplot(BallX - BallMoveX, BallY - BallMoveY)
    led.plot(BallX, BallY)
    if (BallX == 0 || BallX == 4) {
        BallMoveX = -1 * BallMoveX
    }
    if (BallY == 0) {
        BallMoveY = -1 * BallMoveY
    }
})
