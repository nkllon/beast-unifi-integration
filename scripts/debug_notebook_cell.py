# Launch this notebook in browser for better visualization & debugging
# This is the "meta-document" debugging tool

from playwright.sync_api import sync_playwright
import subprocess
import time
import sys
from pathlib import Path

def launch_notebook_for_debugging(notebook_name=None):
    """Launch current notebook in browser with Playwright for debugging"""
    if notebook_name is None:
        # Try to get current notebook name from IPython
        try:
            from IPython import get_ipython
            ipython = get_ipython()
            if ipython and hasattr(ipython, 'kernel'):
                # We're in Jupyter
                notebook_name = "unifi_data_analysis.ipynb"  # Default
        except:
            notebook_name = "unifi_data_analysis.ipynb"
    
    notebook_file = Path(notebook_name)
    print("="*60)
    print(f"LAUNCHING NOTEBOOK IN BROWSER FOR DEBUGGING")
    print("="*60)
    print(f"Notebook: {notebook_file.name}")
    
    # Check for Jupyter server
    jupyter_url = None
    try:
        import requests
        for port in [8888, 8889, 8890]:
            try:
                response = requests.get(f'http://localhost:{port}', timeout=2)
                if response.status_code == 200:
                    jupyter_url = f"http://localhost:{port}"
                    break
            except:
                pass
    except:
        pass
    
    if not jupyter_url:
        print("🚀 Starting Jupyter server...")
        jupyter_cmd = [sys.executable, '-m', 'jupyter', 'notebook', '--no-browser', '--port=8888']
        subprocess.Popen(jupyter_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        for i in range(15):
            time.sleep(1)
            try:
                import requests
                response = requests.get('http://localhost:8888', timeout=1)
                if response.status_code == 200:
                    jupyter_url = "http://localhost:8888"
                    break
            except:
                pass
        if not jupyter_url:
            jupyter_url = "http://localhost:8888"
            time.sleep(2)
    
    notebook_url = f"{jupyter_url}/notebooks/{notebook_file.name}"
    
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False, args=['--start-maximized'])
            context = browser.new_context(viewport={'width': 1920, 'height': 1080})
            page = context.new_page()
            page.goto(notebook_url, wait_until='networkidle', timeout=30000)
            print("✓ Notebook opened in browser!")
            print("💡 Browser window open - interact with it")
            print("   Close browser window when done")
            while browser.connected:
                time.sleep(1)
            if browser.connected:
                browser.close()
    except Exception as e:
        print(f"Error: {e}")
        import webbrowser
        webbrowser.open(notebook_url)

# Run it
launch_notebook_for_debugging("unifi_data_analysis.ipynb")
