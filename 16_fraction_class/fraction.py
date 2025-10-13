class Fraction:
    def __init__(self, numerator = 0, denominator = 1):
        # divisor = self.gcd(numerator, denominator)
        self._numerator = numerator 
        self._denominator = denominator 
    
    # Getter
    @property
    def numerator(self):
        return self._numerator
    
    @property
    def denominator(self):
        return self._denominator
    
    # Setter
    @numerator.setter
    def numerator(self, value):
        self._numerator = value
    
    @denominator.setter
    def denominator(self, value):
        if (value == 0):
            print("Incorrect logic: denominator cannot be zero.")
            self.denominator = 1
        else:
            self._denominator = value

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    # Multiplication operator
    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
    
    # Addition operator
    def __add__(self, other):
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)
    
    # Subtraction
    def __sub__(self, other):
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)
    
    # Less than (<)
    def __lt__(self, other):
        return self.__cmp__(other) < 0

    # Compare
    def __cmp__(self, other):
        temp = self.__sub__(other)
        if temp.numerator > 0:
            return 1 # greater
        elif temp.numerator < 0:
            return -1 # smaller
        else:
            return 0 # equal

    # Division
    def __truediv__(self, other):
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        return Fraction(num, den)

    def gcd(n, d):
        gcd = 1
        k = 1
        while k <= n and k <= d:
            if n % k == 0 and d % k == 0:
                gcd = k
            k+=1
        
        return gcd


frac = Fraction(2, 3)
print(frac)

frac.numerator = 3
frac.denominator = 5
print(frac)

frac2 = Fraction(4, 5)
print(f"{frac} * {frac2} = {frac*frac2}")
print(f"{frac} + {frac2} = {frac+frac2}")
print(f"{frac} - {frac2} = {frac-frac2}")
print(f"{frac} < {frac2} = {frac<frac2}")
print(f"{frac} / {frac2} = {frac/frac2}")