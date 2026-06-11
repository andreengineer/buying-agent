# Research Questions — Isaura Valuation Engine

> Research questions for Perplexity Pro Deep Research.
> Context is in `context.md`. README.md has full instructions.

---

## 1. Existing Concierge Valuation Methodologies
How do existing luxury concierges (Quintessentially, Velocity Black, Ten Lifestyle Group, Bon Vivant, John Paul) evaluate products and vendors for UHNW clients? What criteria do they use? Do they have formal scoring systems or is it purely human judgment? What signals do they look for in product reviews, expert opinions, and market data? Find any available documentation, case studies, or interviews that reveal their methodology.

### 2. Wine Market Intelligence (Brazil + Global)
For the concrete MVP use case (Brazilian wine market):
- What are the pricing tiers for premium wine in Brazil? (entry, mid, high, ultra-premium)
- Which critics and ratings systems matter most? (Wine Spectator, Robert Parker, Decanter, local Brazilian critics?)
- What variables determine wine price-to-value: vintage, region, producer reputation, critic scores, scarcity, aging potential, bottle condition, provenance?
- How do Brazilian UHNW wine buyers differ from European or US buyers?
- What are the most common fraud/overpricing signals in premium wine?
- How do secondary market prices (Wine Searcher, Liv-ex) compare to retail prices in Brazil?
- What textual signals in reviews correlate with actual quality vs marketing hype?

### 3. AI/ML Approaches to Product Valuation
What existing AI/ML approaches can evaluate product quality from unstructured text (reviews, expert articles, forum discussions)? Specifically:
- Review authenticity detection (fake vs genuine reviews)
- Sentiment analysis with price sensitivity (is the reviewer price-sensitive or quality-focused?)
- Expert consensus aggregation (weighing multiple critic opinions)
- Brand equity scoring (quantifying brand cachet from text)
- Comparative value analysis (product A at $X vs product B at $Y — which is better value?)
- Any existing research or startups in "worth it" analysis? (Consumer Reports AI? Which? magazine? Wirecutter?)
- Academic papers on textual quality assessment or experience good valuation

### 4. UHNW Buyer Psychology in Purchasing Decisions
What research exists on how UHNW individuals evaluate high-ticket purchases? Specifically:
- What drives purchase decisions beyond price? (status, exclusivity, trust in source, expert validation, social proof among peers)
- How do they discover new products? (word of mouth, sommeliers, brand relationships, private buying offices)
- What would make a UHNW person trust an AI's valuation judgment?
- What are the pain points in their current purchasing process that a concierge solves?
- How do they signal quality to each other? (what matters in social proof among UHNW?)

### 5. Data Sources for "Vale Esse Preço?" Analysis
Identify, for each luxury category, the best data sources:
- **Wine:** Vivino, Wine Searcher, Wine Spectator, Decanter, Robert Parker, local Brazilian importers (Decanter Brazil, Mistral, Expand), auction results (Sotheby's, Christie's wine sales)
- **Watches (future):** Chrono24, Hodinkee, Watchuseek forum, Reddit r/watches, auction results
- **Jewelry/gems (future):** GIA reports, auction results, brand pricing
- **Art (future):** Artsy, MutualArt, Artnet, auction indexes (Artprice, Mei Moses)
- **General luxury:** PurseForum, TheFashionLaw, luxury brand annual reports

For each source: is it freely accessible? Does it have an API? What data structure does it provide? What are the reliability/authority levels?

### 6. Competitive Landscape
What products or services currently exist that attempt AI-powered product valuation or luxury purchasing intelligence?
- AI sommeliers (Vivino AI, Wine AI, etc.) — how do they work? Are they price-comparison or value-assessment?
- AI personal shoppers (Threads Stitch, DressX, etc.)
- Luxury pricing intelligence (Bain Luxury Study, Deloitte luxury reports — any API or accessible data?)
- Any startup doing exactly what Isaura proposes? (price-to-value concierge for UHNW)
- What's the closest competitor and how are they positioned?

### 7. Practical Implementation Considerations
- What data points are needed for a minimum viable valuation engine?
- What evaluation framework would work without needing a vector database or complex ML infrastructure?
- How to handle subjectivity: one buyer's "worth it" is another's "overpriced"
- How to express confidence levels in valuation judgments
- How to learn from user feedback over time (did the user buy? were they happy?)
- What are the legal/compliance considerations for giving purchase advice to UHNW clients?

---

## Output Format Requirements

Return the research as structured markdown with:

1. **Executive Summary** (top 5 actionable insights, max 300 words)
2. **Detailed Findings** (by research question #1-#7, each with concrete data, numbers, sources cited)
3. **Contradictions & Uncertainties** (where sources disagree — flag these clearly)
4. **Data Source Inventory** (table: source, category, accessibility, reliability score 1-5)
5. **Competitive Matrix** (table: competitor, offering, price, coverage, gap vs Isaura)
6. **Implementation Recommendations** (what to build first, what to defer)

**For every factual claim, provide the source URL.** If you synthesize, say so explicitly. No made-up data. If a question has no good answer, say "insufficient data found."

---

## Depth Requirements

- Search in English and Portuguese (for Brazilian market specifics)
- Look for academic papers, industry reports, news articles, forum discussions, and company websites
- Prioritize sources from 2024-2026
- For Brazilian wine market specifically, search Portuguese-language sources (blogs, importers, sommelier interviews, Anuário Brasileiro de Vinhos)
- For competitive landscape, check Crunchbase, PitchBook, TechCrunch, and niche startup databases

---

**Start research now. Return comprehensive findings.**
