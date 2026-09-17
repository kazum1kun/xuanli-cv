---
title: Most Vulnerable Attack Trace in a Probabilistic Attack Graph
authors:
- xuanli
- zhaofeng-zhang
- yinxin-wan
- Ethan Teo
- guoliang-xue
- yanchao-zhang
date: '2024-10-28'
publishDate: '2024-05-09'
publication_types:
- paper-conference
publication:
  name: MILCOM 2024 - 2024 IEEE Military Communications Conference (MILCOM)
  short_name: MILCOM
  pages: '1070-1075'
  publisher: IEEE
summary: This paper identifies attack traces with the highest cumulative success probability in probabilistic attack graphs, including graphs with cycles. It develops an exact search algorithm and a polynomial-time heuristic, then evaluates both on an extensive dataset to support analysis of exploitable network vulnerabilities.
tags:
- attack graph
- probabilistic attack graph
- attack trace
featured: false
projects: []
slides: ''
hugoblox:
  ids:
    doi: 10.1109/MILCOM61039.2024.10773995
links:
- url: https://ieeexplore.ieee.org/document/10773995/
  type: custom
  label: IEEE Xplore
---

## Abstract

In this paper, we investigate the properties and computation of attack traces on probabilistic attack graphs, a model that integrates probability into traditional attack graphs to reflect the varying exploitability of network vulnerabilities. We introduce the Most Vulnerable Attack Trace (MVAT) problem, which aims to identify the attack trace with the highest cumulative success probability for an attacker. To address this problem, we propose both an exact algorithm and a heuristic algorithm, each designed to navigate the complexities introduced by cycles in the attack graph. Our exact algorithm explores all possible sequences of node selections to ensure the optimal attack trace, while our heuristic algorithm efficiently approximates the MVAT in polynomial time. We evaluate the performance of our algorithms using an extensive dataset, demonstrating the usefulness of the proposed algorithms.
