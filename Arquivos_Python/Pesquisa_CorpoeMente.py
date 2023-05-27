from CorpoeMentePOO import *
from CorpoeMenteBbl import *

corpo_e_mente = Pesquisa()

while True:
    # Saudação
    print('\nBem-vindo(a) à nossa Pesquisa "Saúde Física e Mental"!\n')
    linha()

    # Instruções
    print('''Para preencher a pesquisa, preste atenção! 
Digite a idade (em anos inteiros) como resposta para a primeira pergunta.
- Para finalizar a pesquisa, digite 00 na Idade.
Digite o gênero como resposta para a segunda pergunta: '1' para 'Feminino', '2' para 'Masculino', '3' para 'Outro' ou '4' para 'Prefiro não responder'.
Nas demais perguntas, responda apenas com números: '1' para 'Sim', '2' para 'Não' ou '3' para 'Não sei responder'.''')
    linha()

    # Chamando os módulos e atributos do meu objeto
    corpo_e_mente.obter_idade()
    corpo_e_mente.obter_genero()
    
    # Perguntas do questionário
    corpo_e_mente.questionario()

    # Exibindo as respostas armazenadas
    corpo_e_mente.exibir_resposta_armazenada()

    # Criando o arquivo CSV
    corpo_e_mente.criar_arquivo_csv()

    linha()

    # Agradecimento
    print('Obrigado por participar da nossa pesquisa!')
    linha2()
