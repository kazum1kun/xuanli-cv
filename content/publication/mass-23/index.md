---
title: Exploring Machine Learning Algorithms for User Activity Inference from IoT Network Traffic
authors:
- kuai-xu
- yinxin-wan
- xuanli
- feng-wang
- guoliang-xue
date: '2023-09-26'
publishDate: '2023-09-26T00:00:00Z'
publication_types:
- paper-conference
publication:
  name: 2023 IEEE 20th International Conference on Mobile Ad Hoc and Smart Systems (MASS)
  short_name: IEEE MASS
  pages: '366-374'
  publisher: IEEE
summary: This study infers smart-home user activities directly from overlapping IoT network traffic patterns. Wavelet analysis separates activity-related signals from background traffic, and supervised learning classifies activities using the extracted features. Experiments with labeled activities and traffic collected in real homes demonstrate accurate activity inference.
tags:
- Internet of Things
- machine learning
- activity inference
featured: false
projects: []
slides: ''
hugoblox:
  ids:
    doi: 10.1109/MASS58611.2023.00052
links:
- url: https://ieeexplore.ieee.org/document/10298385/
  type: custom
  label: IEEE Xplore
---

## Abstract

The availability of ubiquitous and heterogeneous Internet-of-Things (IoT) devices in smart homes and their interactions with users provide a unique opportunity to monitor, understand, recognize, learn, and infer user activities for safety monitoring, connected health, energy saving as well as other disruptive services. Our analysis on IoT network traffic from smart homes with a variety of IoT devices has discovered that user activities often trigger overlapping traffic waves from multiple IoT devices that are deployed near the activities. This insight leads us to adopt wavelet analysis to decompose IoT network traffic in smart homes into low, middle, and high frequency bands that distinguish IoT traffic waves triggered by user activities from background noises such as heartbeat signals between IoT devices and cloud servers. Subsequently, we extract a broad range of traffic features from these IoT traffic waves and explore supervised machine learning (ML) algorithms to classify various user activities with these features. Based on the labelled user activities and IoT network traffic data collected from real smart home environments, our experiments have demonstrated that the ML-based algorithms are able to use IoT network traffic to accurately infer various user activities in smart homes.


*Best Paper Award Recipient*
