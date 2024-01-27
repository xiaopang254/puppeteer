import asyncio
import random
from pyppeteer import launch
from pyppeteer_stealth import stealth

async def open_website_in_instance(url, instance_number):
    # Launch browser with visible UI and common screen size
    max_heap_size = 8192
    browser = await launch(headless=False, args=['--window-size=1920,1080', f'--max-old-space-size={max_heap_size}'])
    page = await browser.newPage()

    # Reset cookies for each instance
    await page.setCookie()

    # Set a random user-agent
    user_agents = ['Gq6NgQsVNw', '8hL1H42kH1', 'xLMH62fwqR', '3QvsdTWOBx', '9uzNKTxAN9']
    user_agent = random.choice(user_agents)
    await page.setUserAgent(user_agent)

    # Set viewport to a common screen size
    await page.setViewport({'width': 1920, 'height': 1080})

    # Apply stealth to hide webdriver flag and add common browser features
    await stealth(page)

    # Navigate to the URL with random intervals between requests
    await asyncio.sleep(random.uniform(1, 5))  # Random sleep between 1 and 5 seconds
    await page.goto(url)

    # Perform realistic mouse movement and clicks
    await page.mouse.move(random.randint(0, 1920), random.randint(0, 1080))
    await page.mouse.click(random.randint(0, 1920), random.randint(0, 1080))

    # Keep the browser open
    return browser

async def main():
    url = 'https://www.google.com'  # Replace with your desired URL
    number_of_instances = 5  # Specify the number of instances

    # Create multiple instances
    browsers = await asyncio.gather(*(open_website_in_instance(url, i + 1) for i in range(number_of_instances)))

    # Keep the script running
    await asyncio.Future()

asyncio.run(main())
