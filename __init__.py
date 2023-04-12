from mycroft import MycroftSkill, intent_file_handler
from mycroft.util.parse import match_one
import openai

class ChatGPTSkill(MycroftSkill):
    def __init__(self):
        super(ChatGPTSkill, self).__init__(name="ChatGPTSkill")
        self.chat_gpt_api_key = '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'  # Substitua com sua chave de API do Chat GPT

    def initialize(self):
        # Inicializar o cliente da API do Chat GPT
        openai.api_key = self.chat_gpt_api_key

    @intent_file_handler('fazer.pesquisa.intent')
    def handle_fazer_pesquisa(self, message):
        # Extrair a consulta de pesquisa do intent
        query = message.data.get('query')

        # Enviar a consulta para o Chat GPT
        response = self._chat_gpt_request(query)

        if response:
            self.speak(response)
        else:
            self.speak('Desculpe, não consegui encontrar uma resposta para sua pesquisa.')

    def _chat_gpt_request(self, query):
        """
        Faz uma solicitação para o Chat GPT com a consulta de pesquisa fornecida.
        """
        prompt = f'Pesquisar: {query}\nResposta: '
        completions = openai.Completion.create(
            engine='text-davinci-002',
            prompt=prompt,
            max_tokens=1024
        )
        response = completions.choices[0].text.strip()

        return response

def create_skill():
    return ChatGPTSkill()
