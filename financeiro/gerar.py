#!/usr/bin/env python3
"""
📊 Workloop - Sistema Financeiro
Gera o Dashboard com cálculos automáticos.
Uso: python3 financeiro.py
"""

import json
from pathlib import Path

BASE = Path(__file__).parent

def carregar_dados():
    with open(BASE / "dados.json") as f:
        return json.load(f)

def gerar_dashboard(dados):
    custos = dados["custos_fixos"]
    total_custos = sum(custos.values())
    
    receitas = sum(c["valor_mensal"] for c in dados["clientes"])
    lucro = receitas - total_custos
    
    # Status dos clientes
    ativos = sum(1 for c in dados["clientes"] if c["status"] == "ativo")
    implantacao = sum(1 for c in dados["clientes"] if c["status"] == "teste_gratis")
    
    margem = f"{(lucro / receitas * 100):.0f}%" if receitas > 0 else "—"

    linhas = []
    linhas.append("# 📊 Dashboard — Workloop\n")
    linhas.append("> Centro de comando do Workloop Agent")
    linhas.append("> *Gerado automaticamente pelo sistema financeiro*\n")
    linhas.append("---\n")
    
    # === CUSTOS ===
    linhas.append("## 💰 Planilha de Custos & Lucro\n")
    linhas.append("| Item | Custo | Status |")
    linhas.append("|:-----|:-----:|:------:|")
    
    labels = {
        "vps": "☁️ VPS", "tailscale": "🔗 Tailscale", "deepseek_api": "🤖 DeepSeek API",
        "evolution_api": "📱 Evolution API", "supabase": "🗄️ Supabase",
        "replicate": "🎨 Replicate (FLUX)", "capcut": "🖼️ CapCut",
        "instagram": "📸 Instagram", "dominio": "🌐 Domínio", "outros": "📦 Outros"
    }
    
    for key, label in labels.items():
        valor = custos.get(key, 0)
        status = "🟢 Grátis" if valor == 0 else f"🔴 R$ {valor:.2f}"
        linhas.append(f"| {label} | R$ {valor:.2f} | {status} |")
    
    linhas.append(f"| **Total custos fixos** | **R$ {total_custos:.2f}** | |\n")
    
    # === RECEITAS ===
    linhas.append("### 📈 Receitas\n")
    linhas.append("| Cliente | Plano | Valor/mês | Status |")
    linhas.append("|:--------|:------|:---------:|:------:|")
    
    for c in dados["clientes"]:
        status_emoji = "🟢 Ativo" if c["status"] == "ativo" else "🟡 Teste" if c["status"] == "teste_gratis" else "🔴 Inativo"
        linhas.append(f"| {c['nome']} | {c['plano']} | R$ {c['valor_mensal']:.2f} | {status_emoji} |")
    
    linhas.append(f"| **Total receitas** | | **R$ {receitas:.2f}** | |\n")
    
    # === RESUMO ===
    linhas.append("### 📊 Resumo Financeiro\n")
    linhas.append("| Indicador | Valor |")
    linhas.append("|:----------|:-----:|")
    linhas.append(f"| 💰 **Receita total** | R$ {receitas:.2f} |")
    linhas.append(f"| 📉 **Custos totais** | R$ {total_custos:.2f} |")
    
    if lucro >= 0:
        linhas.append(f"| 📈 **Lucro líquido** | R$ **{lucro:.2f}** 🟢 |")
    else:
        linhas.append(f"| 📉 **Prejuízo** | -R$ **{abs(lucro):.2f}** 🔴 |")
    
    linhas.append(f"| 📊 **Margem** | {margem} |")
    linhas.append(f"| 🎯 **Meta curto prazo** | R$ {dados['meta_curto_prazo']:.2f}/mês |")
    linhas.append(f"| 🏆 **Meta longo prazo** | R$ {dados['meta_longo_prazo']:.2f}/mês |\n")
    
    # === METAS ===
    linhas.append("### 🎯 Metas Comerciais\n")
    
    metas = [
        (50, "🥇 1º cliente pagando → R$ 50-100/mês"),
        (500, "🥈 5 clientes → R$ 500/mês"),
        (1000, "🥉 10 clientes → R$ 1.000/mês"),
        (2000, "🏆 20+ clientes → R$ 2.000+/mês"),
    ]
    for valor_meta, texto in metas:
        checked = "x" if receitas >= valor_meta else " "
        linhas.append(f"- [{checked}] {texto}")
    
    linhas.append("")
    
    # === PRECIFICACAO ===
    precos = dados["precos"]
    linhas.append("### 📝 Tabela de Preços\n")
    linhas.append("| Plano | Recursos | Preço |")
    linhas.append("|:------|:---------|:-----:|")
    linhas.append(f"| 🟢 **Básico** | WhatsApp + Database | R$ {precos['basico']}/mês |")
    linhas.append(f"| 🔵 **Profissional** | WhatsApp + Instagram + Database + n8n | R$ {precos['profissional']}/mês |")
    linhas.append(f"| 🟣 **Premium** | Tudo + Posts + Suporte Prioritário | R$ {precos['premium']}/mês |")
    
    linhas.append("\n---\n")
    
    # === CLIENTES ===
    linhas.append("## 📋 Clientes\n")
    linhas.append("| Cliente | WhatsApp | Instagram | Database | n8n | Status |")
    linhas.append("|---------|:--------:|:---------:|:--------:|:---:|:------:|")
    
    for c in dados["clientes"]:
        nome_link = f"[{c['nome']}](Clientes/{c['nome']}/index.md)"
        status = "🟢 Ativo" if c["status"] == "ativo" else "🟡 Implantação" if c["status"] == "teste_gratis" else "🔴 Inativo"
        linhas.append(f"| {nome_link} | ✅ | ⏳ | ✅ | ✅ | {status} |")
    
    linhas.append(f"\n**Total:** {ativos} ativo(s) · {implantacao} em implantação\n")
    
    # === PROXIMOS PASSOS ===
    linhas.append("## 🎯 Próximos Passos\n")
    linhas.append("- [ ] 📱 **Testar WhatsApp** (Baileys ou Business Cloud)")
    linhas.append("- [ ] 🔐 **Restaurar Google Calendar OAuth**")
    linhas.append("- [ ] 🛒 **Povoar Nuvemshop**")
    linhas.append("- [ ] 🧩 **Explorar Blueprints/Profile Builder**")
    linhas.append("- [ ] 📢 **Postar no Instagram** (semanal)")
    linhas.append("- [ ] 📋 **Onboarding novo cliente**\n")
    
    # === METRICAS ===
    linhas.append("## 📊 Métricas\n")
    linhas.append("| Métrica | Valor |")
    linhas.append("|---------|:-----:|")
    linhas.append(f"| 👥 Clientes | {len(dados['clientes'])} |")
    linhas.append(f"| 💰 Receita mensal | R$ {receitas:.2f} |")
    linhas.append(f"| 📈 Lucro mensal | R$ {lucro:.2f} |")
    
    return "\n".join(linhas)

def atualizar_dashboard():
    dados = carregar_dados()
    md = gerar_dashboard(dados)
    
    with open(BASE.parent / "Dashboard.md", "w") as f:
        f.write(md)
    
    print(f"✅ Dashboard atualizado!")
    print(f"   Receitas: R$ {sum(c['valor_mensal'] for c in dados['clientes']):.2f}")
    print(f"   Custos:   R$ {sum(dados['custos_fixos'].values()):.2f}")
    print(f"   Lucro:    R$ {sum(c['valor_mensal'] for c in dados['clientes']) - sum(dados['custos_fixos'].values()):.2f}")

if __name__ == "__main__":
    atualizar_dashboard()
