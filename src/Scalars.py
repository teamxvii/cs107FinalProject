#!/usr/bin/env python3

from FADiff import FADiff


class Scalar:
    # TODO: add name attribute
    def __init__(self, val, der=None, name=None, new_input=False):
        self._val = val
        if new_input:                      # Creating input var?
            self._der = {}
            for var in FADiff.vars_list:
                self._der[var] = 0         # Partial der of others' as 0 in self
                var._der[self] = 0         # Self's partial der as 0 in others
            self._der[self] = 1            # Self's partial der as 1 in self
            FADiff.vars_list.append(self)  # Add self to global vars list
        else:
            self._der = der

    def __add__(self, other):
        try:
            der = {}
            for var, part_der in self._der.items():
                der[var] = part_der + other.partial_der(var)
            return Scalar(self._val + other._val, der)
        except AttributeError:
            return Scalar(self._val + other, self._der)

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        try:
            der = {}
            for var, part_der in self._der.items():
                der[var] = self._val * other.partial_der(var) +\
                           part_der * other._val
            return Scalar(self._val * other._val, der)
        except AttributeError:
            der = {}
            for var, part_der in self._der.items():
                der[var] = part_der * other
            return Scalar(self._val * other, der)

    def __rmul__(self, other):
        return self.__mul__(other)

    def partial_der(self, var):                # Returns partial deriv wrt var
        return self._der[var]

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, into):
        self._val = into

    @property
    def der(self):
        return self._der

    @der.setter
    def der(self, into):
        self._der = into