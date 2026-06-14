function acordarBotJornalVanguarda() {
  // Alterado para o repositório jornal-vanguarda-bot
  var url = "https://api.github.com/repos/robsonvit/jornal-vanguarda-bot/actions/workflows/facebook_news_bot.yml/dispatches";
  
  // ATENÇÃO: Substitua este token pelo novo Token Clássico (Personal Access Token) criado no GitHub
  var token = "SEU_GITHUB_TOKEN_AQUI"; 
  
  var options = {
    "method": "post",
    "headers": {
      "Authorization": "Bearer " + token,
      "Accept": "application/vnd.github.v3+json"
    },
    "payload": JSON.stringify({"ref": "master"}) // se a branch principal for 'main', troque 'master' por 'main'
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
