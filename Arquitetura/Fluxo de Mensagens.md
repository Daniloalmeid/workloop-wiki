# 📨 Fluxo de Mensagens

## Fluxo Geral (Atendimento)

```text
📲 Cliente → WhatsApp
       │
       ▼
Evolution API → Webhook → n8n
                           │
                           ▼
                        Hermes (responde)
                           │
                           ▼
                n8n → Evolution API → 📲 Cliente
```

## Fluxo de Agendamento

```text
📲 "Quero agendar" → WhatsApp
       │
       ▼
Evolution → n8n (detecta intenção)
              │
              ▼
        n8n scheduling agent
        (conversa direto com paciente)
              │
              ├── Consulta Google Calendar
              ├── Confirma horário
              ├── Salva no Supabase
              └── Notifica Hermes
```

## Regras
- **n8n** só conversa sobre agendamento
- **Hermes** cuida de todo o resto
- **Google Calendar** é a fonte da verdade para horários
