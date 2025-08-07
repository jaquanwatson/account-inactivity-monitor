import pyad
from datetime import datetime, timedelta
import logging
from typing import List, Dict

class ADMonitor:
    def __init__(self, config: dict):
        self.config = config
        self.domain = config['ad_settings']['domain']
        self.server = config['ad_settings']['server']
        
    def connect(self):
        """Establish connection to Active Directory"""
        try:
            pyad.set_defaults(ldap_server=self.server)
            return True
        except Exception as e:
            logging.error(f"Failed to connect to AD: {e}")
            return False
    
    def get_inactive_users(self) -> List[Dict]:
        """Get list of inactive users based on last logon"""
        inactive_users = []
        threshold_date = datetime.now() - timedelta(days=self.config['thresholds']['inactive_days'])
        
        try:
            # Query all users
            users = pyad.adquery.ADQuery()
            users.execute_query(
                attributes=["sAMAccountName", "displayName", "lastLogon", "userAccountControl"],
                where_clause="objectCategory='person' AND objectClass='user'"
            )
            
            for user in users.get_results():
                last_logon = user.get('lastLogon')
                if last_logon and last_logon < threshold_date:
                    inactive_users.append({
                        'username': user.get('sAMAccountName'),
                        'display_name': user.get('displayName'),
                        'last_logon': last_logon,
                        'days_inactive': (datetime.now() - last_logon).days,
                        'enabled': not bool(user.get('userAccountControl', 0) & 2)
                    })
                    
        except Exception as e:
            logging.error(f"Error querying AD users: {e}")
            
        return inactive_users
    
    def disable_user(self, username: str) -> bool:
        """Disable a user account"""
        try:
            user = pyad.aduser.ADUser.from_cn(username)
            user.disable()
            logging.info(f"Disabled user: {username}")
            return True
        except Exception as e:
            logging.error(f"Failed to disable user {username}: {e}")
            return False
