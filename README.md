# Email com Django
E-mail com python + Django

1- 'pip install decouple'

2 - criar um arquivo .env fora do projeto

3 - Colocar as seguintes informações

![Env Dados](https://user-images.githubusercontent.com/93543449/212479936-a7af302d-c07b-4e37-9745-36c9bd27e1f9.png)

EMAIL_HOST_USER=Seu email <br>
EMAIL_HOST_PASSWORD=Sua senha  <br>
EMAIL_USE_TLS=True # criptografar emails  <br>
EMAIL_PORT=587 - Porta do servidor que você usa  <br>
EMAIL_HOST=smtp.gmail.com - No caso, aqui o meu é gmail


4 - Ir no arquivo Settings.py do 'ProjetoEmail'

5 - Importar a biblioteca baixada

![Settings importDecouple](https://user-images.githubusercontent.com/93543449/212479881-d028214a-c46b-4818-912b-75f98e37df1a.png)

6 - Agora configurar o Email no arquivo Settings.py (nas últimas linhas)

![SettingsE-mail](https://user-images.githubusercontent.com/93543449/212480070-a0c797f2-0799-4e6e-ab38-1ae0fea59fd2.png)

7 - Ir no arquivo Views.py  em 'Email', na linha 13 colocar 

![Views EmailEnviado](https://user-images.githubusercontent.com/93543449/212480215-1064aeeb-04ad-491c-9d57-6f33079519b9.png)

8 - Ir na pasta templates (dentro da pasta Email), depois emails e acessar o arquivo html (lá você pode configurar o estilo do email, oque vai aparecer ou não)


Se gostou da uma estrelinha

Pedro | Dev 2023
