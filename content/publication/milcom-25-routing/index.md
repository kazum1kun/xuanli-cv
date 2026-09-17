---
title: Dynamic Flow Routing and Scheduling for Time-Critical Network Services
authors:
- xuanli
- zhaofeng-zhang
- zunzheng-zhang
- guoliang-xue
date: '2025-10-06'
publication_types:
- paper-conference
publication:
  name: MILCOM 2025 - 2025 IEEE Military Communications Conference (MILCOM)
  short_name: IEEE MILCOM
  publisher: IEEE
  pages: 624-629
summary: This paper jointly routes and schedules time-critical network services to maximize completion rewards while meeting delivery deadlines. It models the network over time and develops a sequential-rounding heuristic guided by linear programming. A static-flow formulation accelerates feasibility checks, and simulations evaluate the resulting trade-offs in performance.
tags:
- network optimization
- flow routing
- scheduling
featured: false
hugoblox:
  ids:
    doi: 10.1109/MILCOM64451.2025.11310531
    dblp: conf/milcom/LinZZX25
links:
- type: custom
  label: IEEE Xplore
  url: https://ieeexplore.ieee.org/document/11310531/
---

## Abstract

A key challenge in next-generation networks is providing intelligent network services to support time-sensitive applications such as AR/VR and the Internet of Military Things (IoMT). This work aims to answer the question: "How can we design a network service scheduling and flow routing scheme to satisfy the stringent demand and deadline requirements of tactical network applications?" We take a time-expanded graph-based approach to this study. Specifically, given a time-expanded graph constructed from an original network graph, we propose an optimization problem to find a subset of network services to maximize their total completion rewards such that the data of all services in this subset can be transmitted to their destination nodes by their deadlines. Unfortunately, solving this problem directly is challenging since it is a mixed-integer program. We propose a heuristic algorithm based on a sequential rounding approach where a linear programming (LP) feasibility problem is iteratively solved to update the network service subset, guided by a relaxed reward maximization problem that prioritizes high-reward requests. To further improve efficiency, we fine-tune the above LP feasibility problem from a static flow perspective, enabling fast feasibility checks on the original graph, and design the corresponding efficient heuristic algorithm. The simulation results demonstrate the trade-off among different approaches and validate the effectiveness of the proposed algorithms.
