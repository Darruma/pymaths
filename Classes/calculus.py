class Calculus:
    def __init__(self,precision):
        self.dx = 1/(10 ** precision)

    def derivative_operator(self,f):  # define a function that takes a function f
        def fPrime(x):                # returns the derivative function
            value = (f(x + self.dx) - f(x)) / self.dx
            return round(value,3)
        return fPrime

    def integrate(self,f): # takes a function f 
        def integral(a,b): # returns a function which integrates between a and b
            rectangleWidth = (b - a) * self.dx
            sum = 0
            index = a
            while(index <= b):
                sum += f(index) * rectangleWidth
                index += rectangleWidth 
            return sum
        return integral

    

