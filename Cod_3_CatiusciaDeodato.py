import pandas as pd

df = pd.read_csv('c:/Users/catid/Downloads/Planilha_notas_alunos.csv', delimiter=';')

correl_estudo = df["horas_estudo"].corr(df["nota_final"])
correl_aulas = df["aulas_assistidas"].corr(df["nota_final"])

print("--- ANÁLISE DE CORRELAÇÃO ---")
print(f"Horas de Estudo x Nota Final: {correl_estudo:.4f}")
print(f"Aulas Assistidas x Nota Final: {correl_aulas:.4f}")