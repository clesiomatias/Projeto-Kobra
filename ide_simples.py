#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import subprocess
import os

class KobraIDE:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Kobra IDE - Python em Português")
        self.root.geometry("800x600")
        
        self.current_file = None
        self.setup_ui()
    
    def setup_ui(self):
        # Menu
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Arquivo", menu=file_menu)
        file_menu.add_command(label="Novo", command=self.new_file)
        file_menu.add_command(label="Abrir", command=self.open_file)
        file_menu.add_command(label="Salvar", command=self.save_file)
        file_menu.add_command(label="Salvar Como", command=self.save_as_file)
        
        run_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Executar", menu=run_menu)
        run_menu.add_command(label="Executar (F5)", command=self.run_code)
        
        # Toolbar
        toolbar = tk.Frame(self.root)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        
        tk.Button(toolbar, text="Novo", command=self.new_file).pack(side=tk.LEFT)
        tk.Button(toolbar, text="Abrir", command=self.open_file).pack(side=tk.LEFT)
        tk.Button(toolbar, text="Salvar", command=self.save_file).pack(side=tk.LEFT)
        tk.Button(toolbar, text="▶ Executar", command=self.run_code, bg="green", fg="white").pack(side=tk.LEFT)
        
        # Editor
        self.text_editor = scrolledtext.ScrolledText(self.root, wrap=tk.WORD)
        self.text_editor.pack(expand=True, fill=tk.BOTH)
        
        # Output
        output_frame = tk.Frame(self.root)
        output_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=5)
        
        tk.Label(output_frame, text="Saída:").pack(anchor=tk.W)
        self.output_text = scrolledtext.ScrolledText(output_frame, height=8)
        self.output_text.pack(fill=tk.BOTH, expand=True)
        
        # Keybindings
        self.root.bind('<F5>', lambda e: self.run_code())
        self.root.bind('<Control-s>', lambda e: self.save_file())
        self.root.bind('<Control-o>', lambda e: self.open_file())
        self.root.bind('<Control-n>', lambda e: self.new_file())
    
    def new_file(self):
        self.text_editor.delete(1.0, tk.END)
        self.current_file = None
        self.root.title("Kobra IDE - Novo Arquivo")
    
    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Arquivos Kobra", "*.kobra"), ("Todos os arquivos", "*.*")]
        )
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                self.text_editor.delete(1.0, tk.END)
                self.text_editor.insert(1.0, content)
            self.current_file = file_path
            self.root.title(f"Kobra IDE - {os.path.basename(file_path)}")
    
    def save_file(self):
        if self.current_file:
            content = self.text_editor.get(1.0, tk.END)
            with open(self.current_file, 'w', encoding='utf-8') as file:
                file.write(content)
            messagebox.showinfo("Salvo", "Arquivo salvo com sucesso!")
        else:
            self.save_as_file()
    
    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".kobra",
            filetypes=[("Arquivos Kobra", "*.kobra"), ("Todos os arquivos", "*.*")]
        )
        if file_path:
            content = self.text_editor.get(1.0, tk.END)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            self.current_file = file_path
            self.root.title(f"Kobra IDE - {os.path.basename(file_path)}")
            messagebox.showinfo("Salvo", "Arquivo salvo com sucesso!")
    
    def run_code(self):
        if not self.current_file:
            messagebox.showwarning("Aviso", "Salve o arquivo antes de executar")
            return
        
        self.save_file()
        self.output_text.delete(1.0, tk.END)
        
        try:
            result = subprocess.run(
                ['python3', 'kobra.py', self.current_file],
                capture_output=True,
                text=True,
                cwd=os.path.dirname(os.path.abspath(__file__))
            )
            
            if result.stdout:
                self.output_text.insert(tk.END, result.stdout)
            if result.stderr:
                self.output_text.insert(tk.END, f"Erro: {result.stderr}")
                
        except Exception as e:
            self.output_text.insert(tk.END, f"Erro ao executar: {e}")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    ide = KobraIDE()
    ide.run()