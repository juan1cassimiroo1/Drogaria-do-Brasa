
from src.service import MedicamentoService

def test_viacep_integration_real():
    service = MedicamentoService()
    resultado = service.buscar_cep("70150900")
    
    assert resultado is not None
    assert "Brasilia" in resultado
    assert "DF" in resultado