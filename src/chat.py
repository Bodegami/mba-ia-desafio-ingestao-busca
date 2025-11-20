from search import search_prompt


def main():
    print("Iniciando chat. Digite sua pergunta ou 'exit' para sair.")

    while True:
        try:
            question = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nSaindo...")
            break

        if not question:
            continue

        if question.lower() in ("exit", "sair"):
            print("Saindo...")
            break

        try:
            chain = search_prompt(question)
        except Exception as e:
            print(f"Erro ao processar a pergunta: {e}")
            continue

        if not chain:
            print(
                "Não foi possível iniciar o chat. Verifique os erros de inicialização."
            )
        else:
            print(chain)


if __name__ == "__main__":
    main()
