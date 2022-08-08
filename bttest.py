import bluetooth

name="bt_server"
target_name="test"
# some random uuid, generated by https://www.famkruithof.net/uuid/uuidgen
uuid="0fee0450-e95f-11e5-a837-0800200c9a66"

def runServer():
    # you had indentation problems on this line:
    serverSocket=bluetooth.BluetoothSocket(bluetooth.RFCOMM )
    port=bluetooth.PORT_ANY
    serverSocket.bind(("",port))
    print ("Listening for connections on port: ", port)

# wait for a message to be sent to this socket only once
    serverSocket.listen(1)
    port=serverSocket.getsockname()[1]

# you were 90% there, just needed to use the pyBluez command:
    bluetooth.advertise_service( serverSocket, "SampleServer",
    service_id = uuid,
    service_classes = [ uuid, bluetooth.SERIAL_PORT_CLASS ],
    profiles = [ bluetooth.SERIAL_PORT_PROFILE ]
    )

    inputSocket, address=serverSocket.accept()
    print ("Got connection with" , address)
    data=inputSocket.recv(1024)
    print ("received [%s] \n " % data)
    inputSocket.close()
    serverSocket.close()

runServer()