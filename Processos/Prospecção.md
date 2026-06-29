# 🔍 Prospecção Automática

> Sistema automatizado via Apify + Hermes cron. 1 nicho/dia.

## Schedule Semanal

| Dia | Nicho |
|-----|-------|
| Seg 🏗️ | Material de Construção |
| Ter 🐾 | Pet Shops |
| Qua 💆 | Clínicas Estética + Salão |
| Qui 🍕 | Restaurantes + Lanchonetes |
| Sex 🔧 | Oficinas + Borracharias |
| Sáb 🛒 | Mercados + Padarias + Açougues |
| Dom 🏫 | Outros (academias, escolas, farmácias) |

## Como funciona

1. **08:00** — Cron job dispara no Hermes
2. Busca Google Maps via Apify
3. Salva em /root/leads/
4. Entrega relatório no Telegram

**Custo:** ~$1,50/mês de Apify

## Mensagens de Abordagem

### Material de Construção
Olá, tudo bem? Aqui é o Danilo, do Workloop. Vi sua loja aqui no Jaraguá. A gente automatiza WhatsApp pra você: orçamento 24h, promoções, pedidos. 15 dias grátis. Valeu!

### Pet Shop
Oi, Danilo do Workloop. Sistema que lembra vacinas, agenda banho, dispara ofertas. 15 dias grátis sem fidelidade. Topa um teste?

### Clínica de Estética
Oi, Danilo do Workloop. WhatsApp automático pra sua clínica: confirma consultas, lembretes, ofertas. Menos falta, mais agendamento. 15 dias grátis?
