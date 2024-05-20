import re
import time
from playwright.sync_api import Playwright, sync_playwright

def test_get_top_gainer(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True)
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
            page.goto(f"https://tw.stock.yahoo.com/quote/{code}.TW/revenue")
            page.get_by_role("link", name="財務").click()
            income =  page.locator("xpath=/html/body/div[1]/div/div/div/div/div[4]/div/div[1]/div/div[4]/div/section[2]/div/div[2]/div/div/ul/li[3]/div/div[2]/ul/li[1]/span").inner_text()
            result.append(f"{code},{number},{name},{value},{link},{income}")
            page.goto("https://www.wantgoo.com/stock/ranking/top-gainer")
            time.sleep(5)

    # Output the results as CSV format
    for line in result:
        print(line)

with sync_playwright() as playwright:
    test_get_top_gainer(playwright)
