import tkinter as tk
import serial
import serial.tools.list_ports

serial_port = 0

ports_name_list = []


def list_ports():
    global ports_name_list
    ports_list = serial.tools.list_ports.comports()
    ports_name_list = [port.device for port in ports_list]    

def serial_connection():
    global ports
    global ports_selection
    port_name = ports.get()
    serial_port = serial.Serial(port = port_name, timeout = 0)


window = tk.Tk()
window.title("LiPo monitor")

port_label = tk.Label(window, text = "Ports: ")
port_label.pack()

list_ports()
ports = tk.StringVar()
ports_selection = tk.OptionMenu(window, ports, *ports_name_list)
ports_selection.pack()

port_connection =  tk.Button(window, text = "Connect", command=serial_connection)
port_connection.pack()
window.mainloop()