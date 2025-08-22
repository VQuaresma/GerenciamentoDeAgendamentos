# Usa uma imagem leve do Python
FROM python:3.12-slim

# Cria a pasta de trabalho dentro do container
WORKDIR /app

# Copia o requirements.txt e instala as dependências
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copia todo o projeto para dentro do container
COPY . .

# Expõe a porta que o Django vai usar
EXPOSE 8000

# Comando padrão para rodar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
