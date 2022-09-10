from time import sleep
traço = 50*"-"
print('--->Bem Vindo a Pizzaria RPM<---')
print(traço)
print('-->Este é o nosso Cardápio! Deseja qual sabor?<--')
saborP1 = 15
saborP11 = ('1 - Pepperoni (+ R$ 15,00)\n'
      '(Molho de Tomate - Mussarela - Pepperoni)')
saborP2 = 15
saborP22 = ('2 - Quatro Queijos (+ 15,00)\n'
            '(Molho de Tomate - Mussarela - Parmesão - Provolone - Gorgonzola)')
saborP3 = 10
saborP33 = ('3 - Frango com Catupiry (+ R$ 10,00)\n'
            '(Molho de Tomate - Mussarela - Frango Desfiado - Catupiry - Cebola)')
saborP4 = 5
saborP44 = ('4 - Calabresa (+ R$ 5,00)\n'
            '(Molho de Tomate - Mussarela - Calabresa - Cebola)\n')
saborP5 = 5
saborP55 = ('5 - Marguerita (+ R$ 5,00)\n'
            '(Molho de Tomate - Mussarela - Tomate - Mangericão)\n')
saborP0 = 'Nenhum, desisti voltarei outra hora!'
sabAtual = ""
valAtual = 0
sleep(4)
# Tamanho da Pizza (valor)
tamP1 = 15
tamP11 = ('1 - Pequeno (+ R$ 15,00)')
tamP2 = 20
tamP22 = ('2 - Média (+ R$ 20,00)')
tamP3 = 25
tamP33 = ('3 - Grande (+ R$ 25,00)')
tamP4 = 30
tamP44 = ('4 - Família (+ R$ 30,00)')

saborPizza = int(input(f'{saborP11}\n'
                       f'\n{saborP22}\n'
                       f'\n{saborP33}\n'
                       f'\n{saborP44}\n'
                       f'\n{saborP55}\n'
                       f'Digite aqui o número: '))

# Sabor da Pizza
if saborPizza == 0:
      print(traço)
      print('Ok, até logo!!!')
      print(traço)
elif saborPizza == 1:
      print(traço)
      print('Voce escolheu o sabor -->\n'
            f'{saborP11} ')
      sabAtual += saborP11
      valAtual += saborP1
      print(f'Valor atual está: R$ {valAtual},00')
      print(traço)
elif saborPizza == 2:
      print(traço)
      print('Voce escolheu o sabor -->\n'
            f'{saborP22} ')
      valAtual += saborP2
      print(f'Valor atual está: R$ {valAtual},00')
      print(traço)
elif saborPizza == 3:
      print(traço)
      print('Voce escolheu o sabor -->\n'
            f'{saborP33} ')
      valAtual += saborP3
      print(f'Valor atual está: R$ {valAtual},00')
      print(traço)
elif saborPizza == 4:
      print(traço)
      print('Voce escolheu -->\n'
            f'{saborP44} ')
      valAtual += saborP4
      print(f'Valor atual está: R$ {valAtual},00')
      print(traço)
elif saborPizza == 5:
      print(traço)
      print('Voce escolheu o sabor -->\n'
            f'{saborP55} ')
      valAtual += saborP5
      print(f'Valor atual está: R$ {valAtual},00')
      print(traço)
else:
      print(traço)
      print(f'Tente novamente, digite numeros de 1 a 4.')
      print(traço)

# TAMANHO DA PIZZA
print('-->Agora, qual é o tamanho da Pizza?<--')

tamanhoPizza = int(input(f'{tamP11}\n'
                       f'\n{tamP22}\n'
                       f'\n{tamP33}\n'
                       f'\n{tamP44}\n'
                       f'Digite aqui o número: '))

if tamanhoPizza == 0:
      print(traço)
      print('Ok, até logo!!!')
      print(traço)
elif tamanhoPizza == 1:
      print(traço)
      print('Voce escolheu tamanho -->\n'
            f'{tamP11} ')
      valAtual += tamP1
      print(f'Valor atual está: R$ {valAtual},00')
      print(traço)
elif tamanhoPizza == 2:
      print(traço)
      print('Voce escolheu tamanho -->\n'
            f'{tamP22} ')
      valAtual += tamP2
      print(f'Valor atual está: R$ {valAtual},00')
      print(traço)
elif tamanhoPizza == 3:
      print(traço)
      print('Voce escolheu tamanho -->\n'
            f'{tamP33} ')
      valAtual += tamP3
      print(f'Valor atual está: R$ {valAtual},00')
      print(traço)
elif tamanhoPizza == 4:
      print(traço)
      print('Voce escolheu tamanho -->\n'
            f'{tamP44} ')
      valAtual += tamP4
      print(f'Valor atual está: R$ {valAtual},00')
      print(traço)
else:
      print(traço)
      print(f'Tente novamente, digite numeros de 1 a 4.')
      print(traço)
print(f'{sabAtual}\nR$ {valAtual},00')