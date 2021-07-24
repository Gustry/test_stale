---
name: Custom issue template
about: Describe this issue template's purpose here.
title: ''
labels: ''
assignees: ''

---

- type: markdown
    attributes:
      value: |
        Thanks for taking the time to fill out this bug report correctly.

  - type: textarea
    id: what
    attributes:
      label: What is the bug or the crash?
    validations:
      required: true

  - type: textarea
    id: steps
    attributes:
      label: Steps to reproduce the issue
      placeholder: |
        Steps, sample datasets and qgis project file to reproduce the behavior. Screencasts or screenshots welcome.
        1. Go to '...'
        2. Click on '...'
        3. Scroll down to '...'
        4. See error
    validations:
      required: true

  - type: input
    id: about-info
    attributes:
      label: Versions
      description: |
        In the QGIS Help menu -> About, click in the table, Ctrl+A and then Ctrl+C. Finally paste here.
        Do not make a screenshot.
    validations:
      required: true

  - type: textarea
    id: additional-context
    attributes:
      label: Additional context
      description: |
        Add any other context about the problem here.
