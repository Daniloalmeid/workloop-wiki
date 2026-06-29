# 🎨 Geração de Imagens

Três métodos disponíveis para criar imagens para posts de Instagram e materiais visuais.

## 1️⃣ Replicate (FLUX) — 🔥 Principal
Geração por IA via API, melhor qualidade.

```python
# API Key: r8_YUd...
# Modelo: black-forest-labs/flux-dev
# Tamanho: 1024x1024 (square)
# Tempo: ~10-15 segundos
```

**Dicas de Prompt:**
| Tipo | Prompt |
|------|--------|
| 📸 **Foto realista** | "Professional photo of [cena], warm golden hour, high detail 8K, no text" |
| 🌆 **Bairro** | "Vibrant Brazilian neighborhood street, colorful shops, sunset, community" |
| 🎨 **Ilustração** | "Vector illustration, flat design, vibrant colors, clean, no text" |
| 💼 **Loja** | "Professional storefront, modern, clean, inviting, commercial street" |

**IMPORTANTE:** FLUX não renderiza texto bem — sempre gerar SEM texto e sobrepor com HTML+CSS depois.

[[Ferramentas/Replicate|→ Ver doc completo da Replicate]]

## 2️⃣ HTML+CSS — Fallback
Criar design via código HTML e screenshot do navegador.

```javascript
// Viewport: 1080x1080px
// Criar em about:blank via Playwright
// Screenshot fullPage
// Upload para Instagram
```

**Vantagens:** Sem depender de API, texto perfeito, qualquer layout.
**Desvantagens:** Design mais simples (sem foto realista).

## 3️⃣ CapCut — Alternativa
Editor online de design (capcut.com — sem Cloudflare).
- **Login:** danilotecteatro@yahoo.com.br
- **Ferramentas:** Design Studio, Seedream 5.0, templates
- **Limitação:** UI complexa com modais

## Bloqueados (não usar)
| Serviço | Motivo |
|---------|--------|
| Canva | 🔒 Cloudflare |
| ChatGPT/DALL-E | 🔒 Cloudflare |
| FAL AI | 💳 Sem créditos na conta |
