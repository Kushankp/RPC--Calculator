# RPC--Calculator
Pyro4 Calculator Application
This is a simple client-server application that demonstrates the usage of Pyro4 to perform remote method invocations on a calculator object.

Server
The server code (server.py) sets up a Pyro4 daemon and exposes a Calculator class as a remote object. The Calculator class provides various mathematical operations such as addition, subtraction, multiplication, division, exponentiation, square root, absolute value, and negation.

To run the server:

Make sure you have Pyro4 installed (pip install Pyro4).
Run the server script using Python: python server.py.
The server will start running and display the URI (Uniform Resource Identifier) of the remote Calculator object.
Client
The client code (client.py) connects to the remote Calculator object using the URI provided by the server. It prompts the user to select an operation and input the required numbers. The client then performs the remote method invocation on the calculator object and displays the result.

To run the client:

Make sure you have Pyro4 installed (pip install Pyro4).
Run the client script using Python: python client.py.
The client will prompt for an operation and the necessary input based on the selected operation.
The result of the operation will be displayed.
Note: Make sure the server is running before running the client.

Dependencies
Pyro4: The Pyro4 library is required to run both the server and client scripts. Install it using pip install Pyro4.
Additional Notes
The server and client should be run on separate machines or processes. Adjust the URI in the client code if necessary to match the server's URI.
The server and client should have network connectivity to communicate with each other.
The server and client scripts can be customized to add more functionality or operations to the Calculator class.
Error handling is implemented in the client code to handle communication errors and invalid user input.
Feel free to modify the code or expand it further based on your requirements.

Enjoy using the Pyro4 Calculator Application!
