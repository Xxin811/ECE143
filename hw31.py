import operator
class Polynomial(object):
    def __init__(self, pol_dict):
        '''
        :param pol_dict: dictionary
        '''
        assert isinstance(self, Polynomial)
        assert isinstance(pol_dict, dict)
        for i in list(pol_dict.keys()):
            assert isinstance(i, int)
        for i in list(pol_dict.values()):
            assert isinstance(i, int)
        self.coefs = list(pol_dict.values())



    def __repr__(self):
        '''
        overwrite repr
        '''
        assert isinstance(self, Polynomial)


    def __eq__(self, other):
        '''
        overwrite equal
        '''
        assert isinstance(self, Polynomial)



    def __add__(self, other):
        '''
        overwrite add
        '''
        assert isinstance(self, Polynomial)



    def __sub__(self, other):
        '''
        overwrite substraction
        '''
        assert isinstance(self, Polynomial)



    def __mul__(self, other):
        '''
        overwirte multiplication
        '''
        assert isinstance(self, Polynomial)


    def __rmul__(self, other):
        '''
        overwrite right multiplication
        '''
        assert isinstance(self, Polynomial)



    def __truediv__(self, other):
        '''
        overwrite division
        '''
        assert isinstance(self, Polynomial)



    def subs(self, variable):
        '''
        A function that take a variable as the x value of the polynomial and return the result after the substitution
        :param variable: int number used to substitute into the polynomial
        :return: res. The answer we got after substitution
        '''
        assert isinstance(variable, int)
        assert isinstance(self, Polynomial)


