# Use uma imagem base leve do Python
FROM python:3.9-slim

# Defina o diretório de trabalho no container
WORKDIR /visualization

# Copie o arquivo de dependências para o container
COPY requirements.txt .

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante dos arquivos do projeto
COPY visualization/ /visualization

# Expõe a porta padrão do Streamlit
EXPOSE 8501

# Define o comando para rodar a aplicação Streamlit
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]