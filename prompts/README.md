# prompts/
>
> Estrutura otimizada por LLM. Cada subdiretório = 1 estágio da pipeline.
> README.md = entry point que diz ao LLM o que fazer e quais arquivos ler.
> Marcela: recebe URL do README.md (ou arquivo concatenado) — copia tudo, cola.

## Estrutura

```
prompts/
  README.md                          ← este índice
  perplexity/                        ← Estágio ①: Hermes → Perplexity Pro
    README.md                        ← "You are Perplexity Pro. Your goal is deep research."
    context.md                       ← contexto do projeto Isaura
    research_questions.md            ← 7 eixos de pesquisa
  gpt55/                             ← Estágio ③: Hermes → GPT 5.5 ext thinking (A GERAR)
    README.md                        ← "You are GPT 5.5 with extended thinking."
    context.md                       ← Output do Perplexity processado por Hermes
    data.json                        ← Dados estruturados da pipeline Isaura
    instructions.md                  ← Como gerar o prompt do Fable 5
  fable5/                            ← Estágio ④: GPT 5.5 → Fable 5 (A GERAR)
    README.md                        ← "You are Fable 5. Design the valuation engine."
    context.md                       ← Contexto completo dos estágios anteriores
    instructions.md                  ← Output esperado
  reference/                         ← Documentos de referência
    scrapling-analysis.md            ← Análise do Scrapling
    fable5-sprint-metrics.md         ← Métricas do primeiro run Fable 5
  mobile-pack/                       ← Para Marcela: arquivos concatenados prontos pra copiar-colar
    (gerado automaticamente por Hermes)
```

## Regras

| Regra | Por quê |
|-------|---------|
| README.md em cada dir = entry point | LLM lê primeiro, sabe o que fazer |
| 1 arquivo = 1 propósito | `data.json` só tem dados, `instructions.md` só tem instruções |
| LLM gasta tokens no objetivo | Não perde tempo entendendo estrutura bagunçada |
| mobile-pack/ gerado sob demanda | Marcela não navega estrutura — só copia 1 arquivo |
| Arquivos nomeados semanticamente | `research_questions.md` > `file2.md` |