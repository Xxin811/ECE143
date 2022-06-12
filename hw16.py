class Interval(object):
    def __init__(self, a, b):
        """
        :a: integer
        :b: integer
        """
        assert a < b
        assert isinstance(a, int)
        assert isinstance(b, int)
        self.a = a
        self.b = b
    pass

    def __repr__(self):

        return 'Interval(%s,%s)'%(self.a, self.b)
    pass

    def __eq__(self, other):
        if type(other) == type(self):
            return True
        else:
            return False
    pass

    def __add__(self, other):
        if self.b > other.a:
            return Interval(self.a,other.b)
        else:
            return [Interval(self.a,self.b),Interval(other.a,other.b)]


    pass


