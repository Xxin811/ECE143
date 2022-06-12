import math
from fractions import Fraction
class Rational(object):
    def __init__(self, numerator, denominator):
        """
        :a: integer
        :b: integer
        """
        assert denominator != 0
        assert isinstance(numerator, int)
        assert isinstance(denominator, int)
        self.num = numerator
        self.den = denominator

    pass

    def __repr__(self):
        return '{}'.format(Fraction(self.num, self.den))

    def __rtruediv__(self, other):
        return Rational((Fraction(other)/Fraction(self.num, self.den)).numerator,
                        (Fraction(other) / Fraction(self.num, self.den)).denominator)

    def __neg__(self):
        return Rational(-self.num, self.den)

    def __float__(self):
        return self.num/self.den

    def __int__(self):
        return math.floor(Fraction(self.num/self.den))

    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        return Rational(new_num, new_den)

    def __sub__(self, other):
        if type(other) == int:
            other = Rational(other.num, other.den)
        if type(other) == Rational:
            new_num = self.num * other.den - self.den * other.num
            new_den = self.den * other.den
            return Rational(Fraction(new_num, new_den).numerator,
                             (Fraction(new_num, new_den).denominator))

    def __mul__(self, other):
        if type(other) == int:
            other = Rational(other, 1)
        if type(other) == Rational:
            new_num = self.num * other.num
            new_den = self.den * other.den
            return Rational(new_num, new_den)

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num == second_num

    def __lt__(self, other):
        return Fraction(self.num, self.den) < Fraction(other.num, other.den)

    def __truediv__(self, other):
        if type(other) == int:
            other = Rational(other, 1)
        if type(other) == Rational:
            new_param = Rational(other.den, other.num)
            return self.__mul__(new_param)


def square_root_rational(x,abs_tol=Rational(1,1000)):
    '''
    This function is used to get the square root of a number
    :param x: An input rational number
    :param abs_tol:absolute precision
    :return:the square root of x
    '''
    assert isinstance(x,Rational)
    assert isinstance(abs_tol,Rational)
    low = 0
    up = float(x)
    while True:
        mid = (low + up)/2

        if abs(mid ** 2 - float(x)) < float(abs_tol):
            return Fraction(mid)
        else:
            if mid ** 2 > float(x):
                up = mid
            elif mid ** 2< float(x):
                low = mid

# print(square_root_rational(Rational(1112,3),abs_tol=Rational(1,1000)))