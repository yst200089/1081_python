class student() :
    def __init__(self, name) :
        self.name = name
    def sayHello(self) :
        print('Hello, I am '+ self.name)
    def __add__(self, antherstu) :
        return self.name + antherstu.name
def main() :
    a, b, c = map(int.input(),split())

main()
