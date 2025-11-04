import time
import pytest
from src.fatura import (
    FaturaService,
    InMemoryFaturaRepository,
    StubEmailService,
    MockGatewayPagamento,
)


@pytest.fixture
def service():
    repo = InMemoryFaturaRepository()
    email = StubEmailService()
    gateway = MockGatewayPagamento(aprovar=True)
    return FaturaService(repo, email, gateway)


@pytest.mark.parametrize(
    "qtd, preco, desconto, esperado",
    [(2, 10.0, 0, 20.0), (3, 5.0, 10, 13.5)],
)
def test_calcula_total(service, qtd, preco, desconto, esperado):
    assert service.calcular_total(qtd, preco, desconto) == pytest.approx(esperado)


def test_excecao_qtd_invalida(service):
    with pytest.raises(ValueError):
        service.calcular_total(0, 10.0, 0)


def test_envia_email_apos_pagamento_aprovado(service):
    service.fechar_fatura("cli-1", [(2, 10.0)])
    assert len(service.email.enviados) == 1


@pytest.mark.slow
def test_deve_ser_rapido(service):
    t0 = time.perf_counter()
    service.fechar_fatura("cli-1", [(3, 5.0)])
    assert (time.perf_counter() - t0) < 0.2


def test_fluxo_inteiro(service):
    fatura = service.fechar_fatura("cli-2", [(2, 10.0)])
    assert fatura.paga
    assert service.repo.obter("cli-2").total == 20.0
    assert service.email.enviados
