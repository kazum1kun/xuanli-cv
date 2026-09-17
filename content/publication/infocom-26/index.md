---
title: Task Offloading across Unreliable Edge Networks via Distributional Dynamic Programming
authors:
- xuanli
- zhaofeng-zhang
- zunzheng-zhang
- guoliang-xue
date: '2026-05-18'
publication_types:
- paper-conference
publication:
  name: IEEE INFOCOM 2026 - IEEE Conference on Computer Communications
  short_name: IEEE INFOCOM
  publisher: IEEE
  pages: 1-6
summary: A risk-averse task offloading framework balances expected task rewards against severe losses caused by unreliable wireless links. It combines a conditional value-at-risk constraint with distributional dynamic programming, using stochastic-dominance pruning and scaling approximations to improve efficiency. Evaluations examine the resulting risk-reward trade-offs in resource-constrained edge networks.
tags:
- edge computing
- task offloading
- risk-aware optimization
featured: false
hugoblox:
  ids:
    doi: 10.1109/INFOCOM59046.2026.11571468
    dblp: conf/infocom/LinZZX26
links:
- type: custom
  label: IEEE Xplore
  url: https://ieeexplore.ieee.org/document/11571468/
---

## Abstract

As Internet of Things (IoT) networks evolve toward integrated sensing and communications (ISAC), ensuring reliable resource management at the mobile edge has become increasingly complex. The combination of limited communication and computing resources with unreliable wireless links necessitates highly robust offloading strategies. Traditional approaches that merely maximize expected network utility often fail to account for the stochastic link failures in dynamic sensing systems, resulting in severe utility degradation. To address this, we propose a risk-averse task offloading framework that systematically manages uncertainties in sensing-enabled mobile edge computing. We formulate a joint optimization problem that maximizes expected total task reward, subject to a conditional value-at-risk (CVaR) constraint, effectively mitigating the tail risk of communication task failures. We solve the resulting optimization problem via a novel distributional dynamic programming (DDP) approach. To improve computational efficiency, we integrate Pareto Frontier pruning based on first-order stochastic dominance (FSD) alongside scaling and rounding approximations. Evaluation results confirm that our framework successfully navigates the risk-reward trade-offs in resource-constrained deployments.
