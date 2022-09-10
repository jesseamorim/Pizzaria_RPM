import Tamanho
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
saborP5 = 5
saborP0 = 'Nenhum, desisti voltarei outra hora!'
valAtual = 0
# Tamanho da Pizza (valor)
tamP1 = 15
tamP2 = 20
tamP3 = 25
tamP4 = 30

saborPizza = int(input('1 - Pepperoni (+ R$ 15,00)\n '
      '(Molho de Tomate - Mussarela - Pepperoni)\n'
      '\n'
      '2 - Quatro Queijos (+ 15,00)\n(Molho de Tomate - Mussarela - Parmesão - Provolone - Gorgonzola)\n'
      '\n'
      '3 - Frango com Catupiry (+ R$ 10,00)\n(Molho de Tomate - Mussarela - Frango Desfiado - Catupiry - Cebola)\n'
      '\n'
      '4 - Calabresa (+ R$ 5,00)\n(Molho de Tomate - Mussarela - Calabresa - Cebola)\n'
      '\n'
      '5 - Marguerita (+ R$ 5,00)\n(Molho de Tomate - Mussarela - Tomate - Mangericão)\n'
      '\n'
      '0 - Nenhum, desisti voltarei outra hora!\n'
      '\n'
      'Digite aqui o número: '))

# Sabor da Pizza
if saborPizza == 0:
      print(traço)
      print('Ok, até logo!!!')
      print(traço)
elif saborPizza == 1:
      print(traço)
      print('Voce escolheu -->\n'
            f'{saborP11} ')
      valAtual += saborP1
      print(f'Valor atual está: R$ {valAtual},00')
      print(traço)
elif saborPizza == 2:
      print(traço)
      print('Voce escolheu -->\n'
            f'{saborP22} ')
      valAtual += saborP2
      print(f'Valor atual está: R$ {valAtual},00')
      print(traço)
elif saborPizza == 3:
      print(traço)
      print('Voce escolheu -->\n'
            f'{saborP33} ')
      valAtual += saborP3
      print(f'Valor atual está: R$ {valAtual},00')
      print(traço)
elif saborPizza == 4:
      print(traço)
      print('Voce escolheu -->\n'
            f'{saborP22} ')
      valAtual += saborP2
      print(f'Valor atual está: R$ {valAtual},00')
      print(traço)
elif saborPizza == 5:
      print(traço)
      print('Voce escolheu -->\n'
            f'{saborP22} ')
      valAtual += saborP2
      print(f'Valor atual está: R$ {valAtual},00')
      print(traço)
else:
      print(traço)
      print(f'Tente novamente, digite numeros de 1 a 4.')
      print(traço)
print(valAtual)