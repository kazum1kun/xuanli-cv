---
title: IoT System Vulnerability Analysis and Network Hardening with Shortest Attack Trace in a Weighted Attack Graph
authors:
- yinxin-wan
- xuanli
- Abdulhakim Sabur
- alena-chang
- kuai-xu
- guoliang-xue
author_notes:
- Equal contribution
- Equal contribution
date: '2023-05-09'
publishDate: '2023-05-09'
publication_types:
- paper-conference
publication:
  name: Proceedings of the 8th ACM/IEEE Conference on Internet of Things Design and Implementation
  short_name: IoTDI
  pages: '315-326'
  publisher: ACM
summary: This paper introduces weighted attack graphs for analyzing IoT vulnerabilities and selecting network protections. It develops a shortest-attack-trace algorithm, proves the network-hardening problem is NP-hard, and provides exact and heuristic solutions. Tests on nine synthetic systems and two smart-home testbeds show fast analysis and near-optimal heuristic hardening.
tags:
- Internet of Things
- IoT security
- attack graph
- attack trace
featured: false
projects: []
slides: ''
awards:
- name: Best Paper Award
  level: winner
hugoblox:
  ids:
    doi: 10.1145/3576842.3582326
links:
- url: https://dl.acm.org/doi/10.1145/3576842.3582326
  type: custom
  label: ACM DL
- type: slides
  url: iotdi-23.pptx
---

## Abstract

In recent years, Internet of Things (IoT) devices have been extensively deployed in edge networks, including smart homes and offices. Despite the exciting opportunities afforded by the advancements in the IoT, it also introduces new attack vectors and vulnerabilities in the system. Existing studies have shown that the attack graph is an effective model for performing system-level analysis of IoT security. In this paper, we study IoT system vulnerability analysis and network hardening. We first extend the concept of attack graph to weighted attack graph and design a novel algorithm for computing a shortest attack trace in a weighted attack graph. We then formulate the network hardening problem. We prove that this problem is NP-hard, and then design an exact algorithm and a heuristic algorithm to solve it. Extensive experiments on 9 synthetic IoT systems and 2 real-world smart home IoT testbeds demonstrate that our shortest attack trace algorithm is robust and fast, and our heuristic network hardening algorithm is efficient in producing near optimal results compared to the exact algorithm.


*Best Paper Award Recipient*
