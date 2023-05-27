import csv # Importando cvs para o funcionamento do banco de dados
import datetime # Importando datetime para a captação da data e hora da resposta

class Pesquisa: #Criação da Classe Pesquisa
    
    def __init__(self):
        
        self.idade = ''
     
        self.genero = ''
    
        self.respostas = []  # Lista para posteriormente arquivas as respostas dos candidatos
    #------------------------------------------------------------------------------------------------------------------------------------#
    def verifica_idade(self, idade):                                        # Módulo para a verificação da idade inserida, 
        while True:                                                         
            if idade == '00':                                          # Se for '00'
                idade = self.verifica_saida(idade)            # chama a função 'verifica_saida'
                if idade == '00':
                    break
            else:
                try:
                    idade = int(idade)                            # Se puder ser convertida em um numero inteiro
                    return idade                                       # Retorna a idade inserida
                except ValueError:
                    print('Idade inválida. Por favor, digite um valor válido.')   # Caso contrario, retorna uma mensagem de erro
                    idade = input("Digite sua idade novamente: ")            # E solicita uma nova inserção
    #------------------------------------------------------------------------------------------------------------------------------------#                
    def verifica_saida(self, idade):                                         # Módulo para verificar a real intenção de saida do programa
        if idade == '00':                                              # Segurança em caso de saída e encerramento acidental
            while True:
                saida = input('Deseja sair da Pesquisa "Saúde Física e Mental"? (sim/nao): ')
                if saida == 'sim':
                    print('\nFinalizando Pesquisa...\n')                    
                    exit()
                elif saida == 'nao':
                    idade = input("Digite sua idade novamente: ")
                    return self.verifica_idade(idade)
                else:
                    print("Opção Inválida. Digite 'sim' para Sair ou 'nao' para retornar à Pesquisa.")
        return idade
    #------------------------------------------------------------------------------------------------------------------------------------#
    def verifica_genero(self,pergunta): # Módulo para verificação de inserção valida dentro das opçoes 
        significados = {                # e conversão do numero digitado na resposta equivalente na pergunta 'genero'
            '1': 'Feminino',
            '2': 'Masculino',
            '3': 'Outro', 
            '4': 'Prefiro não responder'
        }
        while True:
            resposta = input(pergunta)
            if resposta in significados:
                return significados[resposta]
            else:
                print("Resposta inválida. Por favor, digite apenas 1, 2, 3 ou 4.")
    #------------------------------------------------------------------------------------------------------------------------------------#
    def obter_idade(self):
        self.idade = self.verifica_idade(input("Digite sua idade (ou '00' para sair): "))
    
    def obter_genero(self):
        self.genero= self.verifica_genero('\nQual gênero você se identifica?\n(1) Feminino.\n(2) Masculino.\n(3) Outro.\n(4) Prefiro não responder.\nDigite o numero da opção: ')
    #------------------------------------------------------------------------------------------------------------------------------------#
    def verifica_resposta(self,pergunta): # Módulo para verificação de inserção valida dentro das opçoes 
        significados = {                  # e conversão do numero digitado na resposta equivalente nas demais perguntas
            '1': 'Sim',
            '2': 'Não',
            '3': 'Não sei responder'
        }
        while True:
            resposta = input(pergunta)
            if resposta in significados:
                return significados[resposta]
            else:
                print("Resposta inválida. Por favor, digite apenas 1, 2 ou 3.")      
    #------------------------------------------------------------------------------------------------------------------------------------#
    def questionario(self):
        respostas_candidato = {} # Criação onde cada candidato representa um dicionário com chave:valor.
        
        respostas_candidato['idade'] = self.idade
        
        respostas_candidato['genero'] = self.genero

        respostas_candidato['pergunta01'] = self.verifica_resposta(
            '\nVocê pratica alguma atividade física regularmente?\n(1) Sim.\n(2) Não.\n(3) Não sei responder.\nDigite o numero da opção: ')
        
        respostas_candidato['pergunta02'] = self.verifica_resposta(
            '\nVocê tem facilidade para dormir e descansar adequadamente?\n(1) Sim.\n(2) Não.\n(3) Não sei responder.\nDigite o numero da opção: ')
        
        respostas_candidato['pergunta03'] = self.verifica_resposta(
            '\nVocê já teve problemas de saúde mental, como ansiedade ou depressão? \n(1) Sim.\n(2) Não.\n(3) Não sei responder.\nDigite o numero da opção: ')
        
        respostas_candidato['pergunta04'] = self.verifica_resposta(
            '\nVocê sente que possui um equilíbrio saudável entre trabalho/estudos e vida pessoal? \n(1) Sim.\n(2) Não.\n(3) Não sei responder.\nDigite o numero da opção: ')
        
        respostas_candidato['pergunta05'] = self.verifica_resposta(
            '\nVocê já buscou ajuda profissional para lidar com questões relacionadas à sua saúde mental? \n(1) Sim.\n(2) Não.\n(3) Não sei responder.\nDigite o numero da opção: ')
        
        respostas_candidato['data_hora'] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        
        self.respostas.append(respostas_candidato) #Armazena as respostas obtidas na lista "respostas"
    #------------------------------------------------------------------------------------------------------------------------------------#
    def exibir_resposta_armazenada(self): #Quando chamado, o módulo exibe o ultimo candidato cadastrado
        ultimo_candidato = self.respostas[-1]
        print(f"\nRespostas armazenadas: Idade = {self.idade}, Gênero = {self.genero}, Pergunta 1 = {ultimo_candidato['pergunta01']}, Pergunta 2 = {ultimo_candidato['pergunta02']}, Pergunta 3 = {ultimo_candidato['pergunta03']}, Pergunta 4 = {ultimo_candidato['pergunta04']}, Pergunta 5 = {ultimo_candidato['pergunta05']}, Data - Hora = {ultimo_candidato['data_hora']}")
    #------------------------------------------------------------------------------------------------------------------------------------#
    def criar_arquivo_csv(self): # Criação do arquivo Csv contendo as respostas armazenadas
        with open('Pesquisa_CorpoeMente.csv', 'w', newline='', encoding='utf-8') as arquivo_csv:
            fieldnames = list(self.respostas[0].keys())  # Obtendo as chaves do dicionário do primeiro candidato como nome dos campos
            writer = csv.DictWriter(arquivo_csv, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.respostas)
    #------------------------------------------------------------------------------------------------------------------------------------#
    