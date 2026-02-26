import pandas as pd

df = pd.read_csv('c:/Users/catid/Downloads/Planilha_notas_alunos.csv', delimiter=';')

grupo_ate_10 = df[df["horas_estudo"] <= 10]
grupo_mais_10 = df[df["horas_estudo"] > 10]

media_ate_10 = grupo_ate_10["nota_final"].mean()
media_mais_10 = grupo_mais_10["nota_final"].mean()

print(f"Média de notas (Até 10h): {media_ate_10:.2f}")
print(f"Média de notas (Mais de 10h): {media_mais_10:.2f}")