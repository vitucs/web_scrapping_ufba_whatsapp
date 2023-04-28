Web Scraping com Selenium e BeautifulSoup

Este é um código Python que realiza Web Scraping em uma página HTML utilizando as bibliotecas Selenium e BeautifulSoup. Ele busca uma tabela de convocações e publicações no site https://www.ingresso.ufba.br/ e verifica a cada segundo se houve atualização na tabela. Caso haja uma nova atualização, o código utiliza o navegador Google Chrome e a biblioteca Selenium para enviar uma mensagem para contatos previamente definidos no WhatsApp Web.
Como funciona

O código inicia importando as bibliotecas necessárias: urlopen do urllib.request, BeautifulSoup, datetime, schedule e webdriver do Selenium, além de Keys e By do webdriver. Também são definidas algumas variáveis e listas que serão utilizadas mais tarde no código.

A função web_scraping() é definida para buscar as informações da tabela no site. Para isso, a função acessa a página com a função urlopen, cria um objeto BeautifulSoup com o conteúdo HTML da página e busca a tabela de convocações e publicações no site. Depois, a função procura pelas linhas da tabela e adiciona os textos das células que contém "span" em uma lista chamada lista_trs.

Em seguida, o código utiliza a biblioteca schedule para agendar a execução da função web_scraping() a cada segundo. Depois, há um loop infinito que executa a função run_pending() da biblioteca schedule e espera um segundo com a função time.sleep(1).

O código verifica se a variável atual é diferente da variável anterior. Se sim, é considerado que houve uma nova atualização na tabela do site. Em seguida, o código define uma lista de contatos para quem será enviado uma mensagem pelo WhatsApp Web.

Cada contato é iterado e o código utiliza o webdriver do Google Chrome para acessar o site do WhatsApp Web e enviar a mensagem para o contato. A mensagem é criada com a nova atualização na tabela e a última mensagem enviada (que é armazenada na variável ultMsg). Para enviar a mensagem, o código localiza a caixa de pesquisa do contato, digita a mensagem, localiza o botão de envio e clica nele.

Por fim, a variável anterior é atualizada para o valor de atual, o número de novas atualizações é impresso no console e o loop recomeça.
