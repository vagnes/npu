from printer import Printer

class CLI(object):

    def __init__(self):
        self.printer = Printer()

    @staticmethod
    def jumbotron():
        print("""
    NANO        PRINT     UTILITY

    ███╗   ██╗  ██████╗   ██╗   ██╗
    ████╗  ██║  ██╔══██╗  ██║   ██║
    ██╔██╗ ██║  ██████╔╝  ██║   ██║
    ██║╚██╗██║  ██╔═══╝   ██║   ██║
    ██║ ╚████║  ██║       ╚██████╔╝
    ╚═╝  ╚═══╝  ╚═╝        ╚═════╝

    Write "help" to show options.

    READY.

        """)

    @staticmethod
    def help_menu():
        print("""
    func: run function (func <function> <subfunction>)
    list: list all functions (list func )
        """)

    def functions(self, user_input):
        """
        Functions:
        - copypasta
        - shapes
        """

        if user_input.startswith("copypasta"):
            user_input = self.keystrip(user_input, "copypasta")
            self.copy_pasta(user_input)

        if user_input.startswith("shapes"):
            user_input = self.keystrip(user_input, "shapes")
            self.shapes(user_input)

    @staticmethod
    def keystrip(user_input, keyword):
        return user_input.replace(keyword, "").strip()
    
    def copy_pasta(self, user_input):

        if user_input == "vuvuzela":
            self.printer.print("""
Whether we wanted it or not, 
we've stepped into a war 
with the Cabal on Mars.
So let's get to taking 
out their command, 
one by one. Valus Ta'aurc. 
From what I can gather he 
commands the Siege Dancers 
from an Imperial Land Tank 
outside of Rubicon.
He's well protected, 
but with the right team, 
we can punch through 
those defenses, 
take this beast out, 
and break their grip 
on Freehold.
        """)
            self.printer.feed(2)

    def shapes(self, user_input):

        if user_input == "tictactoe":
            self.printer.justify = self.printer.ThermalPrinter.JUSTIFY_CENTER
            self.printer.print_nowrap("""
+--------+--------+--------+
|        |        |        |
|        |        |        |
|        |        |        |
+--------------------------+
|        |        |        |
|        |        |        |
|        |        |        |
+--------------------------+
|        |        |        |
|        |        |        |
|        |        |        |
+--------+--------+--------+
""")
            self.printer.ThermalPrinter.set_defaults()
            self.printer.feed(2)


    def list_entity(self, entity):

        if entity == "func":
            print(self.functions.__doc__)

    def cli_loop(self):
        while True:
            user_input = input("> ")
            if user_input == "help":
                self.help_menu()

            elif user_input.startswith("func"):

                self.functions(self.keystrip(user_input, "func"))

            elif user_input.startswith("list"):
                self.list_entity(self.keystrip(user_input, "list"))

            elif user_input == "":
                self.printer.feed(1)

            elif user_input == "newl":
                self.printer.feed(3)

            else:
                self.printer.print(user_input)