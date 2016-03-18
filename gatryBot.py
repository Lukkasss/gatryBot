import json, requests, time, telepot, sys

ultimoNome = '';

TOKEN = sys.argv[1];

bot = telepot.Bot(TOKEN);
print(bot.getMe());

while True:

	getJson = requests.get('https://api.import.io/store/connector/361f5280-6bac-4c4c-9a0a-0028622374f8/_query?input=webpage/url:https%3A%2F%2Fgatry.com%2F&&_apikey=000c112af5ad4f33b2f40fdfe34ec36ba64eea2cfb0998639867a151bdaf65f498dc0376a779863af592d87e58c3291732681793b89008f48fbc545a9cb4c34eb6ebc3b5a5695508a964ed5cdda7eb9d');
	data = json.loads(getJson.text);

	nome = data['results'][0]['informacoes_link/_text'];
	valor = data['results'][0]['r_number/_source'];
	link = data['results'][0]['informacoes_link'];
	datapostado = data['results'][0]['datapostado_value'];

	if (nome != ultimoNome):
		bot.sendMessage('78784524', nome + '\n' + 'R$' + valor + '\nLink: ' + link + '\n\n' + datapostado);
		bot.sendMessage('80858327', nome + '\n' + 'R$' + valor + '\nLink: ' + link + '\n\n' + datapostado);
		respostaBot = bot.getUpdates();
		print(respostaBot);
		print(nome);
		print('R$' + valor);
		print(link);
		print(datapostado);
		ultimoNome = nome;
	time.sleep(10);
