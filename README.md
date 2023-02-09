# Flask ChatGPT 🤖

> ### <p>Este projeto consiste em uma aplicação simples de Flask que usa o API do OpenAI para completar frases.</p>

### Pré-requisitos 📋

### Antes de começar, você precisará ter instalado em sua máquina:

    Python 3
    Flask
    Openai

### Instalação 🔧

### Clone o repositório do GitHub com o seguinte comando:
    
    git clone https://github.com/OtavioWc7/mychatgpt-023.git

### Instale as dependências com o seguinte comando:

    pip install -r requirements.txt

### Adicione sua chave de API do OpenAI no arquivo .env

    KEY_ = SUA_CHAVE

### Execute o arquivo main.py com o seguinte comando:

    python app.py

### Abra o navegador e acesse o endereço http://localhost:5000/

## Como funciona 💻

### A aplicação funciona da seguinte maneira:

<p>O usuário acessa a página inicial (http://localhost:5000/), que exibe um formulário HTML para digitar a frase.
Quando o usuário submete o formulário, o servidor Flask recebe a solicitação e usa o API do OpenAI para completar a frase.
O servidor Flask retorna a resposta do API do OpenAI à página inicial, que é exibida na tela.</p>

### Arquivos importantes 📁

    main.py: Contém o código da aplicação Flask
    templates/index.html: Contém o HTML da página inicial
    requirements.txt: Contém a lista de dependências do projeto
    .env: Contém a chave de API do OpenAI

# Conclusão 🎉

> <p> Este projeto é uma ótima maneira de aprender sobre Flask e API do OpenAI! Tente personalizá-lo e adicionar novas funcionalidades. Boa sorte! 😉 </p>
