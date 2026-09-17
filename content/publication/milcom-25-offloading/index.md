---
title: Multi-Hop Relay-Aided Task Offloading for Tactical Edge Computing
authors:
- zhaofeng-zhang
- xuanli
- guoliang-xue
- yanchao-zhang
- kevin-s-chan
date: '2025-10-06'
publication_types:
- paper-conference
publication:
  name: MILCOM 2025 - 2025 IEEE Military Communications Conference (MILCOM)
  short_name: IEEE MILCOM
  publisher: IEEE
  pages: 1572-1577
summary: This paper allows tactical edge tasks to run locally, at intermediate relays, or at edge servers. It jointly optimizes offloading, computing resources, and TDMA scheduling using a graph of feasible links and an exact dynamic-programming algorithm. Scaling and rounding heuristics improve scalability while retaining competitive performance.
tags:
- edge computing
- task offloading
- dynamic programming
featured: false
hugoblox:
  ids:
    doi: 10.1109/MILCOM64451.2025.11310052
    dblp: conf/milcom/ZhangLXZC25
links:
- type: custom
  label: IEEE Xplore
  url: https://ieeexplore.ieee.org/document/11310052/
---

## Abstract

Recent years have witnessed explosive growth in the deployment of IoT devices over tactical edge networks, which demand flexible task offloading strategies to accommodate limited connectivity and computing resources. While many existing works assume direct access to edge servers, such assumptions often break down in adversarial and dynamic environments. This work introduces a novel edge task offloading framework that enables multi-hop communication and enables task execution not only at edge servers but also at relay nodes and local devices. We formulate the problem of joint task offloading, resource allocation, and time frame/slot assignment, under a time-division multiple access (TDMA) uplink scheme, as a nonlinear integer program to maximize total rewards, subject to various communication and resource constraints. To solve it optimally, we first construct a feasibility-aware directed graph that captures valid communication links based on signal-to-noise ratio (SNR) constraints, and then design a dynamic programming (DP) algorithm that integrates slot-minimizing offloading path selection with the assignment of the largest feasible number of time frames for each user to reduce total time slots consumption without violating task completion deadlines. To improve scalability, efficient heuristics are developed using scaling and rounding techniques. Extensive experiments demonstrate that our proposed DP algorithm achieves optimal task offloading and resource allocation, while our heuristic algorithms offer a computationally efficient alternative with competitive performance.
