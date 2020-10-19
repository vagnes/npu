from cli import CLI

if __name__ == "__main__":
    cli = CLI()
    cli.jumbotron()
    cli.cli_loop()

# Print a line of text:
# printer.print("Hello world!")

# Move the paper forward two lines:
# printer.feed(2)

# # Print a bold line of text:
# printer.bold = True
# printer.print("Bold hello world!")
# printer.bold = False

# # Print a normal/thin underline line of text:
# printer.underline = adafruit_thermal_printer.UNDERLINE_THIN
# printer.print("Thin underline!")

# # Print a thick underline line of text:
# printer.underline = adafruit_thermal_printer.UNDERLINE_THICK
# printer.print("Thick underline!")

# # Disable underlines.
# printer.underline = None

# # Print an inverted line.
# printer.inverse = True
# printer.print("Inverse hello world!")
# printer.inverse = False

# # Print an upside down line.
# printer.upside_down = True
# printer.print("Upside down hello!")
# printer.upside_down = False

# # Print a double height line.
# printer.double_height = True
# printer.print("Double height!")
# printer.double_height = False

# # Print a double width line.
# printer.double_width = True
# printer.print("Double width!")
# printer.double_width = False

# # Print a strike-through line.
# printer.strike = True
# printer.print("Strike-through hello!")
# printer.strike = False

# # Print medium size text.
# printer.size = adafruit_thermal_printer.SIZE_MEDIUM
# printer.print("Medium size text!")

# # Print large size text.
# printer.size = adafruit_thermal_printer.SIZE_LARGE
# printer.print("Large size text!")

# # Back to normal / small size text.
# printer.size = adafruit_thermal_printer.SIZE_SMALL

# # Print center justified text.
# printer.justify = adafruit_thermal_printer.JUSTIFY_CENTER
# printer.print("Center justified!")

# # Print right justified text.
# printer.justify = adafruit_thermal_printer.JUSTIFY_RIGHT
# printer.print("Right justified!")

# # Back to left justified / normal text.
# printer.justify = adafruit_thermal_printer.JUSTIFY_LEFT

# # Print a UPC barcode.
# printer.print("UPCA barcode:")
# printer.print_barcode("123456789012", printer.UPC_A)

# # Feed a few lines to see everything.
# printer.feed(2)
