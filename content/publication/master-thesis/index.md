---
title: "Co-simulation of Cyber-Physical Systems Using DEVS and Functional Mockup Units"
authors:
- xuanli
date: "2021-11-16T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
# publishDate: "2017-01-01T00:00:00Z"

# Publication type.
# https://docs.citationstyles.org/en/stable/specification.html#appendix-iii-types
publication_types: ["thesis"]

# Publication name and optional abbreviated publication name.
publication: "*Arizona State University KEEP*"
publication_short: "*ASU KEEP*"

abstract: Cyber-Physical Systems (CPS) are becoming increasingly prevalent around the world. Co-simulation of cyber and physical components has shown to be an effective way towards the development of time-sensitive and reliable CPS. Correctly combining continuous models with discrete models for co-simulation can often be challenging. In this thesis, the Functional Markup Interface (FMI) is used to develop an adapter called DEVS-FMI for the DEVS-Suite simulator. The adapter, implemented using JavaFMI 2.0, allows any Functional Mock-Up Unit (FMU) to be co-simulated with a Discrete Event System Specification (DEVS) model. This approach enables taking advantage of the parallel DEVS formalism to model cyber systems and using Modelica to model physical systems. An FMU serves as a slave simulator while the DEVS-Suite serves as a master simulator. The Four-Variable model is used as a guide to define the requirements for the inputs and outputs of actuator and sensor devices used in cyber and physical systems. The input and output data as non-functional abstractions of the sensor and actuator devices. Select cyber and physical parts of an electric scooter are chosen, modeled, simulated, and evaluated using the integrated OpenModelica and the DEVS-Suite simulators. Closely related research is briefly examined and expanding this work with support for implicit state-changes for continuous models and distributed co-simulation is noted.

# Summary. An optional shortened abstract.
summary: This master's thesis proposes an approach to co-simulation of DEVS and FMUs for Cyber-Physical systems.

tags:
- co-simulation
- cyber-physical systems
- DEVS
- functional mock-up units
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: 'https://keep.lib.asu.edu/items/161251'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
# image:
#   caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/jdD8gXaTZsc)'
#   focal_point: ""
#   preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ''
---