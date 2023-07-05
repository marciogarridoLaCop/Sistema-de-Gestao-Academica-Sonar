# matriculas.py
from prompt_toolkit import prompt
from prompt_toolkit.validation import ValidationError, Validator
from colorama import Fore, Style
import pickle
import uuid

try:
    with open('matriculas.pkl', 'rb') as f:
        matriculas = pickle.load(f)
except FileNotFoundError:
    matriculas = []

def efetuar_matricula():
    while True:
        print(Fore.CYAN + "\nEfetuar Matrícula" + Style.RESET_ALL)
        matricula_aluno = input("Matrícula do aluno: ")
        codigo_disciplina = input("Código da disciplina: ")
        print("\nConfirme as informações:")
        print(f"Matrícula do aluno: {matricula_aluno}")
        print(f"Código da disciplina: {codigo_disciplina}")
        confirmacao = input("\nAs informações estão corretas? (s/n): ")
        if confirmacao.lower() == 's':
            break
    id_matricula = str(uuid.uuid4())
    matriculas.append({"id": id_matricula, "matricula_aluno": matricula_aluno, "codigo_disciplina": codigo_disciplina})
    with open('matriculas.pkl', 'wb') as f:
        pickle.dump(matriculas, f)
    print(Fore.GREEN + f"Matrícula efetuada com o ID {id_matricula}" + Style.RESET_ALL)

def pesquisar_matriculas():
    id_matricula = input("ID da matrícula: ")
    for matricula in matriculas:
        if matricula["id"] == id_matricula:
            print(matricula)
            return
    print(Fore.RED + "Matrícula não encontrada" + Style.RESET_ALL)
