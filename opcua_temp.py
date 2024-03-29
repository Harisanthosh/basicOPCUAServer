
from opcua import Server
from random import randint
import datetime
import time

server = Server()

url = "opc.tcp://192.168.200.195:4840"
server.set_endpoint(url)

name = "Digital_Factory_Server"
addspace = server.register_namespace(name)

node = server.get_objects_node()

Param = node.add_object(addspace, "Parameters")

Temp = Param.add_variable(addspace, "Temperature", 0)
Press = Param.add_variable(addspace, "Pressure", 0)
Time = Param.add_variable(addspace, "Time", 0)

Temp.set_writable()
Press.set_writable()
Time.set_writable()

server.start()
print("Server started at {}".format(url))

while True:
    Temperature = randint(10,23)
    Pressure = randint(120,380)
    TIME = datetime.datetime.now()

    print(Temperature,Pressure,TIME)

    Temp.set_value(Temperature)
    Press.set_value(Pressure)
    Time.set_value(TIME)
    time.sleep(2)
