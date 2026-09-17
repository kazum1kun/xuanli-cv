---
title: 'AEGIS: Throughput-Guaranteed Resilient Routing via a Conditional Value-at-Risk Approach'
authors:
- zhaofeng-zhang
- xuanli
- guoliang-xue
- kevin-s-chan
date: '2026-04-16'
publication_types:
- article-journal
publication:
  name: IEEE Transactions on Networking
  short_name: IEEE Transactions on Networking
  publisher: IEEE
  volume: '34'
  pages: 4929-4943
summary: AEGIS guarantees required throughput during normal operation while reducing the risk of throughput loss under network failures, without precomputing routing paths. It reformulates conditional value-at-risk optimization as a linear program and uses bisection to obtain acyclic routing with more efficient resource use. Numerical evaluations compare the resulting routing trade-offs.
tags:
- resilient routing
- network optimization
- conditional value-at-risk
featured: false
hugoblox:
  ids:
    doi: 10.1109/TON.2026.3684425
    dblp: journals/ton/ZhangLXC26
links:
- type: custom
  label: IEEE Xplore
  url: https://ieeexplore.ieee.org/document/11482216/
---

## Abstract

The past decade has witnessed significant progress in next-generation wireless networks. Resilient routing is essential for maintaining reliability in mission-critical network services, particularly in dynamic and adversarial environments. Traditional traffic engineering (TE) approaches rely on pre-computed paths. Still, they face performance limitations when the number of pre-computed paths is small and scalability challenges when the number is large. This study seeks to answer the fundamental question: “How can we achieve throughput-guaranteed resilient routing under network failures without pre-computing routing paths?” We propose AEGIS, a novel throughput-guaranteed resilient routing scheme leveraging a conditional value-at-risk (CVaR) approach, which proactively guarantees the required throughput under normal conditions and enables recovery during network failures. Specifically, we propose an optimization problem that minimizes the CVaR of total throughput loss across all the failure situations while respecting user budget and network constraints. The above optimization problem is non-differentiable and non-linear; we then reformulate it as an equivalent linear program (LP) and develop an optimal solution. However, the above solution will induce cyclic flows due to resource reservation behaviors. To achieve a more resource-efficient routing, we propose a bisection approach to obtain a CVaR upper bound so that the corresponding routing is acyclic. Extensive numerical evaluations demonstrate the trade-offs among various approaches and highlight the advantages of AEGIS.
