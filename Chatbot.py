import json


class Chatbot:
    def __init__(self, name):
        try:
            memory = open(name + '.json', 'r')
        # caso o json n seja encontrado, ele será criado aqui
        except FileNotFoundError:
            memory = open(name + '.json', 'w')
            memory.write('[["Julio Leonardo Carvalho"], {"oi": "Olá, qual o seu name?", "tchau": "tchau"}]')
            memory.close()
            memory = open(name + '.json', 'r')
        self.name = name
        self.known, self.sentences = json.load(memory)
        memory.close()
        self.history = [""]

    # Aqui é realizado o tratamento do que é recebido pelo bot
    @staticmethod
    def listen(sentence=None):
        if sentence is None:
            sentence = input('>: ')
        sentence = str(sentence)
        sentence = sentence.lower()
        return sentence

    def think(self, sentence):
        if sentence in self.sentences:
            return self.sentences[sentence]

        # Responde sentences dependendo do histórico
        lastSentence = self.history[-1]
        if 'qual o seu' in lastSentence:
            name = self.get_name(sentence)
            sentence = self.answer_name(name)
            return sentence
        if 'cliente do Banco' in lastSentence:
            if sentence == '1':
                return 'Por gentileza, informe o número do cartão a ser consultado.'
            elif sentence == '2':
                return 'Será um prazer te atender, :):\n' \
                       'https://aquisicao.carrefoursolucoes.com.br/'
            else:
                return 'Por favor responda 1 ou 2'
        if 'consultado' in lastSentence:
            if sentence.isdigit() and len(sentence) == 16:
                return 'Vamos confirmar alguns dados, ok?\nQual o nome da sua mãe?'
            else:
                return 'O cartão deve ter apenas números e possuir 16 dígitos.\n' \
                       'Por gentileza, verifique e envie novamente. ;)'
        if 'mãe' in lastSentence:
            return 'Qual o ano em que você nasceu?'
        if 'nasceu' in lastSentence and sentence.isdigit():
            return 'Perfeito!\n' \
                   'Em que posso te ajudar hoje?\n' \
                   '1 - Bloquear cartão\n' \
                   '2 - Limite disponível\n' \
                   '3 - Pagar fatura atual\n' \
                   'Para demais informações, seguros, serviços e promoções, visite nosso site:\n' \
                   'https://www.carrefoursolucoes.com.br/'
        else:
            'Para o ano em que você nasceu, gentilza responder no formato "AAAA", apenas números. ;)'

        if 'ajudar' in lastSentence and sentence.isdigit():
            if sentence == '1':
                return 'Cartão bloqueado com sucesso! Até a próxima!'
            elif sentence == '2':
                return 'Seu limite disponível é R$1234,56. Até a próxima!'
            elif sentence == '3':
                return 'Segue código de barras para pagamento:\n' \
                       '00000000000000000000000000000000000000000000000\n' \
                       'Até a próxima!'
            else:
                return 'Para que eu possa te ajudar, responda apenas o número da opção desejada:\n' \
                       '1 - Bloquear cartão\n' \
                       '2 - Limite disponível\n' \
                       '3 - Pagar fatura atual\n' \
                       'Para demais informações, seguros, serviços e promoções, visite nosso site:\n' \
                       'https://www.carrefoursolucoes.com.br/'

        try:
            resp = str(eval(sentence))
            return resp
        except:
            pass
        return 'Não entendi'

    # coleta nome da pessoa
    @staticmethod
    def get_name(name):
        if 'o meu name eh ' in name:
            name = name[14:]

        name = name.title()
        return name

    # responde com o nome e pergunta se é cliente ou não
    def answer_name(self, name):
        if name in self.known:
            sentence = 'Bem vindo de volta, '
        else:
            sentence = 'Muito prazer, '

        sentence2 = '\nVocê já é cliente do Banco Carrefour?\n' \
                    'Se sim, responda 1.\n' \
                    'Ou responda 2 para ser nosso cliente.'
        return sentence + name + "!" + sentence2

    # função responsável por enviar resposta ao cliente
    def speak(self, sentence):
        print(sentence)
        self.history.append(sentence)
