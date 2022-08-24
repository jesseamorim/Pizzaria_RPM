print('--->Bem Vindo a Pizzaria RPM<---')
print('--------------------------------')
print('-->Este é o nosso Cardápio! Deseja qual sabor?<--')
saborP1 = 15
saborP2 = 15
saborP3 = 10
saborP4 = 5
saborP5 = 5
saborP0 = 'Nenhum, desisti voltarei outra hora!'
# Sabor da Pizza
cont = 2
while cont == 2:
      saborPizza = int(input('1 - Pepperoni (+ R$ 15,00)\n '
      '(Molho de Tomate - Mussarela - Pepperoni)\n'
      '\n'      
      '2 - Quatro Queijos (+ 15,00)\n(Molho de Tomate - Mussarela - Parmesão - Provolone - Gorgonzola)\n'
      '\n'
      '3 - Frango e Catupiry (+ R$ 10,00)\n(Molho de Tomate - Mussarela - Frango Desfiado - Catupiry - Cebola)\n'
      '\n'
      '4 - Calabresa (+ R$ 5,00)\n(Molho de Tomate - Mussarela - Calabresa - Cebola)\n'
      '\n'
      '5 - Marguerita (+ R$ 5,00)\n(Molho de Tomate - Mussarela - Tomate - Mangericão)\n'
                       '\n'
                       '0 - Nenhum, desisti voltarei outra hora!\n'
                       '\n'
 
                       'Digite aqui o número: '))
      qtde_sabor = int(input('Prefere somente um sabor? Pode escolher até 2!\n'
                       'Digite aqui --> '))

      if saborPizza == 0:
            print(f'--------------------------------\n'
                  f'Valor atual: R$ 0,0 {saborP0}\n'
                  f'--------------------------------')
      if saborPizza == 1:
            if qtde_sabor == 1:
                  print('Ok! Voce escolheu apenas 1 sabor!')
                  print(f'--------------------------------\n'
                  f'Valor atual está: R$ {saborP1}\n'
                  f'--------------------------------')
            elif qtde_sabor == 2:
                  print('Ok! Voce escolheu 2 sabores!')
                  print(f'--------------------------------\n'
                        f'Valor atual está: R$ {saborP1 + 1}\n'
                        f'--------------------------------')

      elif saborPizza == 2:
            print(f'--------------------------------\n'
                  f'Valor atual: R$ {saborP2}\n'
                  f'--------------------------------')
      elif saborPizza == 3:
            print(f'--------------------------------\n'
                  f'Valor atual: R$ {saborP3}\n'
                  f'--------------------------------')
      elif saborPizza == 4:
            print(f'--------------------------------\n'
                  f'Valor atual: R$ {saborP4}\n'
                  f'--------------------------------')
      elif saborPizza == 5:
            print(f'--------------------------------\n'
                  f'Valor atual: R$ {saborP5}\n'
                  f'--------------------------------')