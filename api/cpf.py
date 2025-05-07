

class CPF:
    def __init__(self, cpf):
        self.cpf = cpf


    def __str__(self):
        return self.cpf
    

    def format(self):
        return f'{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}'


    def validate(self):
        if len(self.cpf) < 11:
            return False
        
        sequencia = self.cpf[0] * len(self.cpf)
        if sequencia == self.cpf:
            return False
        
        soma = 0
        for i in range(9):
            soma += int(self.cpf[i]) * (10 - i)
        digito1 = (soma * 10) % 11
        if digito1 > 9:
            digito1 = 0
        
        soma = 0
        for i in range(10):
            soma += int(self.cpf[i]) * (11 - i)
        digito2 = (soma * 10) % 11
        if digito2 > 9:
            digito2 = 0
        
        return digito1 == int(self.cpf[9]) and digito2 == int(self.cpf[10])
        