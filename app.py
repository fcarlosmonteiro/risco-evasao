''''
Renda Baixa e Raça Preta: Risco de evasão aumentado (entre 0.6 e 0.9).
Renda Média e Raça Preta: Risco de evasão alto (entre 0.7 e 0.9).
Renda Alta e Raça Preta: Risco de evasão moderado (entre 0.6 e 0.8).
Renda Baixa e Raça Parda: Risco de evasão moderado (entre 0.3 e 0.5).
Renda Média e Raça Parda: Risco de evasão baixo a moderado (entre 0.2 e 0.4).
Renda Alta e Raça Parda: Risco de evasão baixo (entre 0.1 e 0.3).
Outras situações: Risco de evasão geralmente baixo (entre 0.1 e 0.2).
'''
from flask import Flask, render_template
import pandas as pd
import plotly.offline as pyo
import plotly.express as px

app = Flask(__name__)

# Carregue os dados
df = pd.read_csv('dataset.csv')

# Crie os gráficos
def criar_grafico_contagem_alunos(df):
    contagem_por_idade_sexo = df.groupby(['Idade', 'Sexo']).size().reset_index(name='Contagem')
    
    fig = px.bar(contagem_por_idade_sexo, x='Idade', y='Contagem', color='Sexo',
                 title='Contagem de Alunos por Idade e Sexo',
                 labels={'Contagem': 'Quantidade de Alunos'})
    
    return fig

def criar_grafico_risco_evasao(df):
    fig = px.scatter(df, x='Idade', y='RiscoEvasao', color='Sexo', symbol='Raca',
                     title='Risco de Evasão por Idade, Sexo e Raça',
                     labels={'RiscoEvasao': 'Risco de Evasão'})
    
    return fig

fig_contagem_alunos = criar_grafico_contagem_alunos(df)
fig_risco_evasao = criar_grafico_risco_evasao(df)

# Salve os gráficos em arquivos HTML temporários
pyo.plot(fig_contagem_alunos, filename='static/contagem_alunos.html', auto_open=False)
pyo.plot(fig_risco_evasao, filename='static/risco_evasao.html', auto_open=False)

# Rota para exibir os gráficos
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
