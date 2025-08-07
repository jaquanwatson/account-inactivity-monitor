# Account Inactivity Monitor

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Automate the detection and cleanup of inactive Active Directory and Microsoft 365 user accounts to improve security posture and reduce licensing costs.

## Features

- **Multi-Platform Monitoring**: Track user activity across both Active Directory and Microsoft 365
- **Configurable Thresholds**: Set custom inactivity periods for different user groups
- **Automated Reporting**: Generate detailed reports of inactive accounts with export capabilities
- **Safe Cleanup Process**: Built-in approval workflows and backup mechanisms before account modifications
- **Email Notifications**: Automated alerts to administrators with actionable insights
- **Audit Trail**: Comprehensive logging of all actions for compliance requirements
- **Flexible Scheduling**: Run on-demand or schedule automated checks

## Prerequisites

- Python 3.8 or higher
- Active Directory domain access with appropriate service account
- Microsoft 365 tenant with admin permissions
- SMTP server access for email notifications

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/account-inactivity-monitor.git
   cd account-inactivity-monitor
