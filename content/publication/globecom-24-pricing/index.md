---
title: Max-min Hub Pricing in Payment Channel Networks
authors:
- guoliang-xue
- alena-chang
- xuanli
- Ruozhou Yu
- Dejun Yang
date: '2024-12-08'
publishDate: '2024-05-09'
publication_types:
- paper-conference
publication:
  name: GLOBECOM 2024 - 2024 IEEE Global Communications Conference
  short_name: GLOBECOM
  pages: '535-540'
  publisher: IEEE
summary: This paper studies how competing payment-channel hubs set transaction fees. It proves that approximate best responses can always be computed efficiently, while approximate Nash equilibria may not exist. A max-min pricing strategy uses conservative revenue estimates to guide hub decisions, with numerical evaluations demonstrating its effectiveness.
tags:
- blockchain security
- hub pricing
- payment channel network
featured: false
projects: []
slides: ''
hugoblox:
  ids:
    doi: 10.1109/GLOBECOM52923.2024.10901005
links:
- url: https://ieeexplore.ieee.org/document/10901005/
  type: custom
  label: IEEE Xplore
---

## Abstract

Payment Channel Networks (PCNs) offer an efficient off-chain alternative to the blockchain for transactions. Router nodes in PCNs facilitate transactions between non-adjacent nodes in exchange for a fee. PCN topology tends to be centralized, with a select number of routers known as hubs dominating all payment services. The fee-setting choices of hubs in order to maximize their revenue present fertile grounds for the study of PCN communications and economics. In this paper, we conduct a comprehensive analysis of the Hub Price-Setting (HPS) game. In particular, we define approximate Best Response strategies (ϵ-BR) as well as approximate Nash equilibria (ϵ-NE). We prove that for any ϵ > 0, an ϵ-BR always exists, and can be computed in polynomial time. We also prove that for some ϵ > 0, an ϵ-NE may not exist. We furthermore introduce the notion of conservative estimate and present a max-min approach to the HPS game. Extensive evaluation results demonstrate the power of our proposed approach.
