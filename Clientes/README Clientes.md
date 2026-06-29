---
tags:
  - clientes
---
# 📋 Clientes Workloop

> Base centralizada de todos os clientes, serviços ativos e configurações.
> Atualizado em **29/06/2026**

## 📊 Visão Geral

| Cliente | WhatsApp | Instagram | Database | Status |
|---------|:--------:|:---------:|:--------:|:------:|
| [Cliente 1 - Clínica de Estética](./Cliente%201%20-%20Cl%C3%ADnica%20de%20Est%C3%A9tica/index.md) | ✅ | ⏳ | ✅ | 🟢 Ativo |

## 📂 Estrutura por Cliente

Cada cliente segue o mesmo padrão de pastas:

```
Clientes/
├── Cliente - Nome/
│   ├── index.md           → Visão geral, dados básicos, status
│   ├── whatsapp.md        → Config WhatsApp + Evolution API
│   ├── instagram.md       → Instagram, posts, prospecção
│   ├── database.md        → Tabelas Supabase, queries
│   ├── automacoes.md      → Fluxos n8n, agendamentos
│   └── historico.md       → Histórico de suporte e decisões
```

## 🚀 Novo Cliente — Checklist

- [ ] Criar pasta em `/root/clientes/<id>/` (servidor)
- [ ] Criar pasta no wiki `Clientes/Cliente - Nome/`
- [ ] Preencher index.md com dados básicos
- [ ] Configurar WhatsApp (Evolution API)
- [ ] Criar tabelas no Supabase
- [ ] Configurar n8n workflows
- [ ] Testar Instagram (se aplicável)
- [ ] Registrar credenciais em `memoria.json`

---

> 📁 Estrutura mantida pelo Hermes
