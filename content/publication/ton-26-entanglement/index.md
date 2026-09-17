---
title: Computing an Optimal Entanglement Path with Throughput and Fidelity Considerations
authors:
- guoliang-xue
- nageswara-s-v-rao
- Don Towsley
- Gayane Vardoyan
- zunzheng-zhang
- xuanli
- Muneer Alshowkan
- Joseph M. Lukens
- Nicholas A. Peters
- Saikat Guha
date: '2026-08-27'
publication_types:
- article-journal
publication:
  name: IEEE Transactions on Networking
  short_name: IEEE Transactions on Networking (Early Access)
  publisher: IEEE
summary: This paper develops a quantum-network routing algorithm that maximizes entanglement throughput while meeting a fidelity threshold, accounting for node buffers and sequential swapping. It proves the general feasibility problem is NP-hard and uses entanglement probability distributions and path dominance to find optimal routes, with reported subsecond results on networks containing thousands of nodes.
tags:
- quantum networks
- entanglement distribution
- routing
featured: false
hugoblox:
  ids:
    doi: 10.1109/TON.2026.3728139
links:
- type: custom
  label: IEEE Xplore
  url: https://ieeexplore.ieee.org/document/11668978/
---

## Abstract

Entanglement distribution is a core function of quantum networks essential for operations including teleportation, distributed quantum sensing, and multisite computation. Entanglement throughput and fidelity are two critical performance measures that depend on the quantum transmission along the links and swapping operations at the repeaters along the path. We study the problem of computing a end-to-end entanglement path that satisfies both fidelity and throughput requirements, leveraging qubit buffers at the nodes and considering the sequential swapping order. We show that the general problem of simultaneously satisfying both metrics to be NP-hard, and develop an algorithm to maximize throughput subject to a given fidelity threshold. We introduce the concepts of entanglement probability distribution and path domination and exploit them in the design of our algorithm. Extensive numerical results show that our algorithm can find optimal solutions in networks with thousands of nodes in less than a second. We also describe practical and possible implementation aspects of this algorithm in terms of devices and architecture support.


Published online as an Early Access article on August 27, 2026. Final volume and page numbers have not yet been assigned.
