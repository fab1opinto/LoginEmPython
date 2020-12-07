from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import databaser


#Criar Janela
jan = Tk()
jan.title("Novo Sistema - Painel de Controle")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False) #não é possivel alterar o tamanho da janela 
jan.attributes("-alpha",0.9) #transparencia na janela
#Carregando Imagens

logo = PhotoImage(file="images/logo.png")#Python e Tkinter trabalham com arquivos de imagens .png

#Widgets
LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise") #Lado esquerdo da janela
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE" , relief="raise")#Lado direito da janela
RightFrame.pack(side=RIGHT)

#exibir imagem
#Frame da esquerda
LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)

#Usuario, Login
UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
UserLabel.place(x=5, y=100)

#Entrada de dados - Username
UserEntry = ttk.Entry(RightFrame, width=25)
UserEntry.place(x=160, y=110)

#Password
PassLabel = Label(RightFrame, text="Password:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
PassLabel.place(x=12, y=150)

#Entrada de dados - Password
PassEntry = ttk.Entry(RightFrame, width=25, show="*")
PassEntry.place(x=160, y=160)

def loginbotao():
    User = UserEntry.get()
    Pass = PassEntry.get()
    databaser.cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? and Password = ?)
    """, (User, Pass))
    print("Logado")
    verifylogin = databaser.cursor.fetchone()
    try: 
        if (User in verifylogin and Pass in verifylogin):
            messagebox.showinfo(title="Login Info", message="Acesso Confirmado, Bem Vindo!")
    except:
            messagebox.showinfo(title="Login Info", message="Acesso Negado, Verifique se está cadastrado no sistema")    

#Botões
LoginButton = ttk.Button(RightFrame, text="Login", width=25, command=loginbotao)
LoginButton.place(x=160, y=225)



def register():
    #Removendo widgets de login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    #Inserindo widgets de Cadastro
    NomeLabel = Label(RightFrame, text="Nome:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    NomeLabel.place(x=65, y=5)
    
    NomeEntry = ttk.Entry(RightFrame, width=25)
    NomeEntry.place(x=160, y=10)

    EmailLabel = Label(RightFrame, text="Email:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    EmailLabel.place(x=65, y=55)

    EmailEntry = ttk.Entry(RightFrame, width=25)
    EmailEntry.place(x=160, y=60)

    def registertodatabase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if(Name == "" and Email == "" and User == "" and Pass == ""):
            messagebox.showerror(title="Register Error", message="Preencha todos os Campos")
        else:
            databaser.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            """, (Name, Email, User, Pass))
            databaser.conexao.commit()
            messagebox.showinfo(title="Register Info", message="Conta criada com Sucesso")
        
    Register = ttk.Button(RightFrame, text="Registrar", width=15, command=registertodatabase)
    Register.place(x=10,y=225)

    def backtologin():
        #removendo widgets de cadastro
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
        #Trazendo de volta os widgets de login
        LoginButton.place(x=150, y=225)
        RegisterButton.place(x=150, y=260)

    Back = ttk.Button(RightFrame, text="Voltar", width=15, command=backtologin)
    Back.place(x=10, y=260)

RegisterButton = ttk.Button(RightFrame, text="Registrar", width=25, command=register)
RegisterButton.place(x=160, y=260)
jan.mainloop()
