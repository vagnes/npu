import board
import busio

from wordwrap import wrap

import adafruit_thermal_printer

class Printer(object):

    def __init__(self):
        self.ThermalPrinter = adafruit_thermal_printer
        self.ThermalPrinterClass = self.ThermalPrinter.get_printer_class(2.68)

        RX = board.RX  # PIN 3, 5V so not used with TM0
        TX = board.TX  # PIN 4

        self.uart = busio.UART(TX, RX, baudrate=19200)

        self.printer = self.ThermalPrinterClass(self.uart, auto_warm_up=False)

        self.printer.warm_up()

    def print(self, user_input):
        self.printer.print(wrap(user_input, 32))
    
    def print_nowrap(self, user_input):
        self.printer.print(user_input)

    def feed(self, lines):
        self.printer.feed(lines)
    