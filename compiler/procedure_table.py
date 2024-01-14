from code_generator import CodeGenerator

class ProcedureTable(dict):
    def __init__(self):
        super().__init__()
        self.memory_offset = 0
        self.current_line = 0
        self.first_line = ''
        self.code = []

    def add_procedure(self, procedure):
        if procedure.name in self:
            raise Exception(f"Redeclaration of {procedure.name}")
        self.setdefault(procedure.name, procedure)
        self.memory_offset = procedure.last_indeks

    def gen_first_jump(self):
        self.first_line = f"JUMP start_program"
        self.current_line += 1

    def update_first_jump(self):
        first_line = self["PROGRAM"].first_line
        self.first_line = self.first_line.replace('start_program', str(first_line))

    def gen_code(self):
        codeGenerator = CodeGenerator()
        for name in self:
            self[name].first_line = self.current_line
            codeGenerator.gen_code_from_procedure(name, self)
            self.code.append(codeGenerator.code)
            self.current_line += len(codeGenerator.code)
