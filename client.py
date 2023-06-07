import Pyro4

uri = "PYRO:obj_226a21babd05481ab786678d7d334ffb@localhost:54932"  # URI of the remote Calculator object
calculator = Pyro4.Proxy(uri)  # Creating a proxy object to communicate with the remote Calculator

print("Available operations: add, subtract, multiply, divide, power, square_root, absolute, negate")

while True:
    operation = input("Enter operation (add/subtract/multiply/divide/power/square_root/absolute/negate): ")
    if operation not in ["add", "subtract", "multiply", "divide", "power", "square_root", "absolute", "negate"]:
        print("Invalid operation. Please try again.")
        continue

    if operation in ["add", "subtract", "multiply", "divide"]:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        try:
            result = getattr(calculator, operation)(x, y)  # Call the appropriate method on the remote Calculator object
            print("Result:", result)
        except Pyro4.errors.CommunicationError:
            print("Failed to connect to the server. Make sure the server is running.")
        except ValueError as e:
            print("Error:", str(e))

    elif operation == "power":
        base = float(input("Enter the base number: "))
        exponent = float(input("Enter the exponent number: "))

        try:
            result = calculator.power(base, exponent)  # Call the power method on the remote Calculator object
            print("Result:", result)
        except Pyro4.errors.CommunicationError:
            print("Failed to connect to the server. Make sure the server is running.")
        except ValueError as e:
            print("Error:", str(e))

    elif operation in ["square_root", "absolute", "negate"]:
        x = float(input("Enter a number: "))

        try:
            result = getattr(calculator, operation)(x)  # Call the appropriate method on the remote Calculator object
            print("Result:", result)
        except Pyro4.errors.CommunicationError:
            print("Failed to connect to the server. Make sure the server is running.")
        except ValueError as e:
            print("Error:", str(e))
