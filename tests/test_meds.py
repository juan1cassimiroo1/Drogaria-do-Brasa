import pytest
import os
from src.service import MedicamentoService
from src.models import Medicamento

@pytest.fixture
def service_temporario():
    """Cria um serviço que usa um arquivo de teste e o deleta depois."""
    service = MedicamentoService()
    service.file_path = "test_db.json"
    service.db = []
    yield service
    if os.path.exists("test_db.json"):
        os.remove("test_db.json")

def test_adicionar_medicamento_valido(service_temporario):
    med = Medicamento(nome="Aspirina", dosagem="100mg", estoque=10)
    service_temporario.adicionar(med)
    assert len(service_temporario.listar()) == 1
    assert service_temporario.listar()[0].nome == "Aspirina"

def test_estoque_negativo_deve_falhar():
    # Caso inválido (Requisito da Etapa 9)
    with pytest.raises(ValueError):
        Medicamento(nome="Erro", dosagem="1mg", estoque=-1)

def test_remover_medicamento_inexistente(service_temporario):
    # Caso limite (Requisito da Etapa 9)
    resultado = service_temporario.remover("Inexistente")
    assert resultado is False