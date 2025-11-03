#!/usr/bin/env python3
"""
Launch Jupyter Notebook in Browser with Playwright for Better Visualization and Debugging

This is a meta-document/debugging tool that launches notebooks in a browser
with full automation hooks, making visualizations and debugging much better
than the IDE's notebook viewer.

Usage:
    python launch_notebook_debug.py notebook.ipynb
    python launch_notebook_debug.py  # Launches all .ipynb files in current directory
"""

import sys
import subprocess
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

def find_jupyter_server(ports=[8888, 8889, 8890, 8887]):
    """Check if Jupyter server is already running"""
    try:
        import requests
        for port in ports:
            try:
                response = requests.get(f'http://localhost:{port}', timeout=2)
                if response.status_code == 200:
                    return f"http://localhost:{port}"
            except:
                pass
    except ImportError:
        pass
    return None

def start_jupyter_server(port=8888):
    """Start Jupyter notebook server"""
    import sys
    from pathlib import Path
    
    print("🚀 Starting Jupyter server...")
    print(f"   Port: {port}")
    
    jupyter_cmd = [sys.executable, '-m', 'jupyter', 'notebook', '--no-browser', f'--port={port}']
    
    process = subprocess.Popen(
        jupyter_cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    # Wait for server to start
    print("   Waiting for server to start...")
    for i in range(20):
        time.sleep(1)
        try:
            import requests
            response = requests.get(f'http://localhost:{port}', timeout=1)
            if response.status_code == 200:
                print(f"✓ Server started on http://localhost:{port}")
                return f"http://localhost:{port}", process
        except:
            if i % 3 == 0:
                print(f"   Still waiting... ({i+1}/20)")
    
    # Assume it started even if we can't verify
    return f"http://localhost:{port}", process

def launch_notebook_in_browser(notebook_path, jupyter_url=None):
    """Launch a notebook in browser using Playwright"""
    notebook_file = Path(notebook_path)
    
    if not notebook_file.exists():
        print(f"✗ Notebook not found: {notebook_file}")
        return False
    
    notebook_name = notebook_file.name
    print("="*60)
    print(f"LAUNCHING NOTEBOOK: {notebook_name}")
    print("="*60)
    
    # Get or start Jupyter server
    if not jupyter_url:
        jupyter_url = find_jupyter_server()
    
    if not jupyter_url:
        jupyter_url, server_process = start_jupyter_server()
        time.sleep(2)  # Give it a moment
    else:
        print(f"✓ Using existing Jupyter server: {jupyter_url}")
        server_process = None
    
    notebook_url = f"{jupyter_url}/notebooks/{notebook_name}"
    
    print(f"\n🌐 Opening notebook with Playwright browser automation...")
    print(f"   URL: {notebook_url}\n")
    
    try:
        with sync_playwright() as p:
            # Launch browser (visible, full automation)
            print("🚀 Launching Chromium browser...")
            browser = p.chromium.launch(
                headless=False,
                args=['--start-maximized']
            )
            
            # Create context with large viewport for better visualization
            context = browser.new_context(
                viewport={'width': 1920, 'height': 1080}
            )
            page = context.new_page()
            
            # Navigate to notebook
            print("📓 Loading notebook...")
            page.goto(notebook_url, wait_until='networkidle', timeout=30000)
            
            print("✓ Notebook opened in browser with full automation hooks!")
            print("\n✅ Browser window is now open - you can:")
            print("   - View all visualizations clearly")
            print("   - Step through cells interactively")
            print("   - Debug and interact with the notebook")
            print("   - Use Playwright hooks for automation")
            print(f"\n📝 Server: {jupyter_url}")
            print(f"🌐 Notebook: {notebook_url}")
            print("\n💡 Browser will stay open - interact with it freely")
            print("   Close the browser window when you're done")
            
            # Keep browser open - user closes it manually
            # The browser object stays alive until context manager exits
            # We'll wait here so browser stays open
            print("\n⏸️  Browser open - interact now...")
            print("   (Close browser window or press Ctrl+C here to exit)\n")
            
            try:
                # Wait indefinitely until user closes browser or interrupts
                while True:
                    time.sleep(1)
                    # Check if browser is still connected
                    if browser.connected:
                        continue
                    else:
                        break
            except KeyboardInterrupt:
                print("\n\n⚠️  Interrupted - closing browser...")
            
            browser.close()
            print("✓ Browser closed")
            
    except Exception as e:
        print(f"⚠️  Playwright error: {e}")
        print(f"\n💡 Opening with regular browser instead...")
        import webbrowser
        webbrowser.open(notebook_url)
        print(f"✓ Notebook opened in default browser")
        return False
    
    return True

def main():
    """Main entry point"""
    if len(sys.argv) > 1:
        # Launch specific notebook
        notebook_path = sys.argv[1]
        launch_notebook_in_browser(notebook_path)
    else:
        # Find all notebooks in current directory
        notebooks = list(Path('.').glob('*.ipynb'))
        
        if not notebooks:
            print("✗ No notebooks found in current directory")
            print("\nUsage:")
            print("  python launch_notebook_debug.py notebook.ipynb")
            print("  python launch_notebook_debug.py  # Launch all notebooks")
            return
        
        print("="*60)
        print("AVAILABLE NOTEBOOKS")
        print("="*60)
        for i, nb in enumerate(notebooks, 1):
            print(f"{i}. {nb.name}")
        
        if len(notebooks) == 1:
            print(f"\n✓ Launching: {notebooks[0].name}")
            launch_notebook_in_browser(notebooks[0])
        else:
            print(f"\n💡 Found {len(notebooks)} notebook(s)")
            print("   Specify which one to launch:")
            print(f"   python launch_notebook_debug.py <notebook_name>")

if __name__ == '__main__':
    main()

