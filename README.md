# Desafio MBA Engenharia de Software com IA - Full Cycle

Este repositório contém uma solução de ingestão e busca com chat (exemplo para o desafio do MBA).

## Pré-requisitos

- Docker e Docker Compose instalados
- Python 3.8+ instalado
- (Opcional) Ambiente virtual Python (venv)

## Instalação

1. Clone o repositório (se ainda não o fez):

```powershell
git clone <url-do-repositorio>
cd mba-ia-desafio-ingestao-busca
```

2. (Opcional) Crie e ative um ambiente virtual Python:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Instale as dependências Python:

```powershell
pip install -r requirements.txt
```

## Configuração de variáveis de ambiente

Antes de executar a aplicação, renomeie o arquivo `.env.example` para `.env` e preencha as informações necessárias (chaves de API, strings de conexão, etc.). Exemplos de comandos:

```powershell
# Copiar o exemplo para .env (PowerShell)
Copy-Item .env.example .env

# Ou renomear o arquivo
Rename-Item .env.example .env
```

Se estiver em bash/sh, use:

```bash
cp .env.example .env
```

Abra o arquivo `.env` em um editor e preencha as variáveis conforme o projeto (por exemplo, chaves de serviços externos, parâmetros de DB, etc.).

## Ordem de execução

1. Subir o banco de dados (com Docker Compose):

```powershell
docker compose up -d
```

2. Executar ingestão do PDF:

```powershell
python src/ingest.py
```

3. Rodar o chat:

```powershell
python src/chat.py
```

## Observações

- Os comandos acima assumem que o `docker` está acessível e que o `docker compose` do seu sistema está configurado.
- Se você usar outro shell (cmd.exe, bash), ajuste os comandos de ativação do ambiente virtual conforme necessário.
- Para depuração, confira os arquivos em `src/` (`ingest.py`, `chat.py`, `search.py`).

## Contato

Para dúvidas ou melhorias, abra uma issue ou um pull request no repositório.