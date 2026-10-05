class Cliente(object):
    def __init__(self, nome, cpf, cnpj, telefone, documento):
        self.nome = nome
        self.cpf = cpf
        self.cnpj = cnpj
        self.telefone = telefone
        self.documento = documento

    def atualizar_telefone(self, novo_telefone):
        self.telefone = novo_telefone

    def exibir_informacoes(self):
        print("Nome:", self.nome)
        print("CPF:", self.cpf)
        print("CNPJ:", self.cnpj)
        print("Telefone:", self.telefone)
        print("documento:", self.documento)

class Veiculo:
    def __init__(self, placa, modelo, ano, ValorDiaria):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
        self.ValorDiaria = ValorDiaria

    def exibir_informacoes(self):
            print("Placa:", self.placa)
            print("Modelo:", self.modelo)
            print("Ano:", self.ano)
            print("ValorDiaria", self.ValorDiaria)

class Carro(Veiculo):

    def __init__(self, placa, modelo, ano, ValorDiaria):
        super().__init__(placa, modelo, ano, ValorDiaria)

    def exibir_informacoes(self):
        print("Tipo: Carro")
        print("Placa:", self.placa)
        print("Modelo:", self.modelo)
        print("Ano:", self.ano)
        print("Valor da diária:", self.ValorDiaria)


class Moto(Veiculo):

    def __init__(self, placa, modelo, ano, ValorDiaria):
        super().__init__(placa, modelo, ano, ValorDiaria)

    def exibir_informacoes(self):
        print("Tipo: Moto")
        print("Placa:", self.placa)
        print("Modelo:", self.modelo)
        print("Ano:", self.ano)
        print("Valor da diária:", self.ValorDiaria)


class Caminhão(Veiculo):

    def __init__(self, placa, modelo, ano, ValorDiaria):
        super().__init__(placa, modelo, ano, ValorDiaria)

    def exibir_informacoes(self):
        print("Tipo: Caminhão")
        print("Placa:", self.placa)
        print("Modelo:", self.modelo)
        print("Ano:", self.ano)
        print("Valor da diária:", self.ValorDiaria)


                

class Manutencao:
    def __init__(self, descricao, custo, data, veiculo, idManutencao):
        self.descricao = descricao
        self.custo = custo
        self.data = data
        self.veiculo = veiculo
        self.idManutencao = idManutencao
        self.HistoricoManutencao = []

    def registrar_manutencao(self, manutencao):
        self.manutencao.append(manutencao)

    def historico_manutencao(self, manutencao):
        self.HistoricoManutencao.append(manutencao)

class Condutor:
    def __init__(self, nome, cnh):
        self.nome = nome
        self.cnh = cnh

    def exibir_informacoes(self):
        print("Nome:", self.nome)
        print("CNH:", self.cnh)
    def atualizar_cnh(self, nova_cnh):
        self.cnh = nova_cnh

class Contrato:
    lista_contratos = []
    
    def __init__(self, idcontrato, nome, telefone, condutor, veiculo, DataInicio, DataFim, status, ValorTotal):
        self.idcontrato = idcontrato
        self.nome = nome
        self.telefone = telefone
        self.condutor = condutor
        self.veiculo = veiculo
        self.DataInicio = DataInicio
        self.DataFim = DataFim
        self.status = "ativo"
        self.ValorTotal = ValorTotal
        self.manutencao = []
        self.contrato = []

        Contrato.lista_contratos.append(self)

    def finalizar(self):
        self.status = "finalizado"

    def cancelar(self):
        self.status = "cancelado"

    @classmethod
    def excluir_contrato(cls, idcontrato):

        for contrato in cls.lista_contratos:

            if contrato.idcontrato == idcontrato:
                cls.lista_contratos.remove(contrato)
                print("Contrato excluído com sucesso!")
                return

        print("Contrato não encontrado.")

