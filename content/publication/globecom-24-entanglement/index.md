---
title: Entanglement Distribution in LEO Satellite-based Dynamic Quantum Networks
authors:
- alena-chang
- yinxin-wan
- xuanli
- guoliang-xue
- Arunabha Sen
date: '2024-12-08'
publishDate: '2024-05-09'
publication_types:
- paper-conference
publication:
  name: GLOBECOM 2024 - 2024 IEEE Global Communications Conference
  short_name: GLOBECOM
  pages: '4485-4490'
  publisher: IEEE
summary: This paper models entanglement distribution through moving LEO satellites while accounting for Earth rotation, inter-satellite links, and multiple orbital shells. It transforms the dynamic network into a smaller static logical graph and develops two greedy routing algorithms, evaluated against an integer-programming benchmark.
tags:
- satellite communication
- quantum entanglement
- quantum networks
featured: false
projects: []
slides: ''
hugoblox:
  ids:
    doi: 10.1109/GLOBECOM52923.2024.10901769
links:
- url: https://ieeexplore.ieee.org/document/10901769/
  type: custom
  label: IEEE Xplore
---

## Abstract

Recent advances in space quantum communications envision Low Earth Orbit (LEO) satellites for global entanglement distribution. Entanglement distribution in such a network requires considerations such as satellite mobility, ground station mobility due to the Earth’s rotation, inter-satellite links, and multiple orbital shells, all of which have not been thoroughly studied in the networking literature. We ameliorate this deficit by defining a system model which accounts for all of the aforementioned factors. Using this system model, we formulate the dynamic optimal entanglement distribution (DOED) problem. We convert the DOED problem in a dynamic physical network to an instance of the problem in a static logical graph, the latter of which can be used to solve the former. We obtain a reduced logical graph from a logical graph, which can be used to reduce the complexity of solving the DOED problem. We propose two polynomial-time greedy algorithms for computing entanglement paths, as well as an integer linear programming (ILP)-based algorithm as a benchmark. We present evaluation results to demonstrate the advantages of our model and algorithms.
