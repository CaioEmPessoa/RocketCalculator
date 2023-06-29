import customtkinter as ctk
import random

root = ctk.CTk()

root.title('Rocket Calculator')

def button_numb(val):
    conta_completa = ''

    if val == "clear":
        calculos.clear()
        conta.configure(text="")
        entry.delete(0, 'end')

    # Se for um calculo
    elif val in ["+", "-", "/", "*"]:
        calculos.append(entry.get()) # append number that appers on the entry
        calculos.append(val) # append the used
        entry.delete(0, 'end')
        conta.configure(text=calculos)

    elif val == "=":
        calculos.append(entry.get())
        conta.configure(text=calculos)

        print(calculos)

        for valor in calculos:
            print(valor)
            conta_completa = conta_completa + valor
        
        resultado = eval(conta_completa)

        if int(str(random.random())[2]) % 2:
            print("menos dois")
            resultado -= 2
        else:
            print("mais dois")
            resultado += 2

        entry.delete(0, 'end') # apaga o último prompt
        entry.insert('end', resultado) # insere a resposta do calculo na area de prompt
        conta.configure(text=str(conta_completa) + " = " + str(resultado))
        calculos.clear()
 
    # se for um número
    else:
        entry.insert('end', val)

# Botões dos numeros -------------------------------------------<
button_numbers = []
calculos = []
row = 2
column = 0

for i in (range(1, 10)):
    button_numbers.append(i)
button_numbers.append(0)

for numb in button_numbers:
    button = ctk.CTkButton(master=root, text=numb, width=60, 
                           command=lambda f=numb: button_numb(f))
    button.grid(row=row, column=column, pady=10, padx=10)
    
    column += 1
    if column == 3:
        column = 0
        row += 1
# >-----------------------------------------------------------
# Entrada
entry = ctk.CTkEntry(root, width=200)
entry.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

conta = ctk.CTkLabel(master=root, text="", text_color="gray")
conta.grid(row=0, column=0, sticky="W",columnspan=3)

# botões de interação
igual = ctk.CTkButton(root, text='=', width=160, command=lambda: button_numb('='))
igual.grid(row=5, column=1, columnspan=2, pady=10, padx=10)

clear = ctk.CTkButton(root, text='Clear', width=100, command=lambda: button_numb('clear'))
clear.grid(row=5, column=3, padx=10, pady=10)

# botões de conta
soma = ctk.CTkButton(root, text='+', width=100,command=lambda: button_numb('+'))
soma.grid(row=1, column=3, padx=10)

menos = ctk.CTkButton(root, text='-', width=100,command=lambda: button_numb('-'))
menos.grid(row=2, column=3)

mult = ctk.CTkButton(root, text='*', width=100,command=lambda: button_numb('*'))
mult.grid(row=3, column=3)

div = ctk.CTkButton(root, text='/', width=100,command=lambda: button_numb('/'))
div.grid(row=4, column=3)

root.mainloop()
