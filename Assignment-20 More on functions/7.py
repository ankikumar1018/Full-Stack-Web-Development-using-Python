def make_adder(x):
       def adder(y):
           return x+y
       return adder

print(make_adder(1)(2))