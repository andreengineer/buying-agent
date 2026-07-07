# Sugestão do Opus 4.8 — Stack de Search para Hermes

Você não disse quanto volume precisa — sem isso, "clever low cost" é chute.
Deixa eu buscar preços atuais antes de recomendar.

Weighed budget constraints against search API alternatives
Weighed budget constraints against search API alternatives

Você está comparando o produto errado. Tavily custa caro porque agrupa search + extração de conteúdo numa chamada só. A pergunta real: você precisa de conteúdo extraído (RAG) ou só de URLs + snippets? Se for só snippets, você está pagando 8x a mais por algo que o Serper faz por centavos.

Deixa eu confirmar preços de Serper e Brave antes de fechar.

Identified self-hosting as optimal cost-free alternative to paid APIs
Identified self-hosting as optimal cost-free alternative to paid APIs

Você não me disse o volume, mas pelo seu estágio (Gama = só você; Alfa = punhado de EAs) você faz talvez centenas de buscas/mês, não milhares. Nesse regime, pagar qualquer API é premature optimization. Você está fazendo vendor-shopping para um problema que seu próprio hardware resolve de graça.

E o erro de base: você está comparando produtos que fazem coisas diferentes. Tavily/Sonar são caros porque agrupam search + extração de conteúdo. Serper/Brave só fazem search (URLs+snippets). Misturar os dois na comparação de preço é o que faz Sonar parecer "caro".

---

## Preços reais (verificado hoje)

| Opção | Custo | O que entrega | Nota |
|-------|-------|--------------|------|
| SearXNG (self-host) | $0 | Search (meta: Google/Bing/DDG) | Roda no seu i7-2600 idle |
| Serper | $0.001/query ($50/50K) | Search only | Mais barato pago |
| Brave | $0.005/query | Search only | Matou free tier em fev/26 |
| Tavily basic | $0.008/credit | Search + extração | Você já conhece |
| Sonar | ~$134/mo moderado | Search + LLM answer | Overkill p/ você |

---

## Resposta clever pro SEU stack

**SearXNG self-hosted + Jina Reader (r.jina.ai) para extração. Custo total: $0.**

**Search:** você já roda Xubuntu + n8n + Docker. SearXNG é um container. Agrega múltiplos engines, sem API key, sem ban se rate-limitar sensato (a 100 buscas/dia isso não é problema).

**Extração:** https://r.jina.ai/<url> retorna markdown limpo da página, free tier generoso. Pluga direto no n8n.

**Por que isso bate Serper/Tavily pra você agora:** gasto marginal zero, zero lock-in (seu princípio de portabilidade), e você controla o índice. O trade-off é que você mantém um container a mais — mas você já mantém 6 serviços, +1 é ruído.

**Quando trocar por API paga:** quando volume passar de ~1-2K buscas/mês OU quando latência do SearXNG virar gargalo no fluxo client-facing (Beta). Aí Serper a $0.001 é o default óbvio, não Tavily.

---

## Uma pergunta que expõe o gap

Você **precisa de conteúdo extraído mesmo?** Se o Hermes só precisa de URLs+snippets para diligência de fornecedor (Reclame Aqui, Google, social), search puro basta e você nem toca em extração — Serper resolve por centavos e você pula a complexidade do SearXNG. Se precisa ler a página inteira, aí sim o par search+extração importa.

**Qual dos dois é o teu caso?**