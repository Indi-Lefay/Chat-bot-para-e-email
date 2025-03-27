import imaplib  # Biblioteca para acessar o e-mail via IMAP
import email  # Biblioteca para manipular e-mails
import os  # Biblioteca para manipulação de arquivos e diretórios
from email.header import decode_header  # Função para decodificar cabeçalhos de e-mails

# Configurações do e-mail
EMAIL_USER = "seuemail@gmail.com"  # Endereço de e-mail do usuário
EMAIL_PASS = "suasenha"  # Senha do e-mail
IMAP_SERVER = "imap.gmail.com"  # Servidor IMAP do provedor de e-mail
PASTA_DOWNLOAD = "downloads"  # Pasta onde os anexos serão salvos

# Conectar ao servidor IMAP
def conectar_email():
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)  # Conectar ao servidor IMAP usando SSL
    mail.login(EMAIL_USER, EMAIL_PASS)  # Fazer login com as credenciais
    mail.select("inbox")  # Selecionar a caixa de entrada
    return mail  # Retornar a conexão do e-mail

# Baixar anexos
def baixar_anexos(mail):
    status, mensagens = mail.search(None, "ALL")  # Buscar todos os e-mails na caixa de entrada
    mensagens = mensagens[0].split()  # Separar os identificadores dos e-mails
    
    if not os.path.exists(PASTA_DOWNLOAD):  # Verificar se a pasta de downloads existe
        os.makedirs(PASTA_DOWNLOAD)  # Criar a pasta caso não exista
    
    for num in mensagens[-5:]:  # Limita aos últimos 5 emails
        status, dados = mail.fetch(num, "(RFC822)")  # Buscar o conteúdo do e-mail
        for resposta in dados:
            if isinstance(resposta, tuple):  # Verificar se a resposta é uma tupla
                msg = email.message_from_bytes(resposta[1])  # Converter os dados do e-mail para formato legível
                assunto, encoding = decode_header(msg["Subject"])[0]  # Decodificar o assunto do e-mail
                if isinstance(assunto, bytes) and encoding:  # Verificar se o assunto está codificado
                    assunto = assunto.decode(encoding)  # Decodificar o assunto
                
                print(f"Baixando anexos do email: {assunto}")  # Exibir mensagem com o assunto do e-mail
                
                for parte in msg.walk():  # Percorrer todas as partes do e-mail
                    if parte.get_content_maintype() == "multipart":  # Ignorar partes multipartes
                        continue
                    if parte.get("Content-Disposition") is None:  # Ignorar partes sem anexo
                        continue
                    
                    nome_arquivo = parte.get_filename()  # Obter o nome do arquivo
                    if nome_arquivo:
                        nome_arquivo = decode_header(nome_arquivo)[0][0]  # Decodificar o nome do arquivo
                        if isinstance(nome_arquivo, bytes):  # Verificar se o nome está codificado
                            nome_arquivo = nome_arquivo.decode()  # Decodificar o nome do arquivo
                        
                        caminho_arquivo = os.path.join(PASTA_DOWNLOAD, nome_arquivo)  # Definir caminho para salvar o arquivo
                        with open(caminho_arquivo, "wb") as f:  # Abrir o arquivo para escrita em modo binário
                            f.write(parte.get_payload(decode=True))  # Escrever o conteúdo do anexo no arquivo
                        print(f"Arquivo salvo: {caminho_arquivo}")  # Exibir mensagem informando que o arquivo foi salvo

if __name__ == "__main__":
    mail = conectar_email()  # Estabelecer conexão com o e-mail
    baixar_anexos(mail)  # Chamar função para baixar anexos
    mail.logout()  # Encerrar a conexão com o e-mail
