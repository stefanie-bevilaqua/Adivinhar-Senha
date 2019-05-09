#Por Stefanie Caroline Bevilaqua
#IFC Campus Concórdia 2019
#=======================================================
#______________Jogo__da__Loteria________________________
import random #Gera números aleatórios
import sys #Para sair do programa
#_______________________________________________________
r1=random.randint(0,9);r2=random.randint(0,9);r3=random.randint(0,9);r4=random.randint(0,9);r5=random.randint(0,9)
digitos='{}{}{}{}{}'.format(r1,r2,r3,r4,r5)
tentativas=0
numeros=0
jogador=''
teste=0
global jogada
global expoente
global mostra
mostra=''
expoente=0
print('_____________Jogo__da__Loteria___________')
print('')
print('*****Lembre-se:*****')
print('Se o dígito está contido na senha mas não está na mesma posição aparecerá "0"')
print('Se o dígito não está na senha aparecerá "-1"')
print('Se o dígito está contido na senha e está na mesma posição aparecerá "+1"')
print('Você tem 10 tentativas!')
print('')
print('=========================================')
print('Preparad@? Vamos começar!!!')
print('=========================================')
print('')
while tentativas<10: #Para definir quantas chances, e repetir até acabarem
    jogador=input('Digite uma senha com 5 dígitos: ')
    if len(jogador)>5 or len(jogador)<5:
        print('Senha Inválida')
#Caso os dígitos forem menores ou maiores que 5, aparece 'Senha inválida' repete e pedirá a té digitar corretamente
        continue
    while teste<5:#Verifica os dígitos escolhidos pelo jogador um a um para ver se estão na senha e em qual posição
        if jogador[expoente] == digitos[expoente] or jogador[expoente] == digitos[expoente] or jogador[expoente] == digitos[expoente] or jogador[expoente] == digitos[expoente] or jogador[expoente] == digitos[expoente]:
            mostra+=' +1 '#Mostra quando o número estiver na senha e no local certo
        elif jogador[expoente]==digitos[0] or jogador[expoente]==digitos[1] or jogador[expoente]==digitos[2] or jogador[expoente]==digitos[3] or jogador[expoente]==digitos[4]:
            mostra+=' 0 '#Mostra quando o número está na senha, mas não no lugar certo
        else:
            mostra += ' -1 '#Mostra quando não está na senha
        expoente+=1
        teste+=1
    if jogador == digitos:#Verifica se o jogador venceu
        print('Muito bom! Você acertou com {} tentativas'.format(tentativas))
        sys.exit()#Sai do programa
    print('Lembrete:', mostra)#Mostra o lembrete, que foi explicado no início do programa
    print('========================================')
    tentativas+=1
    print('Você já usou {} tentativas'.format(tentativas))
    print()
    #Zera as variáveis que terão que ter novos valores
    numeros=0
    mostra=''
    jogador=''
    teste=0
    expoente=0
if tentativas >=10:#Mostra quando acabarem as chances
    print('Que pena! Suas tentativas acabaram!')
