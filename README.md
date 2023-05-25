# Chatbot do Telegram - APizzaS

Este é um projeto de um chatbot desenvolvido em Python que simula o atendimento de uma pizzaria através do Telegram. O chatbot permite que os usuários façam pedidos de pizzas, consultem o menu, personalizem seus pedidos e obtenham informações sobre a pizzaria.

## Funcionalidades Principais
* Menu de pizzas: os usuários podem visualizar o menu completo da pizzaria, incluindo os sabores disponíveis, ingredientes e preços.

* Personalização de pedidos: os usuários têm a opção de personalizar suas pizzas, escolhendo os ingredientes desejados.

* Cálculo de preço: o chatbot calcula o preço total do pedido com base nas escolhas do usuário.

* Gerenciamento de pedidos: os pedidos dos usuários são registrados e armazenados para posterior processamento pela equipe da pizzaria.

* Integração com atendentes: o chatbot permite que os usuários solicitem atendimento de um atendente humano, caso necessitem de assistência adicional.

## Tecnologias Utilizadas
* Python: linguagem de programação utilizada para desenvolver o chatbot.

* pyTelegramBotAPI: biblioteca Python que facilita a interação com a API do Telegram.

* UML: utilizamos diagramas UML, como o diagrama de casos de uso, para modelar e representar a interação do chatbot com os usuários.

## Como Usar

* Clone o repositório para o seu ambiente de desenvolvimento local:
`git clone https://github.com/JoaoRodCruz/APS_Chatbot.git`

* Instale as dependências necessárias:
`pip install -r requirements.txt`

* Configure as credenciais do bot do Telegram:

* Crie um novo bot no Telegram através do BotFather.

* Copie o token do bot gerado.

* Cole o token do bot no arquivo config.py:
`TOKEN = "seu-token-do-bot"`

* Execute o script principal:
`APS_Chatbot.py`

* Inicie uma conversa com o bot no Telegram e experimente as funcionalidades disponíveis.

## Contribuição

Contribuições são bem-vindas! Se você quiser contribuir para este projeto, siga as etapas abaixo:

*Faça um fork do repositório.

*Crie uma nova branch para a sua funcionalidade ou correção:
`git checkout -b nova-funcionalidade`

*Faça as alterações necessárias e adicione os commits:
`git commit -m "Adiciona nova funcionalidade"`

*Envie as alterações para o seu fork:
`git push origin nova-funcionalidade`

*Abra um pull request no repositório original.