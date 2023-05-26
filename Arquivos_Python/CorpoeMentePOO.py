import csv
import datetime

class Pesquisa:
    def __init__(self):
        self.respostas = []  # Lista de respostas de candidatos
    
    @staticmethod
    def linha():
        print('-'*160)
    
    @staticmethod
    def linha2():
        print('='*160)
    
    @staticmethod
    def verifica_idade(idade):
        while True:
            if idade == '00':
                idade = Pesquisa.verifica_saida(idade)
                if idade == '00':
                    break
            else:
                try:
                    idade = int(idade)
                    return idade
                except ValueError:
                    print('Idade inválida. Por favor, digite um valor válido.')
                    idade = input("Digite sua idade novamente: ")
    
    @staticmethod        
    def verifica_saida(idade):
        if idade == '00':
            while True:
                saida = input('Deseja sair da Pesquisa "Saúde Física e Mental"? (sim/nao): ')
                if saida == 'sim':
                    print('\nFinalizando Pesquisa...\n')
                    exit()
                elif saida == 'nao':
                    idade = input("Digite sua idade novamente: ")
                    return Pesquisa.verifica_idade(idade)
                else:
                    print("Opção Inválida. Digite 'sim' para Sair ou 'nao' para retornar à Pesquisa.")
        return idade

    @staticmethod
    def verifica_genero(pergunta):
        significados = {
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
    
    @staticmethod        
    def verifica_resposta(pergunta):
        significados = {
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

    def saudacao(self):
        print('\nBem-vindo(a) à nossa Pesquisa "Saúde Física e Mental"!\n')

    def instrucoes(self):
        print('''Para preencher a pesquisa, preste atenção!
Digite a idade (em anos inteiros) como resposta para a primeira pergunta.
- Para finalizar a pesquisa, digite 00 na Idade.
Digite o gênero como resposta para a segunda pergunta: '1' para 'Feminino', '2' para 'Masculino', '3' para 'Outro' ou '4' para 'Prefiro não responder'.
Nas demais perguntas, responda apenas com números: '1' para 'Sim', '2' para 'Não' ou '3' para 'Não sei responder'.''')

    def questionario(self):
        respostas_candidato = {}
        respostas_candidato['idade'] = self.verifica_idade(input("Digite sua idade (ou '00' para sair): "))
        respostas_candidato['genero'] = self.verifica_genero(
            'Qual gênero você se identifica? (1 = Feminino, 2 = Masculino, 3 = Outro, 4 = Prefiro não responder): ')
        respostas_candidato['pergunta01'] = self.verifica_resposta(
            'Você pratica alguma atividade física regularmente? (1 = Sim, 2 = Não, 3 = Não sei responder): ')
        respostas_candidato['pergunta02'] = self.verifica_resposta(
            'Você tem facilidade para dormir e descansar adequadamente? (1 = Sim, 2 = Não, 3 = Não sei responder): ')
        respostas_candidato['pergunta03'] = self.verifica_resposta(
            'Você já teve problemas de saúde mental, como ansiedade ou depressão? (1 = Sim, 2 = Não, 3 = Não sei responder): ')
        respostas_candidato['pergunta04'] = self.verifica_resposta(
            'Você sente que possui um equilíbrio saudável entre trabalho/estudos e vida pessoal? (1 = Sim, 2 = Não, 3 = Não sei responder): ')
        respostas_candidato['pergunta05'] = self.verifica_resposta(
            'Você já buscou ajuda profissional para lidar com questões relacionadas à sua saúde mental? (1 = Sim, 2 = Não, 3 = Não sei responder): ')
        respostas_candidato['data_hora'] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        
        self.respostas.append(respostas_candidato)

    def exibir_resposta_armazenada(self):
        ultimo_candidato = self.respostas[-1]
        print(f"Respostas armazenadas: Idade = {ultimo_candidato['idade']}, Gênero = {ultimo_candidato['genero']}, Pergunta 1 = {ultimo_candidato['pergunta01']}, Pergunta 2 = {ultimo_candidato['pergunta02']}, Pergunta 3 = {ultimo_candidato['pergunta03']}, Pergunta 4 = {ultimo_candidato['pergunta04']}, Pergunta 5 = {ultimo_candidato['pergunta05']}, Data - Hora = {ultimo_candidato['data_hora']}")
    
    def criar_arquivo_csv(self):
        with open('Pesquisa_CorpoeMente.csv', 'w', newline='', encoding='utf-8') as arquivo_csv:
            fieldnames = list(self.respostas[0].keys())  # Obtendo as chaves do dicionário do primeiro candidato como nome dos campos
            writer = csv.DictWriter(arquivo_csv, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.respostas)

    def agradecimento(self):
        print('Obrigado por participar da nossa pesquisa!')