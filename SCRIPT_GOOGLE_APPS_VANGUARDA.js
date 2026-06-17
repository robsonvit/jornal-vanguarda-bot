function acordarBotJornalVanguarda() {
  // Jitter (Aleatoriedade): Adiciona um atraso aleatório para o disparo não parecer engessado (robô).
  // Como o gatilho roda a cada 15 min e a ação do GitHub leva ~5 min, 
  // limitamos o atraso a no máximo 7 minutos (420.000 ms) para garantir que uma execução termine antes da próxima.
  var maxAtrasoMinutos = 7;
  var atrasoMaximoMs = maxAtrasoMinutos * 60 * 1000;
  var atrasoAleatorio = Math.floor(Math.random() * atrasoMaximoMs);
  
  Logger.log("Jitter ativado: Aguardando " + (atrasoAleatorio / 1000 / 60).toFixed(2) + " minutos antes de disparar o bot...");
  Utilities.sleep(atrasoAleatorio);

  // Alterado para o repositório jornal-vanguarda-bot
  var url = "https://api.github.com/repos/robsonvit/jornal-vanguarda-bot/actions/workflows/facebook_news_bot.yml/dispatches";
  
  // ATENÇÃO: Token Clássico (Personal Access Token) do GitHub
  var token = "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"; 
  
  var options = {
    "method": "post",
    "headers": {
      "Authorization": "Bearer " + token,
      "Accept": "application/vnd.github.v3+json"
    },
    "payload": JSON.stringify({ "ref": "main" }) // se a branch principal for 'main', troque 'master' por 'main'
  };
  
  try {
    var response = UrlFetchApp.fetch(url, options);
    var statusCode = response.getResponseCode();
    
    if (statusCode == 204) {
      Logger.log("Sucesso! O sinal foi enviado para o GitHub e o Bot está trabalhando.");
    } else {
      Logger.log("Atenção, erro. Código: " + statusCode);
      Logger.log("Detalhes: " + response.getContentText());
    }
  } catch(e) {
    Logger.log("Erro de conexão: " + e.toString());
  }
}
