# Account Inactivity Monitor

[![PowerShell](https://img.shields.io/badge/PowerShell-5.1%2B-blue)](https://github.com/PowerShell/PowerShell)
[![Microsoft Graph](https://img.shields.io/badge/Microsoft%20Graph-API-green)](https://docs.microsoft.com/en-us/graph/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

> Automated detection and cleanup of inactive Active Directory and Microsoft 365 user accounts to improve security posture and reduce licensing costs.

## Features

- **Automated Detection**: Identifies inactive accounts across AD and M365
- **Security Compliance**: Helps maintain security posture by removing stale accounts
- **Cost Optimization**: Reduces licensing costs by identifying unused accounts
- **Detailed Reporting**: Generates comprehensive reports with actionable insights
- **Configurable Thresholds**: Customizable inactivity periods and criteria
- **Safe Operations**: Includes dry-run mode and approval workflows

## Prerequisites

- PowerShell 5.1 or later
- Microsoft Graph PowerShell SDK
- Azure AD PowerShell Module
- Appropriate permissions:
  - `User.Read.All`
  - `AuditLog.Read.All`
  - `Directory.Read.All`

## Quick Start

1. **Clone the repository**
   ```powershell
   git clone https://github.com/jaquanwatson/account-inactivity-monitor.git
   cd account-inactivity-monitor
   
2. **Install dependencies**
Install-Module Microsoft.Graph -Force
Install-Module AzureAD -Force

3. **Configure settings**
Copy-Item config.example.json config.json
Edit config.json with your settings

4.**Run the monitor**
.\Start-InactivityMonitor.ps1 -DryRun

## How It Works

mermaid

graph TD
    A[Start Monitor] --> B[Connect to Graph API]
    B --> C[Query User Accounts]
    C --> D[Check Last Sign-in]
    D --> E{Inactive > Threshold?}
    E -->|Yes| F[Add to Report]
    E -->|No| G[Continue]
    F --> H[Generate Report]
    G --> H
    H --> I[Send Notifications]
    I --> J[Cleanup if Enabled]

## Configuration
Create a config.json file:

json

{
  "InactivityThresholdDays": 90,
  "ReportPath": "./reports/",
  "EmailNotifications": true,
  "AutoCleanup": false,
  "ExcludedGroups": ["Executives", "Service Accounts"],
  "NotificationEmail": "admin@company.com"
}
#Sample Output
code

Account Inactivity Report - 2025-01-08
==========================================
Total Accounts Scanned: 1,247
Inactive Accounts Found: 23
Potential Monthly Savings: $345

Inactive Accounts:
- john.doe@company.com (Last login: 2024-09-15)
- jane.smith@company.com (Last login: 2024-08-22)
- old.account@company.com (Last login: 2024-07-10)

## Security Considerations
Uses least-privilege access principles
Supports dry-run mode for testing
Logs all actions for audit purposes
Requires explicit approval for account modifications
Excludes critical service accounts automatically

## Contributing
Fork the repository
Create a feature branch (git checkout -b feature/improvement)
Commit your changes (git commit -am 'Add new feature')
Push to the branch (git push origin feature/improvement)
Create a Pull Request
## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
Jaquan Watson

GitHub: @jaquanwatson
LinkedIn: jaquanwatson
Email: jqwatson96@gmail.com
⭐ If this project helped you, please give it a star!