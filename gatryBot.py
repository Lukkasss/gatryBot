import json, requests, time, telepot, sys

ultimoNome = '';

TOKEN = sys.argv[1];

bot = telepot.Bot(TOKEN);
print(bot.getMe());

while True:

	getJson = requests.get('https://api.import.io/store/connector/0f73e47a-bc1d-490b-924b-8886ac703701/_query?input=webpage/url:https%3A%2F%2Fwww.gatry.com%2F&&_apikey=000c112af5ad4f33b2f40fdfe34ec36ba64eea2cfb0998639867a151bdaf65f498dc0376a779863af592d87e58c3291732681793b89008f48fbc545a9cb4c34eb6ebc3b5a5695508a964ed5cdda7eb9d');
	data = json.loads(getJson.text);
	
	if(data.has_key('results')):
		nome = data['results'][0]['nome/_text'];
		valor = data['results'][0]['valor'];
		link = data['results'][0]['link'];
		#datapostado = data['results'][0]['hora'];
		
		if (nome != ultimoNome):
			bot.sendMessage('78784524', nome + '\n' + 'R$' + valor + '\nLink: ' + link + '\n');
			#bot.sendMessage('80858327', nome + '\n' + 'R$' + valor + '\nLink: ' + link + '\n');
			#respostaBot = bot.getUpdates();
			#print(respostaBot);
			print(nome);
			print('R$' + valor);
			print(link);
			#print(datapostado);
			ultimoNome = nome;
time.sleep(10);
