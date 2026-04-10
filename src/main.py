import typer
from rich.console import Console
from rich.table import Table
from .models import Medicamento
from .service import MedicamentoService

app = typer.Typer(help="Med-Track CLI - Sistema de Gestão de Medicamentos")
console = Console()
service = MedicamentoService()

@app.command()
def add(nome: str, dosagem: str, estoque: int):
    """Adiciona um novo medicamento (Ex: add "Aspirina" "500mg" 30)"""
    try:
        med = Medicamento(nome=nome, dosagem=dosagem, estoque=estoque)
        service.adicionar(med)
        console.print(f"[bold green]✔[/bold green] {nome} cadastrado com sucesso!")
    except Exception as e:
        console.print(f"[bold red]❌ Erro de Validação:[/bold red] {e}")

@app.command()
def list():
    """Lista todos os medicamentos na tela"""
    meds = service.listar()
    if not meds:
        console.print("[yellow]Nenhum medicamento no estoque.[/yellow]")
        return

    table = Table(title="Controle de Estoque - Medicamentos")
    table.add_column("ID", style="dim", no_wrap=True)
    table.add_column("Nome", style="cyan bold")
    table.add_column("Dosagem", style="magenta")
    table.add_column("Estoque", style="green", justify="right")

    for m in meds:
        table.add_row(str(m.id)[:8], m.nome, m.dosagem, str(m.estoque))
    
    console.print(table)

@app.command()
def remove(nome: str):
    """Remove um medicamento pelo nome"""
    if service.remover(nome):
        console.print(f"[bold yellow]⚠[/bold yellow] {nome} foi removido.")
    else:
        console.print(f"[bold red]❌ Erro:[/bold red] '{nome}' não encontrado.")

if __name__ == "__main__":
    app()