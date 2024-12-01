class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Деление на ноль невозможно.")
        return a / b

    def calculate(self, expression):
        try:
            result = eval(expression, {"__builtins__": None}, {})
            return result
        except Exception as e:
            raise ValueError("Ошибка в выражении: " + str(e))