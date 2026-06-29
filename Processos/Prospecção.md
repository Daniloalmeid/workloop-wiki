# 🔍 Prospecção de Clientes

> Duas abordagens: browser manual (gratuito) ou Apify (automático, pago).

## Abordagem 1: Browser Manual (Playwright) — RECOMENDADO

Sem custo. Usamos o navegador para acessar o Google Maps diretamente.

### Passo a passo

1. Pedir pro Hermes: "Busca leads de [NICHO] em [BAIRRO]"
2. Hermes abre Google Maps no navegador
3. Extrai: nome, telefone, endereço, avaliação
4. Tenta encontrar Instagram via curl no site do negócio
5. Compila tabela de leads

### Como pedir
"Busca material de construcao em Jaragua Sao Paulo no Google Maps"

### Resultado
Tabela com nome, telefone, endereço, Instagram (quando disponível).

## Abordagem 2: Apify (Automático) — Pago

Requer créditos no Apify (~$0,05/execução). Usar quando o browser não for viável.

**Setup:**
1. Instalar ator compass/crawler-google-places em console.apify.com
2. Adicionar cartão de crédito (vem $5/mês grátis)
3. Rodar via script: `python3 /root/scripts/prospeccao-diaria.py`

## Schedule Semanal (Browser Manual)

| Dia | Nicho | Região |
|-----|-------|--------|
| Seg 🏗️ | Material de Construção | Jaraguá |
| Ter 🐾 | Pet Shops | Jaraguá/Pirituba |
| Qua 💆 | Clínicas Estética + Salão | Jaraguá |
| Qui 🍕 | Restaurantes | Jaraguá |
| Sex 🔧 | Oficinas | Jaraguá |
| Sáb 🛒 | Mercados/Padarias | Jaraguá |
| Dom 🏫 | Outros | Jaraguá |

## Mensagens de Abordagem

### Material de Construção
```
Olá, tudo bem? Aqui é o Danilo, do Workloop.

Vi que sua loja aqui no Jaraguá tem potencial pra crescer com automação no WhatsApp.
A gente cria um sistema que atende orçamento 24h, dispara promoções e organiza pedidos.

Quer testar 15 dias grátis? Valeu!
```

### Pet Shop
```
Oi, Danilo do Workloop. Sistema que lembra vacinas, agenda banho, dispara ofertas de ração.
15 dias grátis sem fidelidade. Topa um teste?
```

### Clínica de Estética
```
Oi, Danilo do Workloop. WhatsApp automático: confirma consultas, lembretes, ofertas.
Menos falta, mais agendamento. 15 dias grátis?
```

## Dados

Os leads coletados ficam salvos em /root/leads/.
Cada arquivo tem data e nicho no nome.
