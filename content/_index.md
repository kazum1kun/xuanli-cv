---
title: ''
summary: 'Xuanli Lin: network optimization, network security, artificial intelligence, and the Internet of Things.'
date: 2022-10-24
type: landing
sections:
  - block: resume-biography
    id: about
    content:
      username: xuanli
    design:
      avatar:
        size: small
        shape: circle
      biography:
        style: 'text-align: center;'
      spacing:
        padding: ['80px', '24px', '80px', '24px']
  - block: collection
    id: publications
    content:
      title: Recent Publications
      text: 'You can also filter and search [all my publications](/publication/).'
      count: 5
      filters:
        folders: [publication]
      archive:
        enable: true
        text: See all publications
    design:
      view: citation
      css_class: xlin-collection
  - block: collection
    id: talks
    content:
      title: Recent & Upcoming Talks
      count: 0
      sort_by: event_start
      filters:
        folders: [event]
    design:
      view: talk-summary
      css_class: xlin-collection
  - block: markdown
    id: education
    design:
      css_class: xlin-markdown
    content:
      title: Education
      text: |
        - PhD in Computer Science at Arizona State University, Tempe. 2021 - present
        - MS in Computer Science at Arizona State University, Tempe. 2019 - 2021
        - BS in Computer Science at Arizona State University, Tempe. 2015 - 2018
  - block: markdown
    id: teaching
    design:
      css_class: xlin-markdown
    content:
      title: TAship
      text: |
        - Fall 2022 - Spring 2024, CSE 310 Data Structures and Algorithms
        - Spring 2019, Spring 2020, CSE 460 Software Analysis and Design
  - block: markdown
    id: contact
    design:
      css_class: xlin-markdown
    content:
      title: Contact
      text: |
        - [kazumi@asu.edu](mailto:kazumi@asu.edu)
        - BYENG 492, 699 S Mill Ave, Tempe, AZ 85281
---
