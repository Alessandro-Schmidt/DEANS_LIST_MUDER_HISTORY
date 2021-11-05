import pyfiglet
#from threading import Thread
from tabulate import tabulate
#import time

"""
História: 
Ocorreu o assassinato da decâna Andreia Maluceli, dentro do campûs da PUCPR. 
- Lado desconhecido
Cena do crime: 
Local: Na ponte em direção à escola Politécnica. 
Arma: Compasso; 
Assassino: Agente duplo - Giulia Carvalho;
Motivo: A decana descobriu sua identidade, e ameaçou contar para um dos lados;

Período: Guerra fria
Personagens: 
- Monitores de RPLM - Um deles é espião Soviético!
  - Vinícius;
  - Alessandro
- Marco Paludo (General da CIA dentro da PUC);
- Professora Kelly Rafaela (Espiã da CIA);
- Daniel Nowak - Desconhecido (Duplo-espião);
- André Dephino - (espião soviético);
- Giulia Carvalho - Desconhecida (dupla espiã); 
- Sheila Reinehr (Espiã da CIA) 
"""


titulo = pyfiglet.figlet_format('DEANS LIST', font='banner3-D')
sub_title = pyfiglet.figlet_format('Um misterio de ASSASSINATO', font='standard')
print(titulo)
print(sub_title)

# início da história
#print('--- Contexto ---\nNo auge da Guerra Fria, uma semana após a crise dos mísseis de Cuba e início do bloqueio continental, a América Latina vive um momento de tensão sem igual.\n\nNa PUCPR não é diferente.\n\nEspiões andam disfarçados entres os alunos, com o objetivo de roubar os postits dos requisitos do projeto da Bomba de Hidrogênio.\n\nO prédio da Escola Politécnica é o mais vigiado do Paraná. Não é permitida a entrada de pessoas não autorizadas nas aulas de BES.\n\nO assassinato da reitora veio como um choque para os estudantes, e está sendo abafado pela mídia e pela Universidade.\n\nVocê foi designado pelo Governo Federal para solucionar o mistério. A justiça está nas suas mãos. Descubra o autor do crime, o local do crime e a arma do crime. SEJA RÁPIDO! O responsável pode estar fugindo.\n\nVocê tem 15 minutos para descobrir o criminoso ou então conviver pelo resto da vida com o peso de ter o deixado escapar pelos portões da PUCPR.')
#print('-'*len('Vítima: Andreia Malucelli, decâna da Escola Politécnica'))
#print('RELATÓRIO DA INVESTIGAÇÃO\nData do crime: 20/10/1962\nVítima: Andreia Malucelli, decâna da Escola Politécnica.\nLocal: Sigiloso.\nArma: Sigiloso.\nAutor do crime: em investigação.')
#print('-'*len('Vítima: Andreia Malucelli, decâna da Escola Politécnica'))
#print('\n\n-- HIPÓTESES --\n\n')
#print('LOCAL -- \n\na) O assassinato foi feito ao ar livre.\n\nb) Foram encontrados documentos queimados da dec''na no lixo antes da saída da PUCPR.\n\nc) Ela foi vista correndo em diração à Escola Politécnica, com uma bolsa preta...\n\nd) Uma bolsa de cor desbotada foi achada nas margens do rio que passa pela PUCPR.\n\n')
#print('ARMA --\n\na) Uma fita cassete pequena foi encontrada junto aos documentos no lixo. Nesta fita, havia o hino da Alemanha Oriental.\n\nb) O General da CIA dentro da PUCPR possui uma arma no seu escritório\n\nc) Espiões da KGB usam armas pouco convencionais para evitar suspeitas.\n\nd) Um compasso sujo foi encontrado junto com a identidade de um duplo espião.\n\ne) Um notebook completamente formatado foi derrubado próximo a cena do crime.\n\n')
#print('SUSPEITO --\n\na) Se sabe da existência de no mínimo uma espiã da KGB na Universidade.\n\nb) Não era do interesse americano, a morte da decana.\n\nc) O assassino não era neutro.\n\nd) É conhecido o envolvimento de pelo menos um dos monitores com a KGB.\n\ne) Existem no mínimo, dois espiões duplos na Universidade.\n\nf) Se sabe que Alessandro já estava desconfiado de algo...')
#print('\n\nFATOS IMPORTANTES\n\nf) Um dos agentes duplos não tem relação alguma com BES.\n\ng) Você investigar alguém pode causar a sua morte. \n\n')
lados = [['Nome:', 'Lado:', 'Pistas:'], ['Vinícius', '?', ''], ['Alessandro', '?', ''], ['Marco Paludo', 'General da CIA dentro da PUC', ''], ['Professora Kelly', 'Espiã da CIA', ''], ['Daniel Nowak', '?', ''], ['André Delphino', 'Espião da KGB', ''], ['Giulia Carvalho', '?', ''], ['Sheila Reinehr', 'Espiã da CIA', '']]
while True: 
  print(tabulate(lados,headers='firstrow', tablefmt='grid'))
  while True: 
    nomes = [['Código', 'Nome', 'Código', 'Nome'],['1', 'Vinícius', '2', 'Alessandro'], ['3', 'Marco Paludo', '4', 'Professora Kelly'],['5', 'Daniel Nowak', '6', 'André Delphino'], ['7','Giulia Carvalho', '8', 'Sheila Reinehr']]
    armas = [['Código', 'Arma'], ['1', 'Fita Cassete'], ['2', 'Arma do General'], ['3','Curto circuíto\nguiado\n(computador)'], ['4','Compasso'], ['5', 'Machado']]
    locais = [['Código','Locais suspeitos'], ['1','Sala dos monitores'], ['2', 'Sala do General'], ['3', ''], ['4', 'Ponte Escola\nPolitécnica']]
    escolhas_possiveis = [['Número da ação','Ação'], ['1','Investigar'], ['2', 'Acusar'], ['3', 'Consultar possibilidades']]
    print(tabulate(escolhas_possiveis, headers='firstrow', tablefmt='grid'))
    option = str(input('Digite sua escolha: ')).upper()
    if option =='3' or option in 'CONSULTAR':
      print(tabulate(nomes,headers='firstrow', tablefmt='grid'))
      print(tabulate(armas,headers='firstrow', tablefmt='grid'))
      print(tabulate(locais,headers='firstrow', tablefmt='grid'))
    elif option == '1' or option == 'INVESTIGAR':
      print('-'*len('INVESTIGAÇÃO')+'\nINVESTIGAÇÃO\n'+'-'*len('INVESTIGAÇÃO'))
      print(tabulate(nomes, headers='firstrow', tablefmt='grid'))
      while True:
        try: 
          p = int(input('Digite o número de quem deseja investigar: '))
          if p not in range(1,8):
            print('\033[31m\nDigite apenas opções válidas\n\033[m')
          else:
            break
        except:
          print('\033[31m\nDigite apenas opções válidas\n\033[m')
      if p == 1:
        print('\n\nVocê chega para investigar Vinícius...\n\n')
        #time.sleep(0.9)
        print('Vinícius é encontrado morto na sala de monitores. Alguém o atingiu com um machado. Vinícius segurava uma foto do campûs com uma ponte circulada em vermelho.')
        lados[1][1] = '--- MORTO DURANTE INVESTIGAÇÃO ---'
        lados [1][2] = 'Mapa da PUCPR ponte marcada\nMorto com machado'
      elif p == 2:
        while True:
          try: 
            print('Alessadro:\n')
            opt = int(input('[1] - Investigar\n[2] - Interrogar\nSua escolha: ')) 
            if opt not in range(1,3):
              print('\033[31m\nDigite apenas opções válidas\n\033[m')
            else: 
              break
          except:
            print('\033[31m\nDigite apenas opções válidas\n\033[m')
        if opt == 1:
          print('Você segue Alessandro e vê ele chegando próximo da Daniel Nowak, estudante de BCC.\n\nEles começam a conversar em alemão.')
          #time.sleep(1.5)
          print('Você consegue se lembrar apenas da frase "Ich habe sie nicht ermordet".')
          while True:
            try:
              trans = int(input('O que deseja fazer?\n[1] - Traduzir "Ich habe sie nicht ermordet"\n[2] - Seguir em frente\nSua escolha: '))
              if trans not in range(1,3):
                print('\033[31m\nDigite apenas opções válidas\n\033[m')
              else: 
                if trans == 2:
                  break
                elif trans ==1: 
                  print('"Ich habe sie nicht ermordet" = "Eu não a matei"')
                  lados[2][2]+='"Eu não a matei."'
                  break
            except:
              print('\033[31m\nDigite apenas opções válidas\n\033[m')
        elif opt ==2: 
          print('Ele é difícil de desembuchar, provavelmente recebeu treinamento para isso\n\nA única coisa que diz: "Quem a matou tinha treinamento. Foi com uma arma de pequeníssimo porte, pois no corpo há apenas uma marca de perfuração. Provavelmente, coisa da KGB."')
          lados[2][2]+='"Isso é coisa da KGB"\nEle é um provável espião.'
        
          
      #elif p = 3:
      
      
      #elif p =4:
      
      #elif p =5:
      
      #elif p = 6:
      
      #elif p = 7:
      
      #elif p=8: 
      break

    elif option == '2' or option == 'INVESTIGAR':
      result_set = [False, False, False]
      print(tabulate(nomes, headers='firstrow', tablefmt='grid'))
      opt_1 = str(input('\nDigite o código ou o nome de quem deseja acusar: ')).upper()
      if opt_1 == '7' or opt in 'GIULIA CARVALHO':
        result_set[0] = True
      

      

def tempo():
  import time
  time.sleep(750)
t1 = Thread(target=tempo)
#while t1.is_alive():
