import numpy as np

dados = np.genfromtxt('c:/Users/catid/Downloads/Planilha_notas_alunos.csv', delimiter=';', names=True, dtype=None, encoding='utf-8')

notas = dados['nota_final']

media = np.mean(notas)
mediana = np.median(notas)

valores_unicos, contagens = np.unique(notas, return_counts=True)

indice_maior_frequencia = np.argmax(contagens)
moda = valores_unicos[indice_maior_frequencia]
desvio_padrao = np.std(notas)

q1 = np.percentile(notas, 25)
q2 = np.percentile(notas, 50) 
q3 = np.percentile(notas, 75)

print("-" * 35)
print("      RELATÓRIO ESTATÍSTICO")
print("-" * 35)
print(f"Média:         {media:.2f}")
print(f"Mediana:       {mediana:.2f}")
print(f"Moda:          {moda:.2f}")
print(f"Desvio Padrão: {desvio_padrao:.2f}")
print("-" * 35)
print(f"1º Quartil (Q1): {q1:.2f}")
print(f"2º Quartil(Q2):  {q2:.2f}")
print(f"3º Quartil (Q3): {q3:.2f}")
print("-" * 35)