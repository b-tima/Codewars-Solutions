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

    def get_output(self):
        return Interpreter.convert_to_string(self.output)

    def bit_flip(self):
        bit = self.memory[self.memory_pointer]
        self.memory[self.memory_pointer] = not bit

    def read_input(self):
        # Reads a 0 if input stream is exhausted
        if self.input_pointer >= len(self.input):
            self.memory[self.memory_pointer] = False
            return

        self.memory[self.memory_pointer] = self.input[self.input_pointer]
        self.input_pointer += 1

    def output_bit(self):
        self.output.append(self.memory[self.memory_pointer])

    def initiate_memory_address(self, address):
        if self.memory_pointer not in self.memory:
            self.memory[self.memory_pointer] = False

    def move_memory_and_instruction_pointer_by_cached_steps(self, direction):
        steps = self.cached_pointer[self.instruction_pointer]
        self.memory_pointer += direction * steps
        self.instruction_pointer += steps - 1
        self.initiate_memory_address(self.memory_pointer)

    def get_reoccouring_step_count(self, start_pointer, step):
        # Counts the number of memory increments in a row
        pointer = start_pointer
        while pointer < len(self.code) and self.code[pointer] == step:
            pointer += 1
        return pointer - start_pointer

    def move_memory_and_instruction_pointer_by_memory_instruction(
        self, direction, instruction
    ):
        # Checks cache if memory string has already been enumerated
        if self.instruction_pointer in self.cached_pointer:
            self.move_memory_and_instruction_pointer_by_cached_steps(direction)
            return

        step_count = self.get_reoccouring_step_count(
            self.instruction_pointer, instruction
        )
        self.memory_pointer += direction * step_count
        self.cached_pointer[self.instruction_pointer] = step_count
        self.instruction_pointer += step_count - 1

        # Initialize memory
        self.initiate_memory_address(self.memory)

    def increment_memory(self):
        self.move_memory_and_instruction_pointer_by_memory_instruction(1, ">")

    def decrement_memory(self):
        self.move_memory_and_instruction_pointer_by_memory_instruction(-1, "<")

    def find_loop_edges(self, start_pointer, loop_start_edge, loop_end_edge, direction):
        # Count number of edges
        count = 1
        first_pointer = start_pointer
        pointer = start_pointer
        while count > 0:
            pointer += direction
            if self.code[pointer] == loop_start_edge:
                count += 1
            elif self.code[pointer] == loop_end_edge:
                count -= 1
        return first_pointer, pointer

    def move_instruction_pointer_to_loop_edge(
        self, loop_start_edge, loop_target_edge, direction
    ):
        # Check if current instruction pointer is cached
        if self.instruction_pointer in self.cached_loop:
            self.instruction_pointer = self.cached_loop[self.instruction_pointer]
            return

        loop_start, loop_end = self.find_loop_edges(
            self.instruction_pointer, loop_start_edge, loop_target_edge, direction
        )
        self.instruction_pointer = loop_end

        # Cache both loop_start and loop_end
        self.cached_loop[loop_start] = loop_end
        self.cached_loop[loop_end] = loop_start

    def loop_start(self):
        if self.memory[self.memory_pointer] == False:
            self.move_instruction_pointer_to_loop_edge("[", "]", 1)

    def loop_end(self):
        if self.memory[self.memory_pointer] == True:
            self.move_instruction_pointer_to_loop_edge("]", "[", -1)

    def next_instruction(self):
        instruction_set = {
            "+": self.bit_flip,
            ",": self.read_input,
            ";": self.output_bit,
            "<": self.decrement_memory,
            ">": self.increment_memory,
            "[": self.loop_start,
            "]": self.loop_end,
        }

        if self.instruction_pointer >= len(self.code):
            return False
        instruction = self.code[self.instruction_pointer]

        # Ignore instruction not in instruction set
        if instruction in instruction_set:
            instruction_set[instruction]()
        self.instruction_pointer += 1
        return True


def boolfuck(code, input=""):
    interpreter = Interpreter(code, input)
    while interpreter.next_instruction():
        pass
    return interpreter.get_output()
