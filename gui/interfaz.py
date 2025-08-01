import tkinter as tk
from tkinter import messagebox
from logic.planificador import generar_plan

def iniciar_interfaz():
    def ejecutar_plan():
        try:
            presupuesto_str = entry_presupuesto.get().strip()
            if not presupuesto_str:
                raise ValueError("Presupuesto vacío")
            presupuesto = float(presupuesto_str)
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce un presupuesto válido (número).")
            return

        filtros = {
            "proteina": var_proteina.get(),
            "lacteos": var_lacteos.get(),
            "verduras": var_verduras.get()
        }

        resultado = generar_plan(presupuesto, filtros)
        text_resultado.delete(1.0, tk.END)
        text_resultado.insert(tk.END, resultado)

    ventana = tk.Tk()
    ventana.title("Planificador de Comida Equilibrada")
    ventana.geometry("600x500")
    ventana.configure(bg="white")

    fuente_normal = ("Helvetica", 12)

    # ---------------- INTERFAZ VISUAL ----------------
    frame = tk.Frame(ventana, bg="white")
    frame.pack(pady=20)

    tk.Label(frame, text="Presupuesto (€):", bg="white", fg="black", font=fuente_normal).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    entry_presupuesto = tk.Entry(frame, font=fuente_normal, width=20)
    entry_presupuesto.grid(row=0, column=1, padx=5, pady=5)

    var_proteina = tk.BooleanVar()
    var_lacteos = tk.BooleanVar()
    var_verduras = tk.BooleanVar()

    tk.Checkbutton(frame, text="Incluir proteína", variable=var_proteina, bg="white", font=fuente_normal).grid(row=1, column=0, sticky="w", padx=5, pady=5)
    tk.Checkbutton(frame, text="Incluir lácteos", variable=var_lacteos, bg="white", font=fuente_normal).grid(row=2, column=0, sticky="w", padx=5, pady=5)
    tk.Checkbutton(frame, text="Incluir verduras", variable=var_verduras, bg="white", font=fuente_normal).grid(row=3, column=0, sticky="w", padx=5, pady=5)

    tk.Button(frame, text="Generar Plan", command=ejecutar_plan, bg="#cce5ff", font=fuente_normal).grid(row=4, column=0, columnspan=2, pady=10)

    text_resultado = tk.Text(ventana, height=15, width=70, font=("Courier", 10), bg="#f5f5f5")
    text_resultado.pack(padx=10, pady=10)

    ventana.mainloop()
