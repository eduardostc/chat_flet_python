import flet as ft

#Criação da função principal do app
def main(pagina):
    #add titulo
    titulo = ft.Text("Hashzap")
    pagina.add(titulo)

    def enviar_msg_tunel(msg): #Executar tudo o que eu quero que aconteça para todos os usuários que receberem a msg
        texto = ft.Text(msg)
        chat.controls.append(texto)
        pagina.update()

    pagina.pubsub.subscribe(enviar_msg_tunel)

    def enviar_msg(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        msg = f"{nome_usuario}:{texto_campo_mensagem}"
        pagina.pubsub.send_all(msg) #Enviar a mensagem no tunel de comunicação
                #texto = ft.Text(f"{nome_usuario}:{texto_campo_mensagem}") #ft.Text é um elemento de texto do flet
                #chat.controls.append(texto) #Adiciona um elemento na coluna
        campo_enviar_mensagem.value = "" #Limpar a caixar de enviar msg
        pagina.update()

    campo_enviar_mensagem = ft.TextField(label="Digite aqui sua mensagem")
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_msg)
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])#carregar campo de enviar mensagem; #carregar botão enviar em uma linha

    chat = ft.Column() #Criação do chat que é uma coluna

    #Entrar no chat
    def entrar_chat(evento):
        popup.open = False #fechar popup
        pagina.remove(titulo) #sumir com o titulo
        pagina.remove(botao) #Sumir com o botão iniciar chat
        pagina.add(chat) #carregar chat
        pagina.add(linha_enviar)#carregar campo de enviar mensagem
        #Add no chat msg "Fulando entrou no chat"       
        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario} Entrou no chat"
        pagina.pubsub.send_all(mensagem)
            # texto_msg = ft.Text(f"{nome_usuario} Entrou no chat")
            # chat.controls.append(texto_msg)
        pagina.update() #Sempre que faz alguma alteração na tela deve usar o update

    #Dados do Popup
    titulo_popup = ft.Text("Bem vindo ao Hashzap")
    caixa_nome = ft.TextField(label="Digite o seu nome")
    botao_popup = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)

    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, actions=[botao_popup]) #Estrutura do popup

    def abrir_popup(evento): #recebe obrigatoriamente um evento, visto que essa função estar associada ao clique de um botão.
        pagina.dialog = popup #Estar informando que a nossa pagina irá ter dialog (modal)
        popup.open = True #comando para abrir o popup
        pagina.update()
           
    
    #botão Inicial
    botao = ft.ElevatedButton("Iniciar chat", on_click=abrir_popup)
    pagina.add(botao)

#Executar essa função com o flet
#ft.app(main)
ft.app(main, view=ft.AppView.WEB_BROWSER)