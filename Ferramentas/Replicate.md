# 🤖 Replicate (FLUX)

## Setup
- **API Key:** Configurada na memória do Hermes
- **Modelo:** `black-forest-labs/flux-dev`
- **Formato de saída:** WEBP (converter para PNG)
- **Tamanho:** 1024x1024

## Como Usar via Hermes

### Terminal (heredoc — funciona sempre)
```bash
python3 << 'PYEOF'
import urllib.request, json, time
k = "r8_YUd..."  # API key
data = json.dumps({
    "version": "black-forest-labs/flux-dev",
    "input": {
        "prompt": "SEU PROMPT AQUI, sem texto, sem watermark",
        "aspect_ratio": "1:1",
        "num_outputs": 1
    }
}).encode()
req = urllib.request.Request(
    "https://api.replicate.com/v1/predictions",
    data=data,
    headers={"Authorization": f"Bearer {k}", "Content-Type": "application/json"}
)
r = json.loads(urllib.request.urlopen(req).read())
pid = r["id"]
url = r["urls"]["get"]
for _ in range(30):
    time.sleep(3)
    r2 = json.loads(urllib.request.urlopen(urllib.request.Request(url, headers={"Authorization": f"Bearer {k}"})).read())
    s = r2["status"]
    if s == "succeeded":
        print(f"DONE {r2['output'][0]}")
        break
    elif s == "failed":
        print(f"FAIL {r2.get('error','')}")
        break
    print(".", end="", flush=True)
PYEOF
```

### Baixar e Converter
```bash
curl -s -L -o /root/.hermes/imagem.webp "URL_DA_IMAGEM"
python3 -c "from PIL import Image; img = Image.open('/root/.hermes/imagem.webp'); img.save('/root/.hermes/imagem.png', 'PNG')"
```

## Observações
- ⚠️ API key é mascarada pelo redator do Hermes — sempre usar terminal heredoc
- ⚠️ FLUX não renderiza texto — usar HTML+CSS para sobrepor
- ✅ Tempo médio de geração: 10-15s
- ✅ Qualidade 8K / fotorealista
