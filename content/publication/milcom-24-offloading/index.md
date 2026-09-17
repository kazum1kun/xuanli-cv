---
title: Joint Optimization of Task Offloading and Resource Allocation in Tactical Edge Networks
authors:
- zhaofeng-zhang
- xuanli
- guoliang-xue
- yanchao-zhang
- kevin-s-chan
date: '2024-10-28'
publishDate: '2024-05-09'
publication_types:
- paper-conference
publication:
  name: MILCOM 2024 - 2024 IEEE Military Communications Conference (MILCOM)
  short_name: MILCOM
  pages: '703-708'
  publisher: IEEE
summary: This paper jointly chooses task offloading and resource allocation in tactical edge networks to maximize completion rewards under computing and communication constraints. An exact search algorithm uses problem-specific pruning, while a simulated-annealing heuristic offers an efficient alternative. Numerical evaluations compare optimal solutions with the heuristic’s competitive performance.
tags:
- edge network
- task offloading
- joint optimization
featured: false
projects: []
slides: ''
hugoblox:
  ids:
    doi: 10.1109/MILCOM61039.2024.10773851
links:
- url: https://ieeexplore.ieee.org/document/10773851/
  type: custom
  label: IEEE Xplore
---

## Abstract

Recent years have witnessed explosive growth in deploying IoT devices over tactical edge networks. Due to the limited computing resources of local edge devices, there is an urgent need to offload the computing tasks to edge servers. A central question here is "How can we design offloading strategies and resource allocation plans so that all the computing resource constraints of servers and communication constraints between devices and servers are satisfied?" In this paper, we formulate the problem of jointly optimizing task offloading and resource allocation (JOA) in tactical edge networks as maximizing the total task completion rewards subject to various resource constraints. We design two algorithms to solve the JOA problem. The first is an exact algorithm using a search tree, where the branch-cutting criterion is well-crafted based on the property of the JOA problem. The second is a meta-heuristic algorithm based on the simulated annealing approach. We conduct numerical evaluations and demonstrate that the proposed exact algorithm can obtain the optimal task offloading strategy and resource allocation plan. The heuristic algorithm can efficiently provide competitive performance.
