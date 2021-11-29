def decorator1(f):
    def wrapper(text):
        return f(text+'$$$$')

    return wrapper


def decorator2(f):
    def wrapper(self, text):
        return f(self, text+'LLLL')

    return wrapper


class A:
    @decorator2
    def say_text(self, text):
        print(text)

    def activate(self):
        self.say_text = decorator1(self.say_text)

A1 = A()
A1.say_text('123abs')
A1.activate()
A1.say_text('123abs')
