import Pyro4

@Pyro4.expose  # Expose the Calculator class to be used remotely
class Calculator:
    def add(self, x, y):  # Method to add two numbers
        return x + y

    def subtract(self, x, y):  # Method to subtract two numbers
        return x - y

    def multiply(self, x, y):  # Method to multiply two numbers
        return x * y

    def divide(self, x, y):  # Method to divide two numbers
        if y != 0:
            return x / y
        else:
            raise ValueError("Cannot divide by zero")

    def power(self, base, exponent):  # Method to calculate the power of a number
        return base ** exponent

    def square_root(self, x):  # Method to calculate the square root of a number
        return x ** 0.5

    def absolute(self, x):  # Method to calculate the absolute value of a number
        return abs(x)

    def negate(self, x):  # Method to negate a number
        return -x

daemon = Pyro4.Daemon()  # Creating an instance of the Pyro4 daemon
uri = daemon.register(Calculator)  # Registering the Calculator class with the daemon

print("Server ready. URI =", uri)  # Printing the URI (universal resource identifier) of the registered object
daemon.requestLoop()  # Starting the event loop of the daemon to handle incoming requests
