# APS3FlaskPostgre
[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/AqMWIgvG)
# Exercício de Web Services REST com Flask e PostgreSQL

Neste exercício, você aprimorará a aplicação web da biblioteca que foi desenvolvida anteriormente, agora incorporando os princípios REST até o Nível 2 do Modelo de Maturidade de Richardson. A aplicação deve continuar gerenciando livros e usuários, mas agora com uma abordagem mais padronizada e alinhada com as práticas RESTful. Além disso, você preparará seu projeto para um possível deploy no Heroku.

## Requisitos:

1. **Estrutura de Pastas**:
    - Mantenha a estrutura anterior, garantindo a presença do arquivo principal `app.py` e a pata com a colection atualizada do POSTMAN.

2. **Recursos e Verbos HTTP**:
    - Seus endpoints devem ser organizados em torno de recursos (por exemplo, `/livros` e `/usuarios`).
    - Utilize os verbos HTTP para representar ações CRUD sobre esses recursos: 
        - **GET** para leitura.
        - **POST** para criação.
        - **PUT** para atualização.
        - **DELETE** para exclusão.
    - Garanta que os códigos de status HTTP sejam usados de forma adequada para representar o resultado de cada operação.

3. **Endpoints RESTful**:
    - As rotas e métodos devem seguir o padrão RESTful. Por exemplo:
        - **GET** `/livros`: Lista todos os livros.
        - **POST** `/livros`: Adiciona um novo livro.
        - **GET** `/livros/1`: Obtém detalhes do livro com ID 1.
        - **PUT** `/livros/1`: Atualiza o livro com ID 1.
        - **DELETE** `/livros/1`: Exclui o livro com ID 1.
    - Siga a mesma lógica para o recurso `/usuarios`.

4. **Testando com Postman**:
    - Crie uma collection no Postman para testar todos os endpoints.
    - Após realizar os testes, exporte a collection atualizada:
        1. No Postman, clique com o botão direito na collection que você criou.
        2. Selecione "Export".
        3. Escolha a versão do formato (recomendamos a versão 2.1).
        4. Clique em "Export" e salve o arquivo na pasta `postman` do projeto.
    - **ATENÇÃO**: A exportação da collection atualizada é essencial e vale pontos. Certifique-se de substituir o arquivo existente na pasta `postman`.

5. **Preparação para Deploy no Heroku**:
    - Prepare seu repositório para um possível deploy no Heroku. Embora o deploy em si não seja necessário neste exercício, é essencial que o repositório esteja corretamente preparado para tal.
    - Adicione um arquivo `requirements.txt` contendo todas as bibliotecas e dependências necessárias para executar sua aplicação. Este arquivo é crucial para que o Heroku saiba quais pacotes instalar.
    - Crie um arquivo chamado `Procfile` (sem extensão) na raiz do seu projeto. Este arquivo é usado pelo Heroku para determinar como iniciar sua aplicação. Não se esqueça que para executar o webservice com robustez é necessario ter gunicorn em suas configurações.

## Observações:

- Ao refatorar sua aplicação para adotar os princípios REST, você estará operando no Nível 2 do Modelo de Maturidade de Richardson.
- Lembre-se de que, no Nível 2, é importante não apenas usar verbos HTTP, mas também garantir que os códigos de status HTTP sejam usados corretamente.
- Dê atenção especial à organização dos seus endpoints, garantindo que eles estejam alinhados com os princípios RESTful.


## Fonte de Informação

### Ajuda com a plataforma ElephantSQL

- Introdução e Configurações Iniciais: https://www.elephantsql.com/blog/databases-for-beginners-what-is-a-database-what-is-postgresql.html

- Conectando o pgAdmin ao seu server Elephant: https://www.elephantsql.com/docs/pgadmin.html

- Documentação oficial: https://www.elephantsql.com/docs/index.html

### Ajuda com pgAdmin

- Introdução ao pgAdmin: https://www.w3schools.com/postgresql/postgresql_pgadmin4.php

- Documentação oficial: https://www.pgadmin.org/docs/pgadmin4/8.3/index.html

### Ajuda com o Python utilizando a base PostgreSql (psycog2)

- Tutorial excelente sobre psycog2: https://www.tutorialspoint.com/postgresql/postgresql_python.htm

- Documentação oficial: https://www.psycopg.org/docs/

### Ajuda com Flask

- Intro: https://www.tutorialspoint.com/flask/flask_application.htm

- Recebendo JSON via requisição: https://stackabuse.com/how-to-get-and-parse-http-post-body-in-flask-json-and-form-data/

- Variáveis na URL (urls dinâmicas): https://www.geeksforgeeks.org/generating-dynamic-urls-in-flask/

- Query Parameters: https://stackabuse.com/get-request-query-parameters-with-flask/

- Documentação oficial: https://flask.palletsprojects.com/en/3.0.x/

### Ajuda com Postman

- Intro: https://learning.postman.com/docs/getting-started/first-steps/sending-the-first-request/

- Importando uma collection: https://learning.postman.com/docs/getting-started/importing-and-exporting/importing-data/


### Ajuda com Heroku

- Criando conta estudante no Heroku (precisa de cartão): https://youtu.be/aSdx43pesV4?si=PvvuopBh5rUpMa2R
- Fazendo deploy no Heroku: https://youtu.be/OU_Fqt1pBPM?si=F4jPWgEXyigcIYBQ
- Deploy de Flask no Heroku - Alt 1: https://github.com/datademofun/heroku-basic-flask 


### Busque outras fontes

Fique a vontade para procurar vídeos no youtube caso ache necessário, muitas pessoas aprendem melhor com vídeos.

O ChatGPT usado corretamente pode se tornar um grande parceiro de aprendizado, e te ajudar com conceitos que talvez ainda não estejam tão claros para você, pergunte sobre as ferramentas, integrações e papel de cada um dos elementos presentes nesta tarefa, só não peça por código. Não tome o caminho mais fácil, isso irá te prejudicar mais do que você imagina.