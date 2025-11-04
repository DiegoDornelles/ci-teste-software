class ItemFatura:
    def __init__(self, quantidade, preco_unitario):
        if quantidade <= 0:
            raise ValueError("Quantidade inválida")
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    def subtotal(self):
        return self.quantidade * self.preco_unitario


class Fatura:
    def __init__(self, cliente, itens, desconto_pct=0):
        self.cliente = cliente
        self.itens = itens
        self.desconto_pct = desconto_pct
        self.total = 0.0
        self.paga = False

    def calcular_total(self, imposto_pct=0):
        bruto = sum(i.subtotal() for i in self.itens)
        desconto = bruto * (self.desconto_pct / 100)
        imposto = (bruto - desconto) * (imposto_pct / 100)
        self.total = bruto - desconto + imposto
        return round(self.total, 2)


class InMemoryFaturaRepository:
    def __init__(self):
        self.dados = {}

    def salvar(self, fatura):
        self.dados[fatura.cliente] = fatura

    def obter(self, cliente):
        return self.dados.get(cliente)


class StubEmailService:
    def __init__(self):
        self.enviados = []

    def enviar_cobranca(self, msg):
        self.enviados.append(msg)


class MockGatewayPagamento:
    def __init__(self, aprovar=True):
        self.aprovar = aprovar

    def pagar(self, dados):
        return {"status": "aprovado" if self.aprovar else "negado", "id": "123"}


class FaturaService:
    def __init__(self, repo, email_service, gateway):
        self.repo = repo
        self.email = email_service
        self.gateway = gateway

    def calcular_total(self, qtd, preco, desconto_pct=0):
        if qtd <= 0:
            raise ValueError("Quantidade inválida")
        item = ItemFatura(qtd, preco)
        fatura = Fatura("cli-1", [item], desconto_pct)
        return fatura.calcular_total()

    def fechar_fatura(self, cliente, itens, desconto_pct=0):
        fatura = Fatura(cliente, [ItemFatura(q, p) for q, p in itens], desconto_pct)
        fatura.calcular_total()
        resposta = self.gateway.pagar({"cliente": cliente, "valor": fatura.total})
        if resposta["status"] == "aprovado":
            fatura.paga = True
            self.repo.salvar(fatura)
            self.email.enviar_cobranca(f"Cobrança enviada para {cliente}")
        return fatura
