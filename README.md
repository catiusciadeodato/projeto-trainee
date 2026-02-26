# projeto-trainee

# Desafio Trainee - Catiuscia Deodato

Este repositório contém as resoluções para o desafio de trainee, focando em análise de dados acadêmicos e automação com Python.

## 📝 Respostas do Desafio

### 
Na comparação entre a planilha do excel e Python+Numpy, deu uma alteração de 0.25 a menos no 1º quartil e 0,25 a mais no 3º quartil. Isso ocorre porque o excel e o NumPy utilizam métodos ligeiramente diferentes para cálculo de quartis (interpolação estatística).

### Estatística Descritiva com Python + NumPy 

A análise estatística da variável nota_final permitiu compreender o comportamento geral do desempenho dos alunos na base de dados.

A média representa o desempenho médio da turma. É uma medida importante para avaliar o rendimento geral.

A mediana corresponde ao valor central da distribuição. Isso significa que 50% dos alunos possuem nota abaixo desse valor e 50% possuem nota acima. A mediana é especialmente útil quando há valores extremos, pois não sofre tanta influência quanto a média.

A moda indica a nota que aparece com maior frequência no conjunto de dados. Ela permite identificar qual foi o desempenho mais comum entre os alunos.

O desvio padrão mede o nível de dispersão das notas em relação à média. Quanto maior o desvio padrão, maior é a variação das notas.

Os quartis ajudam a entender como as notas estão distribuídas ao longo da amostra: Q1 (1º quartil): 25% dos alunos possuem nota abaixo desse valor, Q2 (2º quartil): corresponde à mediana, Q3 (3º quartil): 75% dos alunos possuem nota abaixo desse valor.

Essas medidas, em conjunto, permitem uma visão mais completa da distribuição das notas e fornecem base sólida para análises posteriores, como correlação e testes de hipótese.

### Análise de Correlação 
O coeficiente de correlação varia de -1 a +1. Próximo de +1 → forte correlação positiva; próximo de 0 → pouca ou nenhuma correlação; próximo de -1 → correlação negativa. Quanto mais horas de estudo ou mais aulas assistidas, maior tende a ser a nota final.

### Teste de Hipótese 
Separei os alunos em dois grupos específicos, quem estuda até 10 horas e quem estuda mais de 10 horas, para conseguir comparar duas realidades diferentes dentro da turma. Essa divisão foi feita porque, ao isolar os dados dessa forma, consigo tratar cada grupo como uma amostra independente. 

##  Tecnologias
- Python
- NumPy
- Pandas
- Excel