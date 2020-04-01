#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 16:00:16 2020

@author: gabrielformario
"""

# EP Design de Software 2020-1 / 

"""""""""""""""


CRAPS INSPER


"""""""""""""""


# Imports necessários para realizar o EP
import random
import time  # Apenas para melhorar a visualização no terminal


dinheiro = 200 # Dinheiro inicial do jogador
print("Bem Vindo ao Craps Insper ! ")
# Começo do Loop do Jogo
while True:
    fase= "COME OUT"
    print()
    
    print(f'Seu total de fichas é {dinheiro}.' )
    if dinheiro == 0:
        print("Acabou o dindin =( ")
        break
    
    time.sleep(1)            
    print(f"Você esta na {fase}.")
    
    # Pergunta aposta para o jogador
    time.sleep(1)
    aposta = int(input("Faça uma aposta para poder jogar o game, digite 0 para sair: "))
    
    # Jogo para se ele digitar 0 ou menor que 0
    if aposta == 0 or aposta < 0:
        break
        
    elif aposta > dinheiro :
        print("Aposta maior que valor atual de moedas")
        aposta = int(input("Faça uma aposta para poder jogar o game, digite 0 para sair: "))
        
    # Pergunta quais opções de aposta jogador quer fazer     
    pergunta = input("Quais opções de aposta vc quer realizar ?\n 1. Pass Line Bet\n 2. Field\n 3. Any Craps\n" 
                  " 4. Twelve\nEscreva o número da opção para escolher o tipo de aposta: ")
    

# Opção Pass Line Bet de aposta
    if pergunta == '1':
        print()
        print("Se a soma dos dados lançados for 7 ou 11 o jogador ganha")
        time.sleep(2)
        print()
        print("Já se os dados somarem 2, 3 ou 12 (chamado de craps) o jogador perde")
        time.sleep(2)
        print()
        print("Já se a soma dos dados der 4, 5, 6, 8, 9 ou 10 o jogo muda para a fase de “Point” e o objetivo muda")
        time.sleep(2)
        print()
        print("Primeiro dado caiu ...")
        time.sleep(2)
        # Lançamento Dado 1
        dado1 = random.randint(1,6)
        print(dado1)
        
        
        time.sleep(1)
        print()
        print("Segundo dado caiu ...")
        time.sleep(2)
        # Lançamento Dado 2
        dado2 = random.randint(1,6)
        print(dado2)
        soma = dado1 + dado2
        print()
        time.sleep(2)
        print(f"Soma: {soma}")
        
        if soma == 7 or soma == 11:
            dinheiro += aposta
        elif soma == 2 or soma == 3 or soma ==12:
            dinheiro -= aposta
        
        # Mudança de Fase dentro do Pass Line Bet para Point
        else:
            fase_pos = 'POINT'
            fase = fase_pos
            time.sleep(2)
            print()
            print("Vc mudou de fase agora etá na fase POINT")
            print()
            print(f"Sua aposta continua valendo e agora o Point é {soma}")
            print()
            time.sleep(2)
            print("Se a nova soma dos dados é a mesma do que foi guardado no Point, o jogador ganha o mesmo valor que apostou")
            print()
            time.sleep(2)
            print("Se sair uma soma de valor 7 o jogador perde tudo")
            print()
            time.sleep(2)
            print(" Caso saia qualquer outro número, se mantem na fase de “Point” sem perder ou ganhar e se continua lançando os dados até um veredito, quando sair ou o número do Point ou o 7")
            
            # Loop dentro da Fase Point até que ele saia desta fase
            while True:
                
                print()
                print("Primeiro dado caiu ...")
                time.sleep(2)
                # Lançamento Dado 1 na fase Point
                dado3 = random.randint(1,6)
                print(dado3)
                time.sleep(1)
                print()
                print("Segundo dado caiu ...")
                time.sleep(2)
                # Lançamento Dado 2 na fase Point
                dado4 = random.randint(1,6)
                print(dado4)
                new_soma = dado3 + dado4
                print()
                time.sleep(2)
                print(f"Soma: {new_soma}")
                
                if new_soma == soma:
                    dinheiro += aposta
                    print("Muito bom vc ganhou !")
                    fase_pos = "COME OUT"
                    break
                    
                elif new_soma == 7:
                    print("Vc perdeu TUDO ! Que azar :/")
                    dinheiro = 0 
                    fase_pos = fase
                    break
                    
                else:
                    fase = fase_pos
        

                    
# Opção Field de aposta        
    elif pergunta == '2':
        print()
        print("Vc escolheu Field como opcao de aposta")
        print()
        time.sleep(2)
        print("Se os dados derem 5, 6, 7 ou 8 o jogador perde tudo")
        print()
        time.sleep(2)
        print("Já se derem 3, 4, 9, 10, ou 11 o jogador ganha o mesmo valor que apostou")
        print()
        time.sleep(2)
        print("Já se a soma for 2 o jogador ganha o dobro do que apostou")
        print()
        time.sleep(2)
        print("E finalmente se sai 12 nos dados o jogador ganha o triplo")
        
        time.sleep(1)
        print()
        print("Primeiro dado caiu ...")
        time.sleep(2)
        # Lançamento Dado 1
        dado1 = random.randint(1,6)
        print(dado1)
        
        
        time.sleep(1)
        print()
        print("Segundo dado caiu ...")
        time.sleep(2)
        # Lançamento Dado 2
        dado2 = random.randint(1,6)
        print(dado2)
        soma = dado1 + dado2
        print()
        time.sleep(2)
        print(f"Soma: {soma}")
        
        if soma == 5 or soma == 6 or soma == 7 or soma == 8:
            dinheiro = 0
            time.sleep(1)
            print()
            print("Que azar! Vc perdeu tudo! =(")
        
        elif soma == 3 or soma == 4 or soma == 9 or soma == 11 or soma == 10 or soma == 11:
            dinheiro += aposta
            
        elif soma == 2:
            dinheiro += 2*aposta
            
        else:
            dinheiro += 3*aposta
            
    
# Opção Any Craps de aposta    
    elif pergunta == '3':
        print()
        print("Vc escolheu Any Craps como opcao de aposta")
        print()
        time.sleep(2)
        print("Se o dados derem 2, 3 ou 12 o jogador ganha sete vezes o que apostou, senão perde a aposta")
        time.sleep(1)
        print()
        print("Primeiro dado caiu ...")
        time.sleep(2)
        # Lançamento Dado 1
        dado1 = random.randint(1,6)
        print(dado1)
        
        
        time.sleep(1)
        print()
        print("Segundo dado caiu ...")
        time.sleep(2)
        # Lançamento Dado 2
        dado2 = random.randint(1,6)
        print(dado2)
        soma = dado1 + dado2
        print()
        time.sleep(2)
        print(f"Soma: {soma}")
                
        if soma == 2 or soma == 3 or soma == 12:
            dinheiro += 7*aposta
            print("Que sorte! Vc ganhou 7X que apostou!")
            
            
        else:
            dinheiro = dinheiro 
            print()
            print("Vc perdeu sua aposta")
            
# Opção Twelve de aposta            
    elif pergunta == '4':
        print()
        print("Vc escolheu Twelve como opcao de aposta")
        print()
        time.sleep(2)
        print("Se o dados derem 12 o jogador ganha trinta vezes o que apostou, senão perde a aposta")
        time.sleep(1)
        print()
        print("Primeiro dado caiu ...")
        time.sleep(2)
        # Lançamento Dado 1
        dado1 = random.randint(1,6)
        print(dado1)
        
        
        time.sleep(1)
        print()
        print("Segundo dado caiu ...")
        time.sleep(2)
        # Lançamento Dado 2
        dado2 = random.randint(1,6)
        print(dado2)
        soma = dado1 + dado2
        print()
        time.sleep(2)
        print(f"Soma: {soma}")
        
        if soma == 12:
            print()
            print("Muita sorte!")
            dinheiro += 30*aposta
            
        else:
            dinheiro = dinheiro
            print()
            print("Vc perdeu sua aposta")
        
        
        

        

            