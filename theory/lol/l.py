class happy:
    a = 120

    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'{self.a} {self.b} {self.c}'


b = happy(a=100,b=120,c=50)

print(b)
