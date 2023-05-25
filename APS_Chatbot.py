import telebot

# Token do seu bot do Telegram
TOKEN = 'SEU_TOKEN_DO_BOT'

# Criando uma instância do bot
bot = telebot.TeleBot(TOKEN)

# Comandos disponíveis para o bot
comandos_disponiveis = {
    '/cardapio': '🍕Mostrar nosso cardápio',
    '/pedido': '😋Faça um pedido',
    '/ajuda': '👋Está com dúdivdas? Chame um atendente',
    '/comandos': '❗Mostra a lista de comandos',
    '/horario': '🕡Veja nosso horário de funcionamento'
}

# Cardápio da pizzaria
cardapio = {
    'pizzas_salgadas': {
        'mussarela':{
            'ingredientes': ['mussarela', 'rodelas de tomate', 'orégano'],
            'preco': 30.00
        },
        'escarola':{
            'ingredientes': ['escarola refogada', 'mussarela', 'orégano'],
            'preco': 30.00
        },
        'atum':{
            'ingredientes': ['mussarela', 'atum', 'cebola', 'orégano'],
            'preco': 30.00
        },
        'calabresa':{
            'ingredientes': ['mussarela', 'linguiça calabresa', 'cebola'],
            'preco': 30.00
        },
        'napolitana':{
            'ingredientes': ['mussarela', 'rodelas de tomate', 'queijo parmesão', 'orégano'],
            'preco': 35.00
        },
        'brocolis':{
            'ingredientes': ['brócolis refogado coberto com mussarela', 'alho'],
            'preco': 38.00
        },
        'lombinho':{
            'ingredientes': ['mussarela', 'lombo defumado', 'cebola'],
            'preco': 42.00
        },
        'portuguesa':{
            'ingredientes': ['mussarela', 'ovos', 'palmito', 'pimentão', 'ervilha', 'presunto', 'cebola'],
            'preco': 42.00
        },
        'palmito':{
            'ingredientes': ['mussarela', 'palmito', 'orégano'],
            'preco': 38.00
        },
        'pepperoni':{
            'ingredientes': ['mussarela', 'pepperoni', 'cebola'],
            'preco': 40.00
        },
        'bacon':{
            'ingredientes': ['mussarela coberta com bacon', 'orégano'],
            'preco': 42.00
        },
        'mista':{
            'ingredientes': ['mussarela', 'presunto', 'orégano'],
            'preco': 34.00
        },
        'vegetariana':{
            'ingredientes': ['mussarela', 'pimentão', 'cebola', 'azeitona', 'ervilha', 'tomate', 'palmito', 'milho', 'orégano'],
            'preco': 48.00
        },
        'frango':{
            'ingredientes': ['molho de tomate', 'mussarela', 'frango'],
            'preco': 34.00
        },
        'frango com Catupiry':{
            'ingredientes': ['molho de tomate', 'mussarela', 'frango', 'catupiry'],
            'preco': 40.00
        },
        'rúcula com Tomate Seco':{
            'ingredientes': ['mussarela', 'rúcula', 'tomate seco', 'orégano'],
            'preco': 45.00
        },
        'berinjela':{
            'ingredientes': ['berinjela', 'cebola', 'parmesão', 'mussarela', 'azeitona preta'],
            'preco': 38.00
        },
        'quatro queijos':{
            'ingredientes': ['mussarela', 'provolone', 'parmesão', 'catupiry'],
            'preco': 45.00
        },
        'canadense':{
            'ingredientes': ['mussarela', 'lombo', 'champignon', 'palmito', 'catupiry'],
            'preco': 45.00
        },
        'strogonoff':{
            'ingredientes': ['mussarela', 'champignon', 'strogonoff de frango', 'batata palha'],
            'preco': 48.00
        },
        'bauru':{
            'ingredientes': ['Presunto', 'mussarela', 'tomate', 'orégano', 'azeitonas'],
            'preco': 36.00
        }
    },
    'pizzas_doces': {
        'banana com Canela': {
            'ingredientes': ['banana caramelizada', 'leite condensado', 'canela'],
            'preco': 39.90
      },
      'chocolate': {
            'ingredientes': ['chocolate preto ou branco'],
            'preco': 42.00
      },
      'prestígio': {
            'ingredientes': ['chocolate', 'coco ralado', 'leite condensado'],
            'preco': 45.00
      },
      'romeu e Julieta': {
            'ingredientes': ['goiabada', 'mussarela'],
            'preco': 42.00
      },
      'sensação': {
            'ingredientes': ['chocolate', 'granulado', 'morango'],
            'preco': 48.00
      },
      'beijinho': {
            'ingredientes': ['chocolate branco', 'coco', 'leite condensado'],
            'preco': 46.00
      },
      'm&m': {
            'ingredientes': ['chocolate', 'M&M'],
            'preco': 52.00
      },
      'sorvete': {
            'ingredientes': ['chocolate', 'sorvete'],
            'preco': 48.00
      },
      'paçoca': {
           'ingredientes': ['chocolate', 'paçoca de amendoim'],
           'preco': 48.00 
      },
      'nutella com Morango':{
            'ingredientes': ['nutella', 'morango'],
           'preco': 55.00
      }
    },
    'bebidas': {
        'refrigerante lata': {
            'opcoes': ['coca-cola', 'guaraná', 'fanta uva', 'fanta laranja', 'sprite', 'pepsi'],
            'preco': 5.00
        },
        'refrigerante 2L': {
            'opcoes': ['coca-cola', 'guaraná', 'fanta uva', 'fanta laranja', 'sprite', 'pepsi'],
            'preco': 9.00
        },
        'cerveja latão': {
            'opcoes': ['itaipava', 'petra', 'skol', 'brahma', 'glacial', 'heineken', 'amstel'],
            'preco': 5.00
        },
        'agua': {
            'opcoes': ['com gás', 'sem gás'],
            'preco': 3.00
        }
    }
}

# Dicionário para armazenar o pedido do usuário
pedidos = {}

# Comando /start
@bot.message_handler(commands=['start'])
def boas_vindas(message):
    nome_usuario = message.from_user.first_name
    bot.reply_to(message, f"""
    Olá, {nome_usuario}! Bem-vindo(a) à APizzaS🍕.
Digite /comandos para ver a lista de comandos existentes!
""")
    #print(message)  -Teste para ver as informações da mensagem recebida!
    
# Comando /comandos
@bot.message_handler(commands=['comandos'])
def ajuda(message):
    respostaComandos = 'Olá! Bem-vindo(a) à APizzaS🍕.\nAqui estão os comandos disponíveis:\n\n'
    for comando, descricao in comandos_disponiveis.items():
        respostaComandos += f'{comando}: {descricao}\n\n'
    bot.send_message(message.chat.id, respostaComandos)
    
# Comando /cardapio
@bot.message_handler(commands=['cardapio'])
def mostrar_cardapio(message):
    resposta = 'Aqui está o nosso cardápio:\n\n'
    for categoria, pizzas in cardapio.items():
        resposta += f'{categoria.title()}:\n\n'
        for pizza, detalhes in pizzas.items():
            if categoria == 'bebidas':
                opcoes = ', '.join(detalhes['opcoes'])
                resposta += f'• {pizza.title()}: Opções: {opcoes} - R${detalhes["preco"]:.2f}\n\n'
            else:
                ingredientes = ', '.join(detalhes['ingredientes'])
                resposta += f'• {pizza.title()}: Ingredientes: {ingredientes} - R${detalhes["preco"]:.2f}\n\n'
        resposta += '\n\n'
    bot.reply_to(message, resposta)

# Comando /fazer_pedido
@bot.message_handler(commands=['pedido'])
def fazer_pedido(message):
    chat_id = message.chat.id
    pedidos[chat_id] = []  # Inicializa uma lista vazia de pedidos para o chat_id
    bot.reply_to(message, """Por favor, escolha os itens que estão no cardápio. Digite os itens separadamente\n\n
Quando finalizar a escolha digite: /finalizar_pedido""")

# Comando /ajuda
@bot.message_handler(commands="ajuda")
def responder (mensagem):
    # ID do chat pessoal para encaminhar a conversa
    chat_pessoal_id = 'ID_DO_ATENDENTE' #colocar o id do atendente para a mensagem cair para o corporativo dele
    # Encaminha a mensagem recebida para o chat pessoal
    bot.forward_message(chat_pessoal_id, mensagem.chat.id, mensagem.message_id)
    bot.send_message(mensagem.chat.id, "Um atendente foi solicitado e está a caminho para te auxiliar, aguarde instantes!")

# Comando /horario
@bot.message_handler(commands="horario")
def horario (mensagem):
      bot.send_message(mensagem.chat.id, "Nosso horário de funcionamento é de Terça a Quinta das 18:00 às 23:00 e Sexta, Sábado e Domingo das 18:00 às 01:00 da manhã seguinte!")

# Lidar com mensagens contendo uma pizza ou bebida escolhida
@bot.message_handler(func=lambda message: message.text.lower() in cardapio['pizzas_salgadas'].keys() or
                                            message.text.lower() in cardapio['pizzas_doces'].keys() or
                                            message.text.lower() in cardapio['bebidas'].keys())
def adicionar_pedido(message):
    chat_id = message.chat.id
    pedido_usuario = pedidos.get(chat_id, [])
    if message.text.lower() in cardapio['pizzas_salgadas'].keys():
        categoria = 'pizzas_salgadas'
    elif message.text.lower() in cardapio['pizzas_doces'].keys():
        categoria = 'pizzas_doces'
    else:
        categoria = 'bebidas'
    item_escolhido = message.text.lower()
    pedido_usuario.append((categoria, item_escolhido))
    pedidos[chat_id] = pedido_usuario
    bot.reply_to(message, f'Item adicionado ao pedido: {item_escolhido.title()}')

# Comando /finalizar_pedido
@bot.message_handler(commands=['finalizar_pedido'])
def finalizar_pedido(message):
    chat_id = message.chat.id
    pedido_usuario = pedidos.get(chat_id, [])
    if pedido_usuario:
        total = 0
        resposta = 'Seu pedido:\n\n'
        for categoria, item in pedido_usuario:
            if categoria == 'bebidas':
                opcoes = ', '.join(cardapio[categoria][item]['opcoes'])
                preco = cardapio[categoria][item]['preco']
                resposta += f'• {item.title()}: Opções: {opcoes} - R${preco:.2f}\n'
            else:
                ingredientes = ', '.join(cardapio[categoria][item]['ingredientes'])
                preco = cardapio[categoria][item]['preco']
                resposta += f'• {item.title()}: Ingredientes: {ingredientes} - R${preco:.2f}\n'
            total += preco
        resposta += f'\nTotal: R${total:.2f} + R$3.50 de frete = R${total + 3.50:.2f}'
        bot.reply_to(message, resposta)
        del pedidos[chat_id]  # Limpa o pedido do usuário
    else:
        bot.reply_to(message, 'Seu pedido está vazio. Por favor, escolha um item antes de finalizar o pedido.')

# Resposta padrão para mensagens não reconhecidas
@bot.message_handler(func=lambda message: True)
def resposta_padrao(message):
    bot.reply_to(message, 'Desculpe, não entendi. Utilize /comandos para ver a lista de comandos disponíveis.')

# Executando o bot
bot.polling()
