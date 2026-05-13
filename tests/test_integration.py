
from src.service import MedicamentoService

def test_viacep_integration_real():
    service = MedicamentoService()
    # Testando com o CEP da SQS 102 em Brasília
    resultado = service.buscar_cep("70150900")
    
    assert resultado is not None
    assert "SQS 102" in resultado
    assert "Brasília" in resultado