# Drogaria do Brasa (v1.0.0)

## O Problema
Pacientes crônicos frequentemente costumão esquecer as doses ou perdem o controle de seus medicamentos, comprometendo o tratamento.

## A Solução
Uma ferramenta de linha de comando para gerenciar protocolos de saúde com validação de dados.

## Tecnologias
- Python 3.12
- Typer (CLI)
- Pydantic (Validação)
- Pytest (Testes)
- Ruff (Linting)

## Instalação
1. Clone o repositório.
2. Instale as dependências: `pip install -r requirements.txt`

## Execução
```bash
python -m src.main add "Lisinopril" "10mg" 30
python -m src.main list
