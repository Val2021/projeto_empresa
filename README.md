# 🚀 Projeto Empresa

Projeto elaborado como parte do programa Luiza Code.
A versão utilizada para desenvolvimento foi Python 3.8
A versão do banco de dados foi MongoDB 4.4.8 Community Standalone
MongoDB 4.4.8 Community

## 🛠 Preparação o projeto
### Pré-requisitos:
- [Python 3.8](https://www.python.org/)
- [MongoDB 4](https://docs.mongodb.com/)
- [Docker version 20.10.8](https://www.docker.com/)

### Clonando o repositório
    https://github.com/Val2021/projeto_empresa.git
### Criando ambiente virtual
    python3 -m venv nome_do_ambiente_virtual

### Ativar ambiente virtual:
#### No linux
    source nome_do_ambiente_virtual/bin/activate
#### No Windows
    nome_do_ambiente_virtual\Scripts\ActivateDependências

### Instalar as dependências do projeto com o comando:
    pip install -r requirements.txt

### Iniciando banco de dados - Mongo Community Tutorial
#### No linux
    https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
#### Principais comandos
    systemctl start mongod
    systemctl stop mongod
    systemctl restart mongod

#### No Windows
    https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/

## 🎲 Rodando o backend (servidor)
    python manage.py runserver

O servidor será iniciado na porta: 8000

    Run 'python manage.py migrate' to apply them.
    September 26, 2021 - 13:05:15
    Django version 3.2.7, using settings 'projeto_luizalabs.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

### Features
- [x] Cadastro de empresas
- [x] Cadastro de produtos

## 🚀 Deploy
Dockerfile
 
    docker pull alicepass/app-magalu:v4
    docker run -itd -p 80:8000 --name app-magalu alicepass/app-magalu:v4
    
Após o deploy acessar no browser: 127.0.0.1


## 🚀 Aplicação em Nuvem
O deploy da aplicação também foi realizado no Google Cloud Plataform

Para subir a imagem no GCP:
 
    docker pull alicepass/app-magalu:v4
    docker tag alicepass/app-magalu:v4 gcr.io/earnest-coder-326622/alicepass/app-magalu:v4
    docker push gcr.io/earnest-coder-326622/alicepass/app-magalu:v4
    
A aplicação pode ser acessada em:
- [Magalu](http://35.222.91.178/)
    

## Contribuidores:
<table>
  <tr>
    <td align="center">
        <a href="https://github.com/alice-passarelli">
            <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/89952137?v=4" width="100px;" alt=""/>
            <br /><sub><b>Alice Passarelli</b></sub></a><br />
    </td>
    <td align="center">
        <a href="https://github.com/marianac-campos">
        <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/69722854?v=4" width="100px;" alt=""/>
        <br /><sub><b>Mariana Camposo</b></sub></a><br />
    </td>
    <td align="center">
        <a href="https://github.com/micaelevieira">
        <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/22177634?v=4" width="100px;" alt=""/>
        <br /><sub><b>Micaele Vieira</b></sub></a><br />
    </td>
    <td align="center">
        <a href="https://github.com/nayara06">
        <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/90937416?v=4" width="100px;" alt=""/>
        <br /><sub><b>Nayara Chieregato</b></sub></a><br />
    </td>
    <td align="center">
        <a href="https://github.com/Val2021">
        <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/63678413?v=4" width="100px;" alt=""/>
        <br /><sub><b>Val Araújo</b></sub></a><br />
    </td>
  </tr>
</table>
