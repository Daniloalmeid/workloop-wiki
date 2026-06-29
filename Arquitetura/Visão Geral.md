# 🏗️ Visão Geral da Arquitetura

## Diagrama

```text
👤 DONO (Telegram)
      │
      ▼
┌─────────────┐     ┌─────────┐     ┌──────────────┐
│   Hermes    │────▶│   n8n   │────▶│  Supabase    │
│   (Agente)  │◀────│(Orquest)│◀────│  (Banco)     │
└──────┬──────┘     └─────────┘     └──────────────┘
       │
       ▼
┌─────────────┐
│ Evolution   │
│ API         │
│ (WhatsApp)  │
└──────┬──────┘
       │
       ▼
👥 CLIENTES (WhatsApp)
```

## Componentes

| Componente | Função | Detalhes |
|---|---|---|
| **Hermes** | Cérebro | Agente IA que entende linguagem natural, mantém memória, executa tarefas |
| **n8n** | Orquestrador | Workflows: agendamento, lembretes, integrações |
| **Evolution API** | Bridge WhatsApp | Conecta WhatsApp via Baileys, expõe API REST |
| **Supabase** | Banco de dados | PostgreSQL cloud: clientes, pacientes, procedimentos, estoque |
| **Todoist** | Tarefas | Lista de afazeres do dono |

## Decisões-chave
- [[Decisoes/Decisões de Arquitetura]]
