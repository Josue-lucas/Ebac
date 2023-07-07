# código de geração do gráfico 
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do arquivo CSV
df = pd.read_csv('gasolina.csv')

# Criar o gráfico de linha
plt.plot(df['dia'], df['venda'])

# Configurar os rótulos dos eixos
plt.xlabel('Dia')
plt.ylabel('Preço')

# Configurar o título do gráfico
plt.title('Preço da Gasolina ao Longo dos Dias')

# Salvar o gráfico no arquivo PNG
plt.savefig('gasolina.png')

# Exibir o gráfico 
plt.show()