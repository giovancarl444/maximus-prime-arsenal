#!/usr/bin/env python3
"""
Maximus Prime Arsenal - Unified Launcher
Launches all Maximus Prime stack components in correct order.
"""
import subprocess
import time
import sys
from pathlib import Path

COMPONENTS = [
    {
        "name": "OpenBB API",
        "cmd": ["python3", "/Users/midas/Code/openbb-env/bin/openbb-api"],
        "check_port": 6900,
        "required": True
    },
    {
        "name": "Killshot Dashboard",
        "cmd": ["python3", "/Users/midas/Code/killshot/scripts/dashboard_pure.py"],
        "check_port": 7777,
        "required": True
    },
    {
        "name": "OpenBB Daemon",
        "cmd": ["python3", "/Users/midas/Code/killshot/scripts/openbb_daemon.py"],
        "check_port": None,
        "required": True
    },
    {
        "name": "Scanner Loop",
        "cmd": ["python3", "/Users/midas/Code/killshot/scripts/scanner_loop.py"],
        "check_port": None,
        "required": True
    },
    {
        "name": "Monitor Services",
        "cmd": ["python3", "/Users/midas/Code/killshot/scripts/monitor_services.py"],
        "check_port": None,
        "required": False
    }
]

def check_port(port, timeout=5):
    """Check if port is listening."""
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        result = sock.connect_ex(('localhost', port))
        sock.close()
        return result == 0
    except:
        sock.close()
        return False

def launch_component(comp):
    """Launch a component and verify it started."""
    print(f"[ARSENAL] Launching {comp['name']}...")
    
    try:
        proc = subprocess.Popen(
            comp['cmd'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            start_new_session=True
        )
        
        # Wait for port if specified
        if comp['check_port']:
            for i in range(10):
                if check_port(comp['check_port']):
                    print(f"[ARSENAL] {comp['name']} UP on port {comp['check_port']}")
                    return True
                time.sleep(1)
            
            if comp['required']:
                print(f"[ARSENAL] ERROR: {comp['name']} failed to start on port {comp['check_port']}")
                return False
        else:
            time.sleep(2)
            if proc.poll() is None:
                print(f"[ARSENAL] {comp['name']} running (PID: {proc.pid})")
                return True
            else:
                print(f"[ARSENAL] ERROR: {comp['name']} exited immediately")
                return False
                
    except Exception as e:
        print(f"[ARSENAL] ERROR launching {comp['name']}: {e}")
        return False

def main():
    """Main entry point."""
    print("[ARSENAL] Maximus Prime Arsenal - Unified Launcher")
    print("[ARSENAL] Starting all components...")
    print()
    
    failed = []
    for comp in COMPONENTS:
        success = launch_component(comp)
        if not success and comp['required']:
            failed.append(comp['name'])
        time.sleep(1)
    
    print()
    if failed:
        print(f"[ARSENAL] FAILED components: {', '.join(failed)}")
        sys.exit(1)
    else:
        print("[ARSENAL] All components launched successfully!")
        print("[ARSENAL] Maximus Prime is OPERATIONAL.")
        sys.exit(0)

if __name__ == "__main__":
    main()
