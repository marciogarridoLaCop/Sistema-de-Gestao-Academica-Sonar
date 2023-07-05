# main.py
from colorama import Fore, Style
import alunos
import disciplina
import matricula

def main():
    while True:
        print(Fore.CYAN + "\n" + "="*30)
        print(Fore.YELLOW + "SISTEMA DE GESTÃO ACADÊMICA")
        print(Fore.CYAN + "="*30)
        print(Fore.GREEN + "\nPor favor, escolha uma das opções abaixo:")
        print("\n1. Cadastrar aluno")
        print("2. Cadastrar disciplina")
        print("3. Efetuar matrícula")
        print("4. Pesquisar aluno")
        print("5. Pesquisar disciplina")
        print("6. Pesquisar matrículas")
        print("7. Sair")
        print(Fore.CYAN + "\n" + "="*30 + "\n" + Style.RESET_ALL)
        opcao = input("Digite o número da opção desejada: ")
        if opcao == "1":
            alunos.cadastrar_aluno()
        elif opcao == "2":
            disciplina.cadastrar_disciplina()
        elif opcao == "3":
            matricula.efetuar_matricula()
        elif opcao == "4":
            alunos.pesquisar_aluno()
        elif opcao == "5":
            disciplina.pesquisar_disciplina()
        elif opcao == "6":
            matricula.pesquisar_matriculas()
        elif opcao == "7":
            break
        else:
            print(Fore.RED + "\nOpção inválida. Por favor, tente novamente." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
