import win32com.client as win32

#criar a integração com o outlook

outlook = win32.Dispatch('outlook.application')

#criar um e-mail
email = outlook.CreateItem(0)

#configurar as informações do seu e-mail
#Destino
email.To = "aeneto14@gmail.com"
#Assunto
email.Subject = "teste_automação"
#corpo e-mail
email.HTMLBody = """

<p>Olá André, isso é um código python</p>

"""

anexo = r'C:\Users\André Neto\OneDrive\Documentos\Planejamento financeiro e profissional - André.xlsx'
email.Attachments.Add(anexo)
email.send()
