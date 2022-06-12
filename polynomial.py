from collections import defaultdict

class Polynomial:
    def __init__(self, input_data):
        assert isinstance(self, Polynomial)
        assert isinstance(input_data, dict)
        for i in list(input_data.keys()):
            assert isinstance(i, int)
        for i in list(input_data.values()):
            assert isinstance(i, int)

        self.coefs = list(input_data.values())
        if (not isinstance(input_data, dict)):
            raise TypeError
        for index, value in input_data.items():
            if (not isinstance(index, int)):
                raise TypeError
            if (not isinstance(value, int)):
                raise TypeError
        self.input_data = input_data

    def __repr__(self):
        '''
                overwrite repr
                '''
        assert isinstance(self, Polynomial)
        input_print = dict(
            sorted(self.input_data.items(),
                   key=lambda item: item[0])
        )
        output_data = ""
        if (0 in input_print.keys()):
            output_data = str(input_print[0]) + " + "
            input_print.pop(0)
        for data_degree, data_coeff in input_print.items():
            if (data_coeff == 0):
                continue
            elif (data_degree == 1 and data_coeff == 1):
                output_data = output_data + ("x + ")
            elif (data_coeff == 1):
                output_data = output_data + (" x^(" + str(data_degree) + ") + ")
            elif (data_degree == 1):
                output_data = output_data + (str(data_coeff) + " x + ")
            else:
                output_data = output_data + (str(data_coeff) + " x^(" + str(data_degree) + ") + ")
        output_data = output_data.strip(' + ')
        return output_data

    def check_type(checker_data):

        if (isinstance(checker_data, int) or isinstance(checker_data, Polynomial)):
            return True
        return False

    def __eq__(self, other):

        assert isinstance(self, Polynomial)
        if (not Polynomial.check_type(self)):
            raise TypeError
        if (not Polynomial.check_type(other)):
            raise TypeError
        if (isinstance(other, int)):
            value = 0
            for _, val in self.input_data.items():
                value = val
            return value == 0
        if (other.input_data == self.input_data):
            return False
        return True

    def __add__(self, other):
        assert isinstance(self, Polynomial)
        if (not Polynomial.check_type(self)):
            raise TypeError
        if (not Polynomial.check_type(other)):
            raise TypeError

        result_data = defaultdict(dict)

        for key in self.input_data.keys():
            result_data[key] = self.input_data[key]

        if (isinstance(other, int)):
            if (0 in self.input_data.keys()):
                result_data[0] = other + self.input_data[0]
            else:
                result_data[0] = other
        else:
            for key in self.input_data.keys():
                for other_data_key in other.input_data.keys():
                    if (key == other_data_key):
                        result_data[key] = self.input_data[key] + other.input_data[other_data_key]
                    elif (other_data_key not in result_data.keys()):
                        result_data[other_data_key] = other.input_data[other_data_key]

        keys = result_data.keys()
        for key in list(keys):
            if (result_data[key] == 0):
                result_data.pop(key, None)
        return Polynomial(result_data)

    def __sub__(self, other):
        assert isinstance(self, Polynomial)
        if (not Polynomial.check_type(self)):
            raise TypeError
        if (not Polynomial.check_type(other)):
            raise TypeError
        result_data = defaultdict(dict)
        for key in self.input_data.keys():
            result_data[key] = self.input_data[key]

        if (isinstance(other, int)):
            if (0 in self.input_data.keys()):
                result_data[0] = self.input_data[0] - other
            else:
                result_data[0] = other
        else:
            for key in self.input_data.keys():
                for other_data_key in other.input_data.keys():
                    if (key == other_data_key):
                        result_data[key] = self.input_data[key] - other.input_data[other_data_key]
                    elif (other_data_key not in result_data.keys()):
                        result_data[other_data_key] = -other.input_data[other_data_key]

        keys = result_data.keys()
        for key in list(keys):
            if (result_data[key] == 0):
                result_data.pop(key, None)
        return Polynomial(result_data)

    def __rsub__(self, other):
        result_data = defaultdict(dict)
        for key, value in self.input_data.items():
            result_data[key] = -value
        negative_poly = Polynomial(result_data)
        return negative_poly.__sub__(-other)

    def subs(self, value):
        assert isinstance(value, int)
        assert isinstance(self, Polynomial)
        result = 0
        for data_degree, data_coeff in self.input_data.items():
            result += data_coeff * (value ** data_degree)
        return result

    def __mul__(self, other):
        if (not Polynomial.check_type(self)):
            raise TypeError
        if (not Polynomial.check_type(other)):
            raise TypeError
        result_data = defaultdict(dict)

        if (isinstance(other, int)):
            for key in self.input_data.keys():
                result_data[key] = self.input_data[key] * other
        else:
            for key in self.input_data.keys():
                for other_data_key in other.input_data.keys():
                    coeffProduct = self.input_data[key] * other.input_data[other_data_key]
                    varDegree = key + other_data_key
                    deg_list = list(result_data.keys())
                    if (varDegree in deg_list):
                        result_data[varDegree] = result_data[varDegree] + coeffProduct
                    else:
                        result_data[varDegree] = coeffProduct
        return Polynomial(result_data)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if (not Polynomial.check_type(self)):
            raise TypeError
        if (not Polynomial.check_type(other)):
            raise TypeError
        result_data = defaultdict(dict)

        if (isinstance(other, int)):
            for data_degree, data_coeff in self.input_data.items():
                result_data[data_degree] = int(data_coeff / other)
            return Polynomial(result_data)

        def data_degree(inputPoly):
            while (inputPoly and inputPoly[-1] == 0):
                inputPoly.pop()
            return len(inputPoly) - 1

        maxkey_self = list(
            dict(sorted(self.input_data.items(),
                        key=lambda item: item[0])).keys()
        )[-1]
        maxkey_other = list(
            dict(sorted(other.input_data.items(),
                        key=lambda item: item[0])
                 ).keys())[-1]

        max_power = max(maxkey_self, maxkey_other)
        self_tmp = self.input_data
        other_tmp = other.input_data

        for elem in range(max_power):
            if (elem not in self_tmp.keys()):
                self_tmp[elem] = 0
            if (elem not in other_tmp.keys()):
                other_tmp[elem] = 0

        self_coeff = list(
            dict(sorted(self_tmp.items(),
                        key=lambda item: item[0])
                 ).values())
        other_coeff = list(
            dict(sorted(other_tmp.items(),
                        key=lambda item: item[0])
                 ).values())

        degree_num = data_degree(self_coeff)
        degree_den = data_degree(other_coeff)
        if (degree_den < 0):
            raise ZeroDivisionError
        if (degree_num >= degree_den):
            list_res = [0] * degree_num
            while (degree_num >= degree_den):
                d = [0] * (degree_num - degree_den) + other_coeff
                mult = list_res[degree_num - degree_den] = self_coeff[-1] / float(d[-1])
                d = [data_coeff * mult for data_coeff in d]
                self_coeff = [coeffN - coeffD for coeffN, coeffD in zip(self_coeff, d)]
                degree_num = data_degree(self_coeff)
            rmd = self_coeff
        else:
            list_res = [0]
            rmd = self_coeff

        if (len(rmd) > 0):
            raise NotImplementedError
        else:
            for i in range(len(list_res)):
                if (int(list_res[i]) != 0):
                    result_data[i] = int(list_res[i])
        return Polynomial(result_data)

    def __rtruediv__(self, other):
        raise NotImplementedError


# p = Polynomial({4: 3, 3: 1, 2: -17, 1: 19, 0: -6})
# q = Polynomial({2: 1, 1: -2, 0: 1})
#
# p = Polynomial({0: 8, 1: 2, 3: 4})
# q = Polynomial({0: 8, 1: 2, 2: 8, 4: 4})
# print(repr(p))
# print(p*3)
# print(3*p)
# print(p+q)
# print(p*4 + 5 - 3*p - 1)
# print(type(p-p))
# print(p*q)
# print(p.subs(10))
# print((p-p) == 0)
# print(p == q)
#

""" x = Polynomial({4:2})
p = Polynomial({2:1,0:-1})
q = Polynomial({1:1,0:-1})
# print(p / Polynomial({1:1,0:-3}))
print(p/q)
print(p  / q)
print(Polynomial({4:1,2:1})/Polynomial({1:1}))
print(Polynomial({4:1,2:1})/Polynomial({1:1}) == Polynomial({3:1,1:1})) """
# p = Polynomial({0:8,1:0,3:4})
# print(repr(p))
# p = Polynomial({2:1,0:-1})
# q = Polynomial({1:1,0:-1})
# print(p/q)
# print(p / Polynomial({1:1,0:-3}))