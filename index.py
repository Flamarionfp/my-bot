# Importações
import os

# Definições

# Lista de comandos possíveis
comands = [
    'e ambiente-d',
    'e chrome',
    'e gitLab',
    'e github',
    'e pla',
    'e mysqlwb'
    'e postman',
    'e vscode',
    'e aula-redes'
    'e git-pages',
    'qual é seu nome?'
]

# Criação do Bot


class Bot:
    def __init__(self):
        self.name = 'BOT Jacinto'

    # Métodos do Bot

    # Função Abrir Chrome

    def openChrome(self):
        #print("Abrindo Chrome...")
        os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")

    # Função Abrir Trello

    def openTrello(self):
        #print("Abrindo Trello...")
        os.startfile("https://trello.com/b/Ylx8YAHT/projeto-faccat-lighthouse")

    # Função Abrir GitLab

    def openGitLab(self):
        #print("Abrindo GitLab...")
        os.startfile("https://gitlab.com/")

    # Função Abrir GitHub

    def openGitHub(self):
        #print("Abrindo GitHub...")
        os.startfile("https://github.com/Flamarionfp")

    # Função Abrir projetos atuais Lighthouse

    def openLightHouseCurrentProjects(self):
        #print("Abrindo projetos atuais da Lighthouse...")
        os.startfile("https://faccat-lighthouse.netlify.app/")
        os.startfile("https://marvelapp.com/prototype/866aj60/screen/80444574")

    # Função abrir MySQL Workbench

    def openMySqlWorkbench(self):
        #print("Abrindo MySql Work Bank...")
        os.startfile(
            "C:\Program Files\MySQL\MySQL Workbench 8.0\MySQLWorkbench.exe"
        )

    # Função abrir Postman

    def openPostman(self):
        #print("Abrindo Postman")
        os.startfile(r"C:\Users\Admin\AppData\Local\Postman\Postman.exe")

    # Função abrir Vs Code

    def openVsCode(self):
        #print("Abrindo Vs Code...")
        os.startfile(
            r"C:\Users\Admin\AppData\Local\Programs\Microsoft VS Code\Code.exe")

    # Função Abrir Android Studio

    def openAndroidStudio(self):
        #print("Abrindo Android Studio...")
        os.startfile(
            r"C:\Program Files\Android\Android Studio\bin\studio64.exe")

    # Função Abrir Discord

    def openDiscord(self):
        #print("Abrindo Discord...")
        os.startfile(
            r"C:\Users\Admin\AppData\Local\Discord\Update.exe --processStart Discord.exe")

    # Função Abrir aula de Redes
    def openNetworkClass(self):
        os.startfile("https://classroom.google.com/c/MzczODM5MTkyMzUy")
        os.startfile("https://meet.google.com/lookup/a4mz43jn4l")

    def showAllCommands(self):
        for i in range(len(comands)):
            print(comands[i])

    def exit(self):
        #print("Até outra hora!")
        exit()


# Configuração do Bot
bot = Bot()  # Instânciando o objeto Bot
botName = bot.name


# Funções

# Função para abrir todos os programas

def openDevelopEnvironment():
    bot.openChrome()
    bot.openPostman()
    bot.openMySqlWorkbench()
    bot.openPostman()
    bot.openVsCode()
    bot.openAndroidStudio()
    bot.openDiscord()


def openGitsPages():
    bot.openGitLab()
    bot.openGitHub()


# Criação do Usuário
class User:
    def __init__(self):
        self.name = "Flamarion"


user1 = User()  # Instânciando o objeto User
userName = user1.name


# Inicio da parte Lógica do Programa

print("{}: Olá, {}!!! O que posso ajudar? ".format(botName, userName))
resp = str(input()).lower().strip()
print(resp)

while True:
    while resp in comands:
        #print('Comando existe')
        print("{}: O que mais posso ajudar {}? ".format(bot.name, userName))
        resp = str(input()).lower().strip()
        break
    else:
        print('Comando inválido')
        resp = str(input()).lower().strip()
