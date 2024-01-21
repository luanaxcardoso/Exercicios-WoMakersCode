# 6- Escreva um programa que calcule o tempo de uma viagem. Faça um comparativo do mesmo percurso de avião,carro e ônibus.Levando em consideração:
# ●avião=600km/h 
# ●carro=100km/h 
# ●ônibus=80km/h

def calcular_tempo_viagem(distancia, velocidade):
    tempo = distancia / velocidade
    return tempo

distancia = float(input("Digite a distância da viagem em quilômetros: "))

velocidade_aviao = 600  
velocidade_carro = 100  
velocidade_onibus = 80   

tempo_aviao = calcular_tempo_viagem(distancia, velocidade_aviao)
tempo_carro = calcular_tempo_viagem(distancia, velocidade_carro)
tempo_onibus = calcular_tempo_viagem(distancia, velocidade_onibus)

print(f"Tempo de viagem de avião: {tempo_aviao:.2f} horas")
print(f"Tempo de viagem de carro: {tempo_carro:.2f} horas")
print(f"Tempo de viagem de ônibus: {tempo_onibus:.2f} horas")
