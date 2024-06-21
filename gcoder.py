class gcode():
    def __init__(self) -> None:
        self.gcode = []
    
    def add_move(self, x, y, z):
        self.gcode.append(f"G0 X{x} Y{y} Z{z}")

    def add_delay(self, delay):
        self.gcode.append(f"G4 P{delay}")
    
    def add_waitforbedtemp(self, temp):
        self.gcode.append(f"M190 S{temp}")
    
    def add_waitforhotendtemp(self, temp):
        self.gcode.append(f"M109 S{temp}")

    def add_line(self, line):
        self.gcode.append(line)

    def write(self, filename):
        with open(filename, "w") as file:
            file.write("\n".join(self.gcode))

    def export(self):
        return "\n".join(self.gcode)