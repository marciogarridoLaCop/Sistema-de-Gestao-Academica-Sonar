# alunos.py
from datetime import datetime
import re
from prompt_toolkit import prompt
from prompt_toolkit.validation import ValidationError, Validator
from colorama import Fore, Style
import pickle
import uuid

try:
    with open('alunos.pkl', 'rb') as f:
        alunos = pickle.load(f)
except FileNotFoundError:
    alunos = []

class DateValidator(Validator):
    def validate(self, document):
        text = document.text
        if len(text) != 10 or text[2] != '/' or text[5] != '/':
            raise ValidationError(message='Data inválida. Por favor, insira a data no formato dd/mm/yyyy.', cursor_position=len(text)-1)

def validar_email(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    return False

def cadastrar_aluno():
    while True:
        print(Fore.CYAN + "\nCadastro de Aluno" + Style.RESET_ALL)
        nome = input("Nome: ")
        data_nascimento = prompt("Data de nascimento (dd/mm/yyyy): ", validator=DateValidator())
        genero = input("Gênero: ")
        email = input("Email: ")
        while not validar_email(email):
            print(Fore.RED + "Email inválido. Por favor, insira um email válido." + Style.RESET_ALL)
            email = input("Email: ")
        print("\nConfirme as informações:")
        print(f"Nome: {nome}")
        print(f"Data de nascimento: {data_nascimento}")
        print(f"Gênero: {genero}")
        print(f"Email: {email}")
        confirmacao = input("\nAs informações estão corretas? (s/n): ")
        if confirmacao.lower() == 's':
            break
    id_aluno = str(uuid.uuid4())
    alunos.append({"id": id_aluno, "nome": nome, "data_nascimento": data_nascimento, "genero": genero, "email": email})
    with open('alunos.pkl', 'wb') as f:
        pickle.dump(alunos, f)
    print(Fore.GREEN + f"Aluno cadastrado com o ID {id_aluno}" + Style.RESET_ALL)

def pesquisar_aluno():
    id_aluno = input("ID do aluno: ")
    for aluno in alunos:
        if aluno["id"] == id_aluno:
            print(aluno)
            return
    print(Fore.RED + "Aluno não encontrado" + Style.RESET_ALL)