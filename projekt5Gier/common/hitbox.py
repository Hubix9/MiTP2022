from math import sqrt, asin, ceil, floor, tan, degrees, atan2
from common.thirdParty.dda import DDA


def checkHitboxOverlay(boxAX, boxAY, boxAWidth, boxAHeight, boxBX, boxBY, boxBWidth, boxBHeight) -> bool:
    if boxBY + boxBHeight < boxAY or boxAY + boxAHeight < boxBY:
        return False

    if boxBX + boxBWidth < boxAX or boxAX + boxAWidth < boxBX:
        return False

    return True


def traverseBetweenPoints(pointAX, pointAY, pointBX, pointBY, callback=None):
    tmpCords = [pointAX, pointAY]
    vec = [pointBX - pointAX, pointBY - pointAY]
    c = sqrt((pointBX - pointAX) ** 2 + (pointBY - pointAY) ** 2)
    angle = atan2(pointBY - pointAY, pointBX - pointAX)
    print(angle)
    i = 0
    while sqrt((tmpCords[0] - pointAX) ** 2 + (tmpCords[1] - pointAY) ** 2) < c:
        if vec[0] > 0:
            deltaX = ceil(tmpCords[0]) - tmpCords[0]
            deltaX = deltaX if deltaX != 0 else 1
        else:
            deltaX = floor(tmpCords[0]) - tmpCords[0]
            deltaX = deltaX if deltaX != 0 else -1

        if vec[1] > 0:
            deltaY = ceil(tmpCords[1]) - tmpCords[1]
            deltaY = deltaY if deltaY != 0 or degrees(angle) == 0 or degrees(angle) == 180 else 1
        else:
            deltaY = floor(tmpCords[1]) - tmpCords[1]
            deltaY = deltaY if deltaY != 0 or degrees(angle) == 0 or degrees(angle) == 180 else -1
        print(deltaX, deltaY)
        if deltaX < deltaY:
            tmpY = deltaX * tan(angle)
            tmpCords[0] += deltaX
            tmpCords[1] += tmpY
        else:
            try:
                tmpX = deltaY / tan(angle)
            except ZeroDivisionError:
                tmpX = deltaX
            tmpCords[0] += tmpX
            tmpCords[1] += deltaY

        if callback is not None:
            if callback(tmpCords[0], tmpCords[1], sqrt((tmpCords[0] - pointAX) ** 2 + (tmpCords[1] - pointAY) ** 2), i):
                break


def detectRayHit(pointAX, pointAY, pointBX, pointBY, colliderX, colliderY, colWidth, colHeight, width, height) -> bool:
    tmpCords = [pointAX, pointAY]
    vec = [pointBX - pointAX, pointBY - pointAY]
    c = sqrt((pointBX - pointAX) ** 2 + (pointBY - pointAY) ** 2)
    angle = atan2(pointBY - pointAY, pointBX - pointAX)
    while sqrt((tmpCords[0] - pointAX) ** 2 + (tmpCords[1] - pointAY) ** 2) < c:
        if vec[0] > 0:
            deltaX = ceil(tmpCords[0]) - tmpCords[0]
            deltaX = deltaX if deltaX != 0 else 1
        else:
            deltaX = floor(tmpCords[0]) - tmpCords[0]
            deltaX = deltaX if deltaX != 0 else -1

        if vec[1] > 0:
            deltaY = ceil(tmpCords[1]) - tmpCords[1]
            deltaY = deltaY if deltaY != 0 or degrees(angle) == 0 or degrees(angle) == 180 else 1
        else:
            deltaY = floor(tmpCords[1]) - tmpCords[1]
            deltaY = deltaY if deltaY != 0 or degrees(angle) == 0 or degrees(angle) == 180 else -1
        if deltaX < deltaY:
            tmpY = deltaX * tan(angle)
            tmpCords[0] += deltaX
            tmpCords[1] += tmpY
        else:
            try:
                tmpX = deltaY / tan(angle)
            except ZeroDivisionError:
                tmpX = deltaX
            tmpCords[0] += tmpX
            tmpCords[1] += deltaY
        if checkHitboxOverlay(colliderX, colliderY, colWidth, colHeight, tmpCords[0], tmpCords[1], width, height):
            return True
    return False


def ddaHit(pointAX, pointAY, pointBX, pointBY, colliderX, colliderY, colWidth, colHeight, width, height) -> bool:
    coords = DDA(pointAX, pointAY, pointBX, pointBY)
    for coord in coords:
        if checkHitboxOverlay(colliderX, colliderY, colWidth, colHeight, coord[0], coord[1], width, height):
            return True
    return False
