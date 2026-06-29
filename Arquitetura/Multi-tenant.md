# 🏢 Estratégia Multi-tenant

## Arquitetura
Cada cliente compartilha o mesmo Hermes (single-agent), com dados isolados via `cliente_id` no Supabase.

```text
DONO (Telegram) ─── Hermes ─── Supabase
                                    │
                          ┌─────────┼─────────┐
                          │         │         │
                     Clínica A  Clínica B  Padaria C
                     (WhatsApp) (WhatsApp) (WhatsApp)
```

## Isolamento
- Tabelas no Supabase têm `cliente_id`
- Cada consulta SQL filtra por `cliente_id`
- Dono vê tudo; cliente vê só os dados dele

## Canais
| Quem | Canal | Ferramenta |
|---|---|---|
| Dono (Danilo) | Telegram | Hermes |
| Clientes | WhatsApp | Evolution API |
