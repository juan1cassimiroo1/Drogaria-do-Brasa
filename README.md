# Med-Track CLI (v1.0.0)

## 🩺 O Problema
Pacientes crônicos frequentemente esquecem doses ou perdem o controle do estoque de seus medicamentos, comprometendo a eficácia do tratamento.

## 🚀 A Solução
Uma ferramenta de linha de comando robusta para gerenciar protocolos de saúde com validação rigorosa de dados.

## 🛠️ Tecnologias
- Python 3.12
- Typer (CLI)
- Pydantic (Validação)
- Pytest (Testes)
- Ruff (Linting)

## 📥 Instalação
1. Clone o repositório.
2. Instale as dependências: `pip install -r requirements.txt`

## 🏃 Execução
```bash
python -m src.main add "Lisinopril" "10mg" 30
python -m src.main list