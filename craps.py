#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 16:00:16 2020

@author: gabrielformario
"""

# EP Design de Software 2020-1

import random
import time 

dinheiro = 200
while True:
    fase= "COME OUT"
    print()
    print(f'Seu total de fichas é {dinheiro}.' )
    if dinheiro == 0:
        print("Acabou o dindin =( ")
        break
                
    print(f"Você esta na {fase}.")
        
    aposta = int(input("Faça uma aposta para poder jogar o game, digite 0 para sair: "))
    if aposta == 0 or aposta < 0:
        break
        
    elif aposta > dinheiro :
        print("Aposta maior que valor atual de moedas")
        
        
    pergunta = input("Quais opções de aposta vc quer realizar ?\n 1. Pass Line Bet\n 2. Field\n 3. Any Craps\n" 
                  " 4. Twelve\nEscreva o número da opção para escolher o tipo de aposta: ")


    if pergunta == '1':
        time.sleep(1)
        print()
        print("Primeiro dado caiu ...")
        time.sleep(2)
        dado1 = random.randint(1,6)
        print(dado1)
        
        
        time.sleep(1)
        print()
        print("Segundo dado caiu ...")
        time.sleep(2)
        dado2 = random.randint(1,6)
        print(dado2)
        soma = dado1 + dado2
        
        if soma == 7 or soma == 11:
            dinheiro += aposta
        elif soma == 2 or soma == 3 or soma ==12:
            dinheiro -= aposta
            
        else:
            fase_pos = 'POINT'
            fase = fase_pos
            time.sleep(2)
            print(f"Sua aposta continua valendo e agora o Point é {soma}")
            print()
            print(f"Agora vc está na fase {fase}, as coisas ficaram diferentes a partir de agora")
            
            while True:
                
                print()
                print("Primeiro dado caiu ...")
                time.sleep(2)
                dado3 = random.randint(1,6)
                print(dado3)
                time.sleep(1)
                print()
                print("Segundo dado caiu ...")
                time.sleep(2)
                dado4 = random.randint(1,6)
                print(dado4)
                new_soma = dado3 + dado4
                print()
                time.sleep(2)
                print(f"Soma = {new_soma}")
                
                if new_soma == soma:
                    dinheiro += aposta
                    fase_pos = "COME OUT"
                    break
                    
                elif new_soma == 7:
                    print("Vc perdeu TUDO ! Que azar :/")
                    dinheiro = 0 
                    fase_pos = fase
                    break
                    
                else:
                    fase = fase_pos
        

                    
        
    elif pergunta == '2':
        print("Vc escolheu Field como opcao de aposta")
        time.sleep(1)
        print()
        print("Primeiro dado caiu ...")
        time.sleep(2)
        dado1 = random.randint(1,6)
        print(dado1)
        
        
        time.sleep(1)
        print()
        print("Segundo dado caiu ...")
        time.sleep(2)
        dado2 = random.randint(1,6)
        print(dado2)
        soma = dado1 + dado2
        
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
            
            
            
            