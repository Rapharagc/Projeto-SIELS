import tkinter as tk
from tkinter import ttk
from tkinter import Canvas, Label, Button
from PIL import ImageTk, Image, ImageGrab


def sair():
    root.destroy()


def clear_frame():
    for widget in root.winfo_children():
        widget.destroy()


def inicial():
    clear_frame()

    frame1 = tk.Frame(root, width=1920, height=880, bg="#2E9AFE")
    frame1.place(x=0, y=0)

    imagem_nome_logo = Image.open("D:\\Projeto INT\\Artes\\logo_nome.png")
    imagem_nome_logo = imagem_nome_logo.resize((600, 200), Image.LANCZOS)
    img1 = ImageTk.PhotoImage(imagem_nome_logo)
    imagem_nome = tk.Label(frame1, image=img1, bg="#2E9AFE")
    imagem_nome.image = img1  
    imagem_nome.place(x=650, y=100)
    
    imagem_logo = Image.open("D:\\Projeto INT\\Artes\\logo.png")
    imagem_logo = imagem_logo.resize((400, 400), Image.LANCZOS)
    img2 = ImageTk.PhotoImage(imagem_logo)
    imagem = tk.Label(frame1, image=img2, bg="#2E9AFE")
    imagem.image = img2  
    imagem.place(x=750, y=340)

    imagem_iniciar = Image.open("D:\\Projeto INT\\Artes\\botao_iniciar.png")
    img_iniciar = ImageTk.PhotoImage(imagem_iniciar)
    botao_iniciar = tk.Button(frame1, image=img_iniciar, bg="#2E9AFE", bd=0, activebackground="#2E9AFE", command=janela_principal)
    botao_iniciar.image = img_iniciar
    botao_iniciar.place(x=900, y=760)

    imagem_sair = Image.open("D:\\Projeto INT\\Artes\\botao_sair.png")
    img_sair = ImageTk.PhotoImage(imagem_sair)
    botao_sair = tk.Button(frame1, image=img_sair, bg="#2E9AFE", bd=0, activebackground="#2E9AFE", command=sair)
    botao_sair.image = img_sair
    botao_sair.place(x=1800, y=10)

    imagem_ajuda = Image.open("D:\\Projeto INT\\Artes\\botao_ajuda.png")
    img_ajuda = ImageTk.PhotoImage(imagem_ajuda)
    botao_ajuda = tk.Button(frame1, image=img_ajuda, bg="#2E9AFE", bd=0, activebackground="#2E9AFE", command=sair)
    botao_ajuda.image = img_ajuda
    botao_ajuda.place(x=1680, y=10)

    imagem_config = Image.open("D:\\Projeto INT\\Artes\\botao_config.png")
    img_config = ImageTk.PhotoImage(imagem_config)
    botao_config = tk.Button(frame1, image=img_config, bg="#2E9AFE", bd=0, activebackground="#2E9AFE", command=sair)
    botao_config.image = img_config
    botao_config.place(x=1560, y=10)

    frame2 = tk.Frame(root, width=1920, height=200, bg="#FF8000")
    frame2.place(x=0, y=880)


def janela_principal():
    clear_frame()

    frame1 = tk.Frame(root, width=1920, height=880, bg="#2E9AFE")
    frame1.place(x=0, y=0)
    
    imagem_voltar = Image.open("D:\\Projeto INT\\Artes\\botao_voltar.png")
    img_voltar = ImageTk.PhotoImage(imagem_voltar)
    botao_voltar = tk.Button(frame1, image=img_voltar, bg="#2E9AFE", bd=0, activebackground="#2E9AFE", command=inicial)
    botao_voltar.image = img_voltar
    botao_voltar.place(x=10, y=10)
    
    frame2 = tk.Frame(root, width=1920, height=220, bg="#FF8000")
    frame2.place(x=0, y=880)

    frame_exercicio = tk.Frame(frame1, width=1680, height=720)
    frame_exercicio.place(x=120, y=120)

    canvas = tk.Canvas(frame_exercicio, width=1680, height=720, background="white")
    canvas.grid(row=0, column=0)

    # Load the background image onto the canvas
    img = ImageTk.PhotoImage(file="D:\\Projeto INT\\INT\\circulo.png")
    canvas.create_image(0, 0, anchor=tk.NW, image=img)
    canvas.image = img  # Keep a reference of the image to avoid garbage collection

    click_num = [0]  # Use a list to be able to modify it within nested functions

    def draw_line(event):
        if click_num[0] % 2 == 0:
            click_num.append((event.x, event.y))
            click_num[0] = 1
        else:
            x1, y1 = click_num.pop()
            for i in range(-1, 2):
                for j in range(-1, 2):
                    canvas.create_line(x1, y1, x1 + i, y1 + j, fill="#32CD32", width=3)
            click_num[0] += 1

    canvas.bind('<B1-Motion>', draw_line)

    def salvar_imagem():
        x = canvas.winfo_rootx()
        y = canvas.winfo_rooty()
        width = canvas.winfo_width()
        height = canvas.winfo_height()
        ImageGrab.grab(bbox=(x, y, x + width, y + height)).save("D:\\Projeto INT\\INT\\testando.png")

    def obter_pontos_computador():
        imagem = Image.open("D:\\Projeto INT\\INT\\circulo.png")
        pixels = imagem.load()
        cor_desejada = (0, 0, 0)
        largura, altura = imagem.size
        pontos_cor_desejada = []

        for x in range(largura):
            for y in range(altura):
                cor = pixels[x, y]
                if cor == cor_desejada:
                    pontos_cor_desejada.append([x, y, 9999])
    
        return pontos_cor_desejada

    def obter_pontos_usuario():
        imagem = Image.open("D:\\Projeto INT\\INT\\testando.png")
        pixels = imagem.load()
        cor_desejada = (50, 205, 50)
        largura, altura = imagem.size
        pontos_cor_desejada = []

        for x in range(largura):
            for y in range(altura):
                cor = pixels[x, y]
                if cor == cor_desejada:
                    pontos_cor_desejada.append((x, y))
    
        return pontos_cor_desejada

    def atualizar_distancia(lista_coords_computador, lista_coords_usuario):
        movimentos = [
            (0, -1),   # Norte
            (0, 1),    # Sul
            (1, 0),    # Leste
            (-1, 0),   # Oeste
            (1, 1),    # Sudeste
            (-1, -1),  # Noroeste
            (-1, 1),   # Sudoeste
            (1, -1)    # Nordeste
        ]

        for coord_computador in lista_coords_computador:
            x_comp, y_comp, _ = coord_computador
            proximo = False
        
            for coord_usuario in lista_coords_usuario:
                x_user, y_user = coord_usuario
            
                for dx, dy in movimentos:
                    novo_x = x_comp + dx
                    novo_y = y_comp + dy
                
                    if (novo_x, novo_y) == (x_user, y_user):
                        coord_computador[2] = 1
                        proximo = True
                        break
                if proximo:
                    break

    def calcular_porcentagem(lista_coords_computador):
        total_pontos = len(lista_coords_computador)
        pontos_corretos = sum(1 for ponto in lista_coords_computador if ponto[2] <= 1)
        porcentagem = (pontos_corretos / total_pontos) * 100
        return porcentagem

    def resultado():
        salvar_imagem()
        lista_coords_computador = obter_pontos_computador()
        lista_coords_usuario = obter_pontos_usuario()

        atualizar_distancia(lista_coords_computador, lista_coords_usuario)

        porcentagem = calcular_porcentagem(lista_coords_computador)
        label_2.config(text=f"Porcentagem do traçado do desenho do usuário é: {porcentagem:.2f}%")

    
    botao_1 = tk.Button(frame2, text="Salvar", command=resultado)
    botao_1.place(x=928, y=40)
    label_2 = tk.Label(frame2, text='')
    label_2.place(x=800, y=120)


root = tk.Tk()
root.attributes("-fullscreen", True)
inicial()
root.mainloop()