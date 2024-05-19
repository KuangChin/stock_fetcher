import re
import time
from playwright.sync_api import Playwright, sync_playwright

def test_get_top_gainer(playwright: Playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.wantgoo.com/stock/ranking/top-gainer")
    time.sleep(5)
    result = []
    for i in range(1, 100):
        code = page.locator(f'xpath=/html/body/div[1]/main/div/div/div[2]/table/tbody/tr[{i}]/td[2]').inner_text()
        name = page.locator(f'xpath=/html/body/div[1]/main/div/div/div[2]/table/tbody/tr[{i}]/td[3]').inner_text()
        number = re.findall(r'\d+\.\d+|\d+', page.locator(f'xpath=/html/body/div[1]/main/div/div/div[2]/table/tbody/tr[{i}]/td[7]').inner_text())[0]
        value = re.findall(r'\d+\.\d+|\d+', page.locator(f'xpath=/html/body/div[1]/main/div/div/div[2]/table/tbody/tr[{i}]/td[12]').inner_text())[0]
        link = f'https://www.wantgoo.com/stock/{code}/news'
        if float(number) >= 15 and float(value) >= 10:
            result.append(f"{code},{number},{name},{value},{link}")
    
    # Output the results as CSV format
    for line in result:
        print(line)

with sync_playwright() as playwright:
    test_get_top_gainer(playwright)
