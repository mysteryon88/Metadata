# @version <=0.3.10

greet: public(String[100])

@external
@payable
def __init__():
    self.greet = "Hello World"