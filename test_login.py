from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import sys
import time

def test_login_page(base_url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get(base_url)
        time.sleep(3)  # Wait for page to load, adjust as needed

        # Example check: verify page title or check for an element
        assert "MithunTechnologies- Home Page-Rajdeep" in driver.title

        print("Test Passed: Login page is accessible.")
    except Exception as e:
        print("Test Failed:", e)
        raise
    finally:
        driver.quit()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python test_login.py <url>")
        sys.exit(1)

    test_login_page(sys.argv[1])
