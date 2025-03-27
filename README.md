# Chat-bot-para-e-email
Este projeto é um bot em Python que se conecta à sua caixa de entrada de e-mails, busca mensagens recentes e faz o download automático dos anexos, organizando-os em uma pasta específica.

✨ Funcionalidades

✅ Conecta-se automaticamente ao seu e-mail via protocolo IMAP.✅ Lê os últimos e-mails da sua caixa de entrada.✅ Identifica e baixa anexos automaticamente.✅ Salva os arquivos em uma pasta específica.✅ Decodifica corretamente nomes de arquivos e assuntos dos e-mails.

🛠️ Tecnologias Utilizadas

Python 3

imaplib → Para acessar o e-mail via IMAP.

email → Para processar e manipular mensagens.

os / shutil → Para organização e manipulação de arquivos.

🚀 Como Usar

1️⃣ Configurar as Credenciais

Edite o arquivo do código e insira suas credenciais no lugar correto:

EMAIL_USER = "seuemail@gmail.com"
EMAIL_PASS = "suasenha"
IMAP_SERVER = "imap.gmail.com"  # Altere conforme seu provedor de e-mail
PASTA_DOWNLOAD = "downloads"

⚠ Atenção! Se estiver usando Gmail, pode ser necessário ativar o acesso a aplicativos menos seguros ou gerar uma senha de app.

2️⃣ Instalar Dependências

Este projeto usa apenas bibliotecas padrão do Python, então nenhuma instalação extra é necessária!

3️⃣ Executar o Script

Basta rodar o script Python:

python automation_bot.py

📂 Organização dos Arquivos

automation_bot.py → Código principal do bot.

downloads/ → Pasta onde os anexos serão salvos automaticamente.

🔧 Possíveis Melhorias Futuras

🔹 Adicionar filtros para baixar apenas anexos de remetentes específicos.🔹 Implementar notificações via Telegram/WhatsApp quando um anexo for baixado.🔹 Criar um sistema de categorização automática dos arquivos baixados.
