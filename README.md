# Aplicação de gerenciamento de vendas de veículos

Aplicação do teste para seleção de trainee na [Devnology](https://devnology.com.br/)

Demo da aplicação rodando no [Heroku](https://www.heroku.com/):

https://django-vehicle-manager.herokuapp.com/

## Tecnologias utilizadas:
* Python
* [Django](https://www.djangoproject.com/)
* [Django Rest Framework](https://www.django-rest-framework.org/)
* [Bootstrap](https://getbootstrap.com/)
* Javascript
* [jQuery](https://jquery.com/)
* [PostgreSQL](https://www.postgresql.org/)
* [Docker](https://www.docker.com/)


### Iniciar aplicação usando [Docker](https://www.docker.com/) (recomendado):
```bash
 docker-compose up
```
O docker fará o build de uma imagem personalizada com as dependências necessárias, em seguida, o servidor de desenvolvimento estará acessível em: [http://localhost:8000](http://localhost:8000). Além do container rodando a aplicação python, o docker-compose também cria um container para o PostgreSQL (banco de dados usado pela aplicação).

### Iniciar a aplicação sem usar Docker:

- Instalação das dependências (é recomendado usar um virtual env):
```bash
 pip install -r requirements.txt
```
Em seguida é preciso instalar o postgres, criar uma base de dados para a aplicação e configurar as credenciais do banco como variáveis de ambiente no arquivo .env.

- Rodar migrations, seed do banco e iniciar servidor:
```bash
 python manage.py migrate &&
 python  manage.py loaddata seed_vehicles.json &&
 python manage.py runserver 0.0.0.0:8000
```
O servidor de desenvolvimento estará acessível em: [http://localhost:8000](http://localhost:8000).

## Solução proposta

A solução proposta foi uma aplicação web construída usando Django e o Django Rest Framework. O Django faz a renderização dos templates e a API fornece uma interface de acesso ao banco de dados.

* Tela Dashboard: Nessa tela é apresentado um resumo das informações de 
  vendas, compras, lucro, comissões. Além disso, todos os veículos 
  (disponíveis para venda ou não) são listados. As informações de lucro 
  podem ser filtradas de acordo com intervalos de tempo (última semana, 
  último mês, último semestre e desde o início).
![image](https://user-images.githubusercontent.com/52494917/124048288-5c5c6380-d9ec-11eb-91c1-067b665b1f1e.png)

* Tela Veículos: Tela responsável por listar os veículos disponíveis para venda, bem como adição de um novo veículo (nova compra), remoção, edição e realização de uma venda.
![image](https://user-images.githubusercontent.com/52494917/124048623-210e6480-d9ed-11eb-84fe-2d8289b5a7a5.png)

* Tela Vendas: Apresenta o histórico de vendas, o usuário pode alterar os dados de uma venda, visualizar detalhes e cancelar uma venda. Ao cancelar uma venda o veículo volta para tela de veículos disponíveis.
![image](https://user-images.githubusercontent.com/52494917/124049116-2d46f180-d9ee-11eb-8297-8f82e304903b.png)

## API
* Endpoint para consultar veículos (GET)```/api/vehicles```
* Endpoint para alterar (PUT, PATCH), remover (DELETE) ou consultar (GET) um veículo específico```/api/vehicles/{id}```
* Endpoint para consultar informações de lucro, compras, vendas e comissões dado um intervalo (month, week, begin, semester) ```/api/profits?interval=month```

## Deploy
O deploy da aplicação foi feito usando o Heroku, para tal foi preciso configurar o comando que inicia o gunicorn no Procfile e o arquivo runtime.txt com a versão do python usada na aplicação. Além disso, o pacote para python django-heroku foi usado, esse pacote ajuda no processo de deploy de uma aplicação Django para o heroku.

Demo da aplicação rodando no [Heroku](https://www.heroku.com/):

https://django-vehicle-manager.herokuapp.com/

