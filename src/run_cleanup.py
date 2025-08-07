#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import yaml
import logging
from datetime import datetime
from src.ad_monitor import ADMonitor
from src.m365_monitor import M365Monitor
from src.utils import send_email, generate_report

def main():
    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('logs/cleanup.log'),
            logging.StreamHandler()
        ]
    )
    
    # Load configuration
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    
    logging.info("Starting account inactivity monitor...")
    
    # Initialize monitors
    ad_monitor = ADMonitor(config)
    m365_monitor = M365Monitor(config)
    
    # Get inactive accounts
    inactive_ad_users = []
    inactive_m365_users = []
    
    if ad_monitor.connect():
        inactive_ad_users = ad_monitor.get_inactive_users()
        logging.info(f"Found {len(inactive_ad_users)} inactive AD users")
    
    if m365_monitor.authenticate():
        inactive_m365_users = m365_monitor.get_user_activity()
        logging.info(f"Found {len(inactive_m365_users)} inactive M365 users")
    
    # Generate report
    report = generate_report(inactive_ad_users, inactive_m365_users)
    
    # Send email notification
    if inactive_ad_users or inactive_m365_users:
        send_email(config, "Inactive Account Report", report)
    
    logging.info("Account inactivity monitor completed")

if __name__ == "__main__":
    main()
