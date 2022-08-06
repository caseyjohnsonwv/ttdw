# ttdw

TikTok Data Warehousing... which is nearly impossible. They obfuscate every element and class name in their HTML, and they certainly don't have a public API. My hacky half solution is to run two Docker containers: one for Selenium, one for my Python script.

---

## Quickstart

Assuming you already have Docker installed and running locally:
1. Clone this repository
2. `docker-compose up`
