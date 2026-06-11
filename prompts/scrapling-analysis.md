# Scrapling (D4Vinci) — Análise para Isaura Pipeline

> Descoberta via LinkedIn. v0.4.9, 10.6k★, Python 3.10+.
> https://github.com/D4Vinci/Scrapling

---

## O Que Resolve

| Problema Atual | Solução Scrapling | Impacto |
|----------------|-------------------|---------|
| Cloudflare Turnstile bloqueia scraping de lojas | `StealthyFetcher(solve_cloudflare=True)` resolve nativamente sem API keys | Acesso a lojas antes bloqueadas |
| Selectores quebram quando HTML muda | `auto_save=True` + `adaptive=True` auto-reloca elementos | Zero manutenção de selectores |
| Tavily rate-limit (3 imagens/run) | Scrape direto da página do produto com `StealthyFetcher.fetch()` | Dados frescos, sem dependência externa |
| Race condition imageSearchCount (P0) | Spider multi-session com contadores isolados por invocação | Concorrência real, sem bug |
| BeautifulSoup lento (1584ms) | Parser 784x mais rápido (2.02ms) | Pipeline 800x mais rápida |
| Sem MCP tool pro Hermes | MCP server built-in (`scrapling mcp-server --port 8000`) | Scrapling vira ferramenta nativa |

---

## Arquitetura de Integração

```
Usuário pergunta "vale esse preço?"
       │
       ▼
┌──────────────────┐
│  Hermes          │  Orquestrador (DeepSeek v4)
│  (orquestrador)  │  Decide: Tavily vs Scrapling vs ambos
└────────┬─────────┘
         │
    ┌────▼────┐
    │Scrapling│  MCP tool via `scrapling mcp-server`
    │:8000    │  ou script Python direto
    └────┬────┘
         │
    ┌────▼──────────────────────────────┐
    │ StealthyFetcher.fetch(url,        │  Resolve Turnstile automaticamente
    │   solve_cloudflare=True,          │
    │   headless=True)                  │
    └────┬──────────────────────────────┘
         │
    ┌────▼────┐
    │Adaptive │  auto_save=True guarda estrutura atual
    │Parser   │  adaptive=True reencontra se HTML mudar
    └────┬────┘
         │
    ┌────▼────────────────────┐
    │ Dados estruturados:     │  → preço, imagem, descrição, reviews
    │ JSON → Isaura pipeline  │  → valuation engine decide "vale?"
    └─────────────────────────┘
```

---

## Testes Que Agora São Possíveis

### 1. Cloudflare Bypass em Lojas Brasileiras
```python
from scrapling.fetchers import StealthyFetcher
page = StealthyFetcher.fetch(
    'https://www.winelovers.com.br/produto/exemplo',
    solve_cloudflare=True,
    headless=True
)
preco = page.css('.price::text').get()
```
Testa em 5 lojas das 41 KNOWN_STORES que usam Cloudflare.

### 2. Pipeline Autocurativa
```python
# Primeira execução: salva estrutura
page = StealthyFetcher.fetch(url, auto_save=True)
preco = page.css('.price::text').get()

# Segunda execução (após loja mudar HTML): adaptive reencontra
page = StealthyFetcher.fetch(url, adaptive=True)
preco = page.css('.price::text').get()  # ainda funciona
```

### 3. Crawler Concorrente de 41 Lojas
```python
from scrapling.spiders import Spider
class PrecoSpider(Spider):
    name = "precos"
    start_urls = STORE_URLS  # 41 KNOWN_STORES
    concurrent_requests = 10  # sem race condition!
    async def parse(self, response):
        yield {
            "produto": response.css('.product-name::text').get(),
            "preco": response.css('.price::text').get(),
            "loja": response.url
        }
```

### 4. Sem Dependência de Tavily
Antes: `Tavily search → rate-limit (3 imagens) → 403s → fallback frágil`
Depois: `Scrapling.fetch(url) → dados completos → 0 calls externas`

### 5. MCP Tool pro Hermes
```bash
scrapling mcp-server --port 8000
# Hermes configura MCP client → Scrapling vira ferramenta nativa
# Hermes pode: fetch(url), extract(selector), crawl(spider)
```

---

## Roadmap de Adoção

| Fase | Ação | Risco | Valor |
|------|------|-------|-------|
| 1 (hoje) | Instalar `pip install "scrapling[all]"` | Baixo | Infra pronta |
| 2 (próximo sprint) | Testar `solve_cloudflare=True` em 5 lojas | Médio | Prova de conceito |
| 3 | Substituir Tavily image-search por Scrapling direct fetch | Médio | Elimina rate-limit cascade |
| 4 | Implementar adaptive parsing nos selectores existentes | Baixo | Zero manutenção |
| 5 | Migrar spider concorrente pros 41 stores | Alto | Pipeline 10x mais rápida |
| 6 | Expor MCP server como tool do Hermes | Médio | Scrapling vira nativo |

---

## Custo

- **Scrapling**: grátis (open source BSD)
- **Proxy residential** (opcional para anti-bot extra): a partir de $0.49/GB (Evomi) ou $0.018/IP (9Proxy)
- **Sem API keys**: Turnstile solving é feito via automação, não serviço pago
- **vs Tavily básico**: Tavily = $0.50/1000 queries. Scrapling = $0.00

---

*Atualizado: 2026-06-11*