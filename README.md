## Sistema de visão computacional
**Tem outro repositório com a mesma ideia feito em [Go](https://github.com/eltonCasacio/gocv), de uma olhada  ;]** 

### Executando

1. clone esse repositorio
2. dentro do projeto execute: `python -m venv .venv` para criar ambiente virtual
3. se estiver utilizando macbook, rode `source .venv/bin/activate`, windows `.venv/bin/activate` para ativar o ambiente virtual
4. caso necessário, instale essas dependencias:
   - `pip install Flask-Cors`
   - `pip install imutils`
   - `pip install pycomm3` 
   - `pip install rich`  
   - `pip install pymysql`
5. suba a imagem do mysql executando `docker-compose up`
6. o banco de dados será criado altomaticamente, mas será necessario criar as tabelas
   - para isso, vamos:
   - no terminal, execute esses comandos:
     - `docker-compose exec mysql bash` para entrar no terminal do container mysql
     - `mysql -u root -p` para entrar no terminal do mysql como root e digitar a senha. (as informacoes de acesso podem ser encontradas no arquivo docker-compose.yaml)
     - `show databases` para ver os bancos de dados. na lista voce vai ver nosso BD, db_opencvroboxyzdell
     - `use db_opencvroboxyzdell` para selecionar o bd que iremos trabalhar
     - execute os camandos de criacao das tabelas. (veja o arquivo src/database/arquivo db.sql)
8. entre no diretorio src e execute `python app.py -i localhost -o 8000`
9. server up on http://localhost:8000

***Veja o repositorio do front*** [aqui](https://github.com/eltonCasacio/opencv_front_dell)  
