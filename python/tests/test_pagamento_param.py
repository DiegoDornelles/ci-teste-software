# python/tests/test_pagamento_param.py
import pytest
from unittest.mock import Mock
from src.fatura import InMemoryFaturaRepository, StubEmailService, FaturaService

@pytest.mark.parametrize(
    "gateway_behavior, esperado_pago, esperado_email",
    [
        ("aprovado", True, 1),
        ("negado", False, 0),
        ("erro", False, 0),
    ]
)
def test_pagamento_parametrizado(gateway_behavior, esperado_pago, esperado_email):
    """
    Testa três cenários do gateway:
      - aprovado -> fatura.paga True, fatura salva no repo e e-mail enviado
      - negado   -> fatura.paga False, não salvo, sem e-mail
      - erro     -> gateway lança exceção -> comportamento: exceção propagada
    Ajuste as expectativas se seu FaturaService tratar exceções de forma diferente.
    """
    # arrange
    repo = InMemoryFaturaRepository()
    email = StubEmailService()

    if gateway_behavior == "aprovado":
        gateway = Mock()
        gateway.pagar.return_value = {"status": "aprovado", "id": "123"}
        raises = None
    elif gateway_behavior == "negado":
        gateway = Mock()
        gateway.pagar.return_value = {"status": "negado", "id": "000"}
        raises = None
    else:  # erro
        gateway = Mock()
        gateway.pagar.side_effect = RuntimeError("Gateway indisponível")
        raises = RuntimeError

    service = FaturaService(repo, email, gateway)

    # act / assert
    if raises:
        with pytest.raises(raises):
            service.fechar_fatura("cli-param", [(1, 10.0)])
        # depois da exceção, garantir que nada foi persistido/enviado
        assert repo.obter("cli-param") is None
        assert len(email.enviados) == 0
    else:
        fatura = service.fechar_fatura("cli-param", [(1, 10.0)])
        assert fatura.paga is esperado_pago
        if esperado_pago:
            assert repo.obter("cli-param") is not None
            assert len(email.enviados) >= esperado_email
        else:
            assert repo.obter("cli-param") is None
            assert len(email.enviados) == 0
