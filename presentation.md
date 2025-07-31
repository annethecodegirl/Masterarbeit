---
marp: true
theme: default
paginate: true
title: "Modeling Household Carbon Footprints: Methods, Metrics, and Estimation Frameworks"
description: "Thesis Defense by Anushka Mukherjee"
---

<!-- Slide 1 -->
# Modeling Household Carbon Footprints: Methods, Metrics, and Estimation Frameworks  
### Master’s Thesis  
Anushka Mukherjee  · 50075072
University of Bonn 
July 2025

 ---

<!-- Slide 2 -->
## Motivation
Why is it important to assess household carbon footprints accurately?

- Households are responsible for ~17% of global CO₂ emissions.
- Traditional calculators overlook investment and systemic effects.
- Need for models that avoid double-counting and reflect market feedback.

---

<!-- Slide: Research Questions -->
## Research Questions

1.  **How do footprint estimates vary across methods when applied to real household data?**  
   – What insights emerge about the robustness, fairness, and policy relevance of each approach?

2. **How does each carbon accounting method estimate and attribute responsibility for household carbon footprints?**  
   – Focus on system boundaries, attribution logic, treatment of investment and spillovers.

3. **How do these attribution methods influence policy, and what are the equity implications of their application?**  
   – Who bears responsibility, and what forms of action are prioritized?

---

## Methods Compared

| Model | Type | Scope | Investment? | Double-Counting? | Market Response? |
|-------|------|-------|-------------|------------------|------------------|
| GHG Protocol | Accounting | 1–3 | ✗ | ✓ | ✗ |
| LCA | Accounting | Lifecycle | ✗ | ✓ | ✗ |
| EEIOA | Top-down | Economy-wide | ✓ | ✓ | ✗ |
| HS Model | Microeconomic equilibrium | Economy-wide | ✓ | ✗ | ✓ |

---

## The Hakenes–Schliephake (HS) Model

- Closed economy with (N) industries.
- Households choose both consumption $(q_h)$ and investment $(i_h)$.
- Carbon footprint:
$$
fp_h = x \cdot (\phi q_h + (1 - \phi) \cdot i_h / c)
$$

---

## Industry-Specific Weights

- $(\phi = \frac{b}{b + c^2 \alpha \sigma^2})$
- Reflects:
  - Price elasticity of demand
  - Risk aversion $(\alpha)$
  - Variance of returns $(\sigma^2)$

---

## Empirical Illustration – Spain 2022

- Household expenditure data (COICOP categories)
- Emission factors from DEFRA & IPCC
- Scope 1–3 emissions + EEIOA + HS

---

## Results Overview (Chart)

<!-- Insert image or code to generate chart using Marp plugin, or link to SVG -->
- Scope 3: Highest estimate  
- LCA: Lower but comprehensive  
- EEIO: Adds investment  
- HS: Balanced + causal

---

## Comparing Models

**GHG Protocol:**
- Broad but static
- Double counts investment

**LCA:**
- Lifecycle detail
- Omits market response

---

**EEIOA:**
- System-wide
- No causality

**HS Model:**
- Dynamic, spillover-aware
- Avoids double-counting

---

## Spillover Effects

\[
fp_h = \sum_j x_j \left[ \phi_j q_{hj} + (1 - \phi_j) \frac{i_{hj}}{c_j} \right] + \sum_{k \neq j} \psi_{jk}(q_{hk} - \frac{i_{hk}}{c_k})
\]

- Cross-industry interactions
- Investment in one sector shifts prices in another

---

## Who is Responsible?

- HS model shows responsibility is **distributed**.
- Individual restraint ≠ total reduction (others respond).
- Market dynamics matter for effective mitigation.

---

## Policy Implications

- Behavior change is not enough.
- Need upstream reforms (e.g., green finance, producer regulation).
- Reassess household “blame” narratives.

---

## Limitations

- Static framework (1-period)
- Abstract parameters (σ², α)
- Empirical challenges in elasticity calibration

---

## Future Work

- Dynamic HS extension
- Multiregional EEIO integration
- Microdata for household heterogeneity

---

## Key Takeaways

- Household carbon footprint = not just what you buy.
- HS model links economic behavior to climate impact.
- Responsibility ≠ blame — it's about systemic leverage.

---

## Thank You 🙏  
**Questions?**

Anushka Mukherjee  
anushkamukherji.wordpress.com  
