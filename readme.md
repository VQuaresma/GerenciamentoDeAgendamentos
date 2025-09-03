💻 Gerenciamento de Agendas
API desenvolvida para gerenciar a reserva de horários. O projeto utiliza Django para o backend, PostgreSQL como banco de dados e Docker para a containerização da aplicação.

:hammer: Funcionalidades
Gerenciamento de usuários:

Criação de usuários e sistema de login.

Permissões de administrador e usuário bem definidas.

Agendamento de horários:

Agendamento de horários.

Campos de auditoria, soft delete, status, restauração e exclusão total.

📁 Acesso ao projeto
Clone o repositório:
Abra seu terminal e execute o comando:

Bash

git clone https://github.com/VQuaresma/GerenciamentoDeAgendamentos.git
Acesse a pasta do projeto:

Bash

cd GerenciamentoDeAgendamentos
Abra o projeto no VS Code (opcional):

Bash

code .
🛠️ Como rodar o projeto
1. Iniciar o ambiente virtual
Windows:

Bash

python -m venv venv
.\venv\Scripts\Activate.ps1
Linux:

Bash

python3 -m venv venv
source venv/bin/activate
2. Subir os containers do Docker
Seus containers serão iniciados automaticamente e as dependências serão instaladas via Dockerfile (caso não tenha sido alterado).

Para iniciar os containers em segundo plano, use:

Bash

docker-compose up -d
Se preferir, para visualizar os logs no terminal, use:

Bash

docker-compose up
3. Acessar a API
Após o Docker estar em execução, você pode acessar a documentação da API em:

Swagger: http://127.0.0.1:8000/swagger/

Redoc: http://127.0.0.1:8000/redoc/