# disciplinas.py
from prompt_toolkit import prompt
from prompt_toolkit.validation import ValidationError, Validator
from colorama import Fore, Style
import pickle
import uuid

try:
    with open('disciplinas.pkl', 'rb') as f:
        disciplinas = pickle.load(f)
except FileNotFoundError:
    disciplinas = []

def cadastrar_disciplina():
    while True:
        print(Fore.CYAN + "\nCadastro de Disciplina" + Style.RESET_ALL)
        nome = input("Nome da disciplina: ")
        turno = input("Turno: ")
        codigo = input("Código da disciplina: ")
        periodo = input("Período: ")
        print("\nConfirme as informações:")
        print(f"Nome da disciplina: {nome}")
        print(f"Turno: {turno}")
        print(f"Código da disciplina: {codigo}")
        print(f"Período: {periodo}")
        confirmacao = input("\nAs informações estão corretas? (s/n): ")
        if confirmacao.lower() == 's':
            break
    id_disciplina = str(uuid.uuid4())
    disciplinas.append({"id": id_disciplina, "nome": nome, "turno": turno, "codigo": codigo, "periodo": periodo})
    with open('disciplinas.pkl', 'wb') as f:
        pickle.dump(disciplinas, f)
    print(Fore.GREEN + f"Disciplina cadastrada com o ID {id_disciplina}" + Style.RESET_ALL)

def pesquisar_disciplina():
    id_disciplina = input("ID da disciplina: ")
    for disciplina in disciplinas:
        if disciplina["id"] == id_disciplina:
            print(disciplina)
            return
    print(Fore.RED + "Disciplina não encontrada" + Style.RESET_ALL)
