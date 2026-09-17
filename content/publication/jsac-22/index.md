---
title: An Effective Machine Learning Based Algorithm for Inferring User Activities From IoT Device Events
authors:
- guoliang-xue
- yinxin-wan
- xuanli
- kuai-xu
- feng-wang
date: '2022-07-20T00:00:00Z'
publication_types:
- article-journal
publication:
  name: IEEE Journal on Selected Areas in Communications
  short_name: IEEE JSAC
  volume: '40'
  issue: '9'
  pages: '2733-2745'
  publisher: IEEE
summary: This study combines deterministic pattern extraction with unsupervised learning to infer smart-home user activities from IoT device events. Experiments with 2,959 real activities and up to 30,000 synthetic activities show that the method tolerates device malfunctions and temporary failures or delays while outperforming the existing comparison method.
tags:
- Internet of Things
- smart homes
- machine learning
- unsupervised learning
- user activity inference
- device events
featured: false
projects: []
slides: ''
hugoblox:
  ids:
    doi: 10.1109/JSAC.2022.3191123
links:
- url: https://ieeexplore.ieee.org/document/9833514/
  type: custom
  label: IEEE Xplore
- type: code
  url: https://github.com/kazum1kun/e2a_python
---

## Abstract

The rapid and ubiquitous deployment of Internet of Things (IoT) in smart homes has created unprecedented opportunities to automatically extract environmental knowledge, awareness, and intelligence. Many existing studies have adopted either machine learning approaches or deterministic approaches to infer IoT device events and/or user activities from network traffic in smart homes. In this paper, we study the problem of inferring user activity patterns from a sequence of device events by first deterministically extracting a small number of representative user activity patterns from the sequence of device events, then applying unsupervised learning to compute an optimal subset of these user activity patterns to infer user activity patterns. Based on extensive experiments with sequences of device events triggered by 2,959 real user activities and up to 30,000 synthetic user activities, we demonstrate that our scheme is resilient to device malfunctions and transient failures/delays, and outperforms the state-of-the-art solution.
