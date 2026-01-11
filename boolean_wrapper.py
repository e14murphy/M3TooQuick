"""Used to pass boolean variables between functions and other classes.

Instance variables:
    boolvar (boolean): Represents any boolean variable.

Methods:
    boolvar_mutator(boolean): Updates the value of self.boolvar to equal the supplied value."""

class BooleanWrapper:
    def __init__(self):
        self.boolvar = True

    def boolvar_mutator(self, boolean):
        """Updates the value of self.boolvar to the supplied value"""
        self.boolvar = boolean