from search import search_prompt


def main():
    question = "Qual o faturamento da SuperTechIABrazil?"
    chain = search_prompt(question)

    question = "Quantos clientes temos em 2024?"
    chain = search_prompt(question)

    if not chain:
        print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
        return

    pass


if __name__ == "__main__":
    main()
