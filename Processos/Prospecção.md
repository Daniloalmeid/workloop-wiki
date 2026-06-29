# 🔍 Prospecção de Clientes

## Regioes Alvo (7 bairros)
Jaragua · Pirituba · Perus · Sao Domingos · Brasilandia · Lapa · Caieiras

## Abordagem
Usar o navegador (Playwright) para acessar Google Maps diretamente.
Sem custo. 1 nicho por dia.

## Schedule Semanal

| Dia | Nicho |
|-----|-------|
| Seg | Material de Construcao |
| Ter | Pet Shops |
| Qua | Clinicas Estetica + Salao |
| Qui | Restaurantes + Lanchonetes |
| Sex | Oficinas + Borracharias |
| Sab | Mercados + Padarias + Acougues |
| Dom | Outros (academias, escolas, farmacias) |

## Banco de Leads (SQLite)

Arquivo: /root/leads/leads.db

### Antes de enviar, consultar:
SELECT status FROM leads WHERE telefone = '5511XXXXXXXXX';

### Status possiveis:
- enviado = ja recebeu mensagem (nao reenviar)
- fixo = numero fixo sem WhatsApp
- nao_contatado = novo, pode enviar

### Inserir novo lead apos envio:
INSERT INTO leads (nome, telefone, endereco, bairro, nicho, avaliacao, status, data_envio)
VALUES ('Nome', '5511XXXXXXX', 'Endereco', 'Bairro', 'Nicho', 4.5, 'enviado', datetime('now'));

## Mensagens de Abordagem

### Material de Construcao
"Ola, tudo bem? Aqui e o Danilo, do Workloop. Vi que sua loja na regiao tem potencial pra crescer com automacao no WhatsApp. Sistema que atende orcamento 24h, dispara promocoes e organiza pedidos. 15 dias gratis. Valeu!"

### Pet Shop
"Oi, Danilo do Workloop. Sistema que lembra vacinas, agenda banho, dispara ofertas. 15 dias gratis. Topa?"

### Clinica de Estetica
"Oi, Danilo do Workloop. WhatsApp automatico: confirma consultas, lembretes, ofertas. Menos falta, mais agendamento. 15 dias gratis?"
