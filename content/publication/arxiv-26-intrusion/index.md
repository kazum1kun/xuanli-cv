---
title: 'Resource-Aware Intrusion Detection in Infrastructure Networks: A Game-Theoretic Approach'
authors:
- xuanli
- zhaofeng-zhang
- zunzheng-zhang
- kevin-s-chan
- guoliang-xue
date: '2026-08-07'
publication_types:
- article
publication:
  name: arXiv preprint arXiv:2608.06655
  short_name: arXiv:2608.06655
summary: A graph security game models how a defender should allocate limited sensing and processing resources against an attacker choosing routes to valuable targets. The report analyzes Nash and Stackelberg equilibria under different attacker observations and develops algorithms for defense configurations and mixed strategies when exhaustive strategy enumeration is impractical.
tags:
- intrusion detection
- game theory
- network security
featured: false
hugoblox:
  ids:
    doi: 10.48550/arXiv.2608.06655
    arxiv: '2608.06655'
---

## Abstract

Infrastructure networks increasingly rely on distributed sensing to detect intrusions before attackers reach valuable assets. Yet sensing devices, communication resources, and edge server capacity are limited, while intelligent attackers can adapt their routes to the deployed defense. Motivated by integrated sensing and communication (ISAC), we study how sensing and processing resources should be allocated under strategic interaction between a defender and an attacker. We formulate their interaction as a graph security game in which the defender deploys sensing actions under resource and false alarm constraints, while the attacker selects routes to valuable targets. We consider simultaneous play and settings in which the attacker observes either a pure defender configuration or a mixed defender strategy. Our analysis characterizes the existence, structure, and computational complexity of the Nash and Stackelberg equilibria, showing how the attacker's observation of the defense affects equilibrium behavior and when optimal strategies become difficult to compute. We develop algorithms that construct effective pure configurations and refine restricted games for mixed Nash and mixed Stackelberg play. On enumerable instances, their solutions have small mean normalized differences from fully enumerated references; the methods also apply when exhaustive strategy enumeration is impractical. We also identify conditions under which Nash and mixed Stackelberg payoffs are ordered or coincide.


Preprint, first submitted 2026-08-07.
