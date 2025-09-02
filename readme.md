# Gerenciamento de Agendas



Descrição:
APi desenvolvida para poder gerenciar a reserva de horários usando, django no backend, postgress de banco de dados e docker para rodar os containers do app.


# :hammer: Funcionalidades do projeto
- `Funcionalidade 1`: Criação de usuarios e sistema de login
- `Funcionalidade 1a`: permissões de usuários e de administradores separadas bem definidamente
- `Funcionalidade 2`: agendamento de horarios
- `Funcionalidade 2a`: campos de auditoria, softdelete, status, restauração e exclusão total 


# 📁 Acesso ao projeto
-Copie a url do repositório no github do projeto "https://github.com/VQuaresma/GerenciamentoDeAgendamentos"
-Abra seu terminal e digite o comando "git clone {url do projeto}"
-Após terminar de baixar digite o comando "ls" e se tudo tiver clonado com sucesso ira aparecer o nome do projeto
-Digite "cd {nome do projeto}" para entrar na pasta do projeto
-Digite "code ." para começar a iniciar ele 
-
# 🛠️ Abrir e rodar o projeto

Iniciar Ambiente virtual:
    - primeiro crie um ambiente virtual
    No Windows:
        python -m venv venv
        .\venv\Scripts\Activate.ps1
    No Linux: 
        python3 -m venv venv
        source venv/bin/activate

Subir Containers docker:
    -Após configurar seu dockerfile e o docker-compose.yml você pode subir seus containers para funcionamento da api.
        -Rode o comando "docker-compose up" ( isso vai construir as imagens[se a primeira vez rodando ] e subir todos os containers definidos no seu docker-compose.yml)
        -Para rodar sem travar os terminais rode "docker-compose up -d"
        -Não sera necessario fazer as instalações das bibliotecas, pois no seu dockerfile ( se não foi alterado ) o docker ja roda comandos para baixar e iniciar a aplicação.

Acessar a API:
    -Você pode acessar http://127.0.0.1:8000/swagger/ para visualizar a documentação da API ou http://127.0.0.1:8000/redoc/




