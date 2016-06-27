# -*- coding: utf-8 -*-


def frogjum(X, Y, D):
    jumps = 0
    if X <= Y:
        while True:
            jumps += 1
            X += D
            if X >= Y:
                break;
    return jumps

frogjum(10, 140, 45)