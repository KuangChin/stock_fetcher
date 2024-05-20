# Project Installation Guide

The following steps will help you set up and run the project:

## Initial Setup

First, you need to install PDM, which is a modern Python package manager. You can install PDM using the following command:

```bash
git clone https://github.com/KuangChin/stock_fetcher.git
pip install pdm
cd src/stock_fetcher
pdm add playwright
pdm run playwright install
pdm run pick.py
```
