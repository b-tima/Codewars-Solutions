class Interpreter:
    def __init__(self, code, program_input):
        self.code = code
        self.program_input = program_input
        
        self.output = ""
        self.tape = [0 for i in range(100)]
        self.memory_pointer = 0
        self.instruction_pointer = 0
        self.input_pointer = 0
    
    def incrementPointer(self):
        self.memory_pointer += 1
        self.instruction_pointer += 1
    
    def decrementPointer(self):
        self.memory_pointer -= 1
        self.instruction_pointer += 1
    
    def incrementValue(self):
        self.tape[self.memory_pointer] += 1
        if self.tape[self.memory_pointer] > 255:
            self.tape[self.memory_pointer] = 0
        self.instruction_pointer += 1
    
    def decrementValue(self):
        self.tape[self.memory_pointer] -= 1
        if self.tape[self.memory_pointer] < 0:
            self.tape[self.memory_pointer] = 255
        self.instruction_pointer += 1
    
    def outputValue(self):
        self.output += chr(self.tape[self.memory_pointer])
        self.instruction_pointer += 1
    
    def acceptInput(self):
        self.tape[self.memory_pointer] = self.nextInput()
        self.instruction_pointer += 1
    
    def loopStart(self):
        if self.tape[self.memory_pointer] == 0:
            count = 1
            while count > 0:
                self.instruction_pointer += 1
                if self.code[self.instruction_pointer] == '[':
                    count += 1
                elif self.code[self.instruction_pointer] == ']':
                    count -= 1
        self.instruction_pointer += 1
    
    def loopEnd(self):
        if self.tape[self.memory_pointer] != 0:
            count = 1
            while count > 0:
                self.instruction_pointer -= 1
                if self.code[self.instruction_pointer] == ']':
                    count += 1
                elif self.code[self.instruction_pointer] == '[':
                    count -= 1
        self.instruction_pointer += 1
    
    def nextInput(self):
        byte = ord(self.program_input[self.input_pointer])
        self.input_pointer += 1
        return byte
    
    def nextInstruction(self):
        if self.instruction_pointer >= len(self.code):
            return False
        instruction = self.code[self.instruction_pointer]
        {   '>': self.incrementPointer, '<': self.decrementPointer, '+': self.incrementValue, \
            '-': self.decrementValue, '.': self.outputValue, ',': self.acceptInput, \
            '[': self.loopStart, ']': self.loopEnd}[instruction]()
        return True

        
def brain_luck(code, program_input):
    interpreter = Interpreter(code, program_input)
    while interpreter.nextInstruction():
        pass
    return interpreter.output