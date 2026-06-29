---
cssclasses:
  - decisão
---
# 🗺️ Decisões de Arquitetura

## ADRs (Architecture Decision Records)

### ADR-001: Single-agent (não perfis separados)
- **Data:** Junho/2026
- **Contexto:** Testamos perfil separado para Sofia (Google Calendar) e não funcionou
- **Decisão:** Hermes é o único agente. Clientes compartilham o mesmo agente com isolamento via DB
- **Consequência:** Mais simples de manter, menos overhead

### ADR-002: Supabase como banco primário
- **Data:** Junho/2026
- **Contexto:** PostgreSQL local no Docker perdia dados com restart
- **Decisão:** Migrar para Supabase (cloud, backup automático)
- **Consequência:** Dados seguros, acessível de qualquer VPS

### ADR-003: Google Calendar como scheduling
- **Data:** Junho/2026
- **Contexto:** Precisávamos de calendário compartilhado
- **Decisão:** Google Calendar é a única fonte da verdade para horários
- **Consequência:** Cliente mantém calendário que já usa

### ADR-004: n8n só agenda, não conversa
- **Data:** Junho/2026
- **Contexto:** n8n tem agente interno, mas Hermes é melhor pra conversar
- **Decisão:** n8n só conversa sobre agendamento. O resto é Hermes
- **Consequência:** Funções bem definidas, sem conflito

## Roadmap
- [[Decisoes/Roadmap]]
