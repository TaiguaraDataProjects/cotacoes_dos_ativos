from datetime import datetime


class Configs:

    def __init__(self, endereco_base_do_projeto: str, data_inicial: str, data_final: str, processar_cotacoes: bool,
                 processar_dividendos: bool):
        if endereco_base_do_projeto[-1] != '\\':
            endereco_base_do_projeto = endereco_base_do_projeto + '\\'

        self.endereco_base_do_projeto = endereco_base_do_projeto

        self.data_inicial = datetime.strptime(data_inicial, "%Y-%m-%d").date()
        self.data_final = datetime.strptime(data_final, "%Y-%m-%d").date()

        self.processar_cotacoes = processar_cotacoes
        self.processar_dividendos = processar_dividendos

        self.endereco_para_salvar_dados = self.endereco_base_do_projeto + 'data\\'
        self.arquivo_compilado_cotacoes = self.endereco_para_salvar_dados + 'todas_as_cotacoes.csv'
        self.arquivo_compilado_dividendos = self.endereco_para_salvar_dados + 'todos_os_dividendos.csv'
        self.arquivo_com_lista_de_fundos_imobiliarios = self.endereco_base_do_projeto + 'lista_de_fundos.csv'

    def __str__(self):
        return (f"Endereço base: {self.endereco_base_do_projeto}\n"
                f"Data inicial: {str(self.data_inicial)}\n"
                f"Data final: {str(self.data_final)}")
