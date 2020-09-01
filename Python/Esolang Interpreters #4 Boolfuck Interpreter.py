class Interpreter:
    @staticmethod
    def convert_to_bits(string):
        def byte_to_bits(byte):
            bits = []
            for i in range(7, -1, -1):
                if byte - 2 ** i >= 0:
                    byte -= 2 ** i
                    bits.append(True)
                else:
                    bits.append(False)
            return reversed(bits)

        bits = []
        for c in string:
            bits.extend(byte_to_bits(ord(c)))
        return bits

    @staticmethod
    def convert_to_string(bits):
        def bits_to_byte(bits):
            bits = list(reversed(bits))
            byte = 0
            for i in range(8):
                if bits[i]:
                    byte += 2 ** (7 - i)
            return byte

        if len(bits) % 8 != 0:
            bits.extend(False for i in range(8 - (len(bits) % 8)))
        string = ""
        for i in range(0, len(bits), 8):
            string += chr(bits_to_byte(bits[i : i + 8]))
        return string

    def __init__(self, code, input):
        self.code = code
        self.input = Interpreter.convert_to_bits(input)

        self.memory_pointer = 0
        self.instruction_pointer = 0
        self.input_pointer = 0

        self.memory = {0: False}

        # List of bools
        self.output = []

        # Loop cache
        self.cached_loop = {}
        self.cached_pointer = {}

    def getOutput(self):
        return Interpreter.convert_to_string(self.output)

    def bitFlip(self):
        bit = self.memory[self.memory_pointer]
        self.memory[self.memory_pointer] = True if not bit else False
        self.instruction_pointer += 1

    def readInput(self):
        # Reads a 0 if input stream is exhausted
        if self.input_pointer >= len(self.input):
            self.instruction_pointer += 1
            self.memory[self.memory_pointer] = False
            return

        self.memory[self.memory_pointer] = self.input[self.input_pointer]
        self.input_pointer += 1
        self.instruction_pointer += 1

    def outputBit(self):
        self.output.append(self.memory[self.memory_pointer])
        self.instruction_pointer += 1

    def moveMemory(self, direction, instruction):
        # Checks cache if number of rows have already been enumerated
        if self.instruction_pointer in self.cached_pointer:
            self.memory_pointer += (
                direction * self.cached_pointer[self.instruction_pointer]
            )

            # Initalize memory
            if self.memory_pointer not in self.memory:
                self.memory[self.memory_pointer] = False

            self.instruction_pointer += self.cached_pointer[self.instruction_pointer]
            return

        count = 0
        first_pointer = self.instruction_pointer

        # Counts the number of memory increments in a row
        while (
            self.instruction_pointer < len(self.code)
            and self.code[self.instruction_pointer] == instruction
        ):
            self.instruction_pointer += 1
            count += 1
        self.memory_pointer += direction * count

        # Initialize memory
        if self.memory_pointer not in self.memory:
            self.memory[self.memory_pointer] = False

        self.cached_pointer[first_pointer] = count

    def incrementMemory(self):
        self.moveMemory(1, '>')

    def decrementMemory(self):
        self.moveMemory(-1, '<')

    def moveLoop(self, b1, b2, direction, condition):
        if condition:
    
            # Check cache for loopend
            if self.instruction_pointer in self.cached_loop:
                self.instruction_pointer = self.cached_loop[self.instruction_pointer] + 1
                return
            
            # Count number of brackets
            count = 1
            first_pointer = self.instruction_pointer
            while count > 0:
                self.instruction_pointer += direction
                if self.code[self.instruction_pointer] == b1:
                    count += 1
                elif self.code[self.instruction_pointer] == b2:
                    count -= 1

            # Cache both loopstart and loopend
            self.cached_loop[first_pointer] = self.instruction_pointer
            self.cached_loop[self.instruction_pointer] = first_pointer

        self.instruction_pointer += 1


    def loopStart(self):
        self.moveLoop('[', ']', 1, self.memory[self.memory_pointer] == False)

    def loopEnd(self):
        self.moveLoop(']', '[', -1, self.memory[self.memory_pointer] == True)

    def nextInstruction(self):
        instruction_set = {
            "+": self.bitFlip,
            ",": self.readInput,
            ";": self.outputBit,
            "<": self.decrementMemory,
            ">": self.incrementMemory,
            "[": self.loopStart,
            "]": self.loopEnd,
        }

        if self.instruction_pointer >= len(self.code):
            return False
        instruction = self.code[self.instruction_pointer]

        # Ignore instruction not in instruction set
        if instruction not in instruction_set:
            self.instruction_pointer += 1
        else:
            instruction_set[instruction]()
        return True


def boolfuck(code, input=""):
    interpreter = Interpreter(code, input)
    while interpreter.nextInstruction():
        pass
    return interpreter.getOutput()