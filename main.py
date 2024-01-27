import asyncio
from pyppeteer import launch

async def open_website_in_instance(url, instance_number, launch_args):
    # Launch Chromium with specified arguments
    browser = await launch(headless=False, args=launch_args)
    page = await browser.newPage()

    # Navigate to the URL
    await page.goto(url)

    # Perform actions unique to this instance
    print(f'Instance {instance_number}: Navigated to {url}')

    # Set a unique cookie for each instance
    await page.setCookie({'name': 'instance', 'value': f'instance-{instance_number}', 'url': url})

    # Log the cookie
    cookies = await page.cookies(url)
    print(f'Instance {instance_number}: Cookies - {cookies}')

    # Keep the browser open

async def main():
    url = 'https://google.com.sg'  # Replace with your desired URL
    number_of_instances = 20  # Specify the number of instances
    memory_limit_mb = 8192  # Set memory limit (e.g., 2048 MB)
    window_width, window_height = 1280, 720  # Set window size (width, height)

    # Combine GPU acceleration arguments, memory limit, and window size
    launch_args = [
        '--enable-gpu-rasterization',
        '--force-gpu-rasterization',
        f'--max-old-space-size={memory_limit_mb}',
        f'--window-size={window_width},{window_height}'
    ]

    # Create multiple instances
    await asyncio.gather(*(open_website_in_instance(url, i + 1, launch_args) for i in range(number_of_instances)))

    # Keep the script running
    await asyncio.Future()

asyncio.run(main())
