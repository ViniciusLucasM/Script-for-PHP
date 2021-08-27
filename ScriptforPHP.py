import subprocess
import os


def execCommands(comando):
    os.system(comando)


def processCapture(comando):
    try:
        capture = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE)
        return capture.stdout.read().decode('utf-8')
    except Exception:
        return ""


def captureString(comando, versao):
    try:
        capString = subprocess.Popen(
            comando, shell=True, stdout=subprocess.PIPE)
        retor = capString.stdout.read().decode('utf-8')
        come = retor.index(versao) + len(versao)
        print(retor[:come])
    except Exception:
        print('ESSA VERSAO NAO ESTA DISPONIVEL NO SEU SERVIDOR')


opcao = 0
while opcao != 9:

    print()
    print('[ 1 ] Ver versoes do PHP')
    print('[ 2 ] Ver versao do PHP que esta sendo utilizada')
    print('[ 3 ] Fazer restart no PHP')
    print('[ 4 ] Verificar status do PHP')
    print('[ 5 ] Mudar versao do PHP')
    print('[ 8 ] Limpar terminal')
    print('[ 9 ] Sair do menu')
    opcao = int(input('Digite a opcao desejada: '))

    if opcao == 1:
        versao = str(input('Digite a versao que voce deseja: '))
        comando = "php" + versao + " -v"
        captureString(comando, versao)
    if opcao == 2:
        comando = "php -v"
        execCommands(comando)
    if opcao == 3:
        versao = str(input('Digite a versao do PHP a ser restartado: '))
        comando = "service php" + versao + "-fpm restart"
        execCommands(comando)
    if opcao == 4:
        versao = str(input('Digite a versao do PHP que deseja ver o status: '))
        comando = 'service php' + versao + '-fpm status | grep -s Active:'
        processCapture(comando)
        if "inactive" in processCapture(comando):
            print('ESSA VERSAO DO SEU PHP NAO ESTA ATIVADA')
        elif "active" in processCapture(comando):
            print('ESSA VERSAO DO SEU PHP ESTA ATIVADO')
        else:
            print()
            print('ESSA VERSAO DO PHP NAO ESTA DISPONIVEL NO SEU SERVIDOR')
    if opcao == 5:
        versao = str(input('Digite a versao para qual deseja mudar: '))
        comando = ' rm /usr/bin/php; \
                    ln -s /usr/bin/php' + versao + ' /usr/bin/php; \
                    rm /usr/bin/php-config; \
                    ln -s /usr/bin/php-config' + versao + ' /usr/bin/php-config; \
                    rm /usr/bin/phpize; \
                    ln -s /usr/bin/phpize' + versao + ' /usr/bin/phpize; \
                    rm /usr/bin/phar; \
                    ln -s /usr/bin/phar' + versao + ' /usr/bin/phar; \
                    rm /usr/bin/phar.phar; \
                    ln -s /usr/bin/phar.phar' + versao + ' /usr/bin/phar.phar; \
                    systemctl enable php' + versao + '-fpm; \
                    systemctl start php' + versao + '-fpm; '
        execCommands(comando)
    if opcao == 8:
        comando = 'clear'
        execCommands(comando)


versoes = ["5.6", "7.0", "7.1", "7.2", "7.3", "7.4"]
retorCommand = []

for i in versoes:
    comando = 'service php' + (i) + '-fpm status | grep -s Active:'
    retorCommand.append(processCapture(comando))
