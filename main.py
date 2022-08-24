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
if saborPizza == 0:
      print(f'--------------------------------\n'
            f'Valor atual: R$ 0,0 {saborP0}\n'
            f'--------------------------------')
if saborPizza == 1:
      print(f'--------------------------------\n'
            f'Valor atual: R$ {saborP1}\n'
            f'--------------------------------')
elif saborPizza == 2:
      print(f'--------------------------------\n'
            f'Valor atual: R$ {saborP2}\n'
            f'--------------------------------')
