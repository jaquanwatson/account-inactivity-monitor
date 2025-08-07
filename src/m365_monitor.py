import msal
import requests
from datetime import datetime, timedelta
import logging
from typing import List, Dict

class M365Monitor:
    def __init__(self, config: dict):
        self.config = config
        self.tenant_id = config['m365_settings']['tenant_id']
        self.client_id = config['m365_settings']['client_id']
        self.client_secret = config['m365_settings']['client_secret']
        self.token = None
        
    def authenticate(self):
        """Authenticate with Microsoft Graph API"""
        try:
            app = msal.ConfidentialClientApplication(
                self.client_id,
                authority=f"https://login.microsoftonline.com/{self.tenant_id}",
                client_credential=self.client_secret
            )
            
            result = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
            
            if "access_token" in result:
                self.token = result["access_token"]
                return True
            else:
                logging.error(f"Authentication failed: {result.get('error_description')}")
                return False
                
        except Exception as e:
            logging.error(f"Authentication error: {e}")
            return False
    
    def get_user_activity(self) -> List[Dict]:
        """Get user activity from Microsoft Graph"""
        if not self.token:
            return []
            
        headers = {'Authorization': f'Bearer {self.token}'}
        inactive_users = []
        
        try:
            # Get user sign-in activity
            url = "https://graph.microsoft.com/v1.0/users"
            params = {
                '$select': 'userPrincipalName,displayName,signInActivity',
                '$top': 999
            }
            
            response = requests.get(url, headers=headers, params=params)
            
            if response.status_code == 200:
                users = response.json().get('value', [])
                threshold_date = datetime.now() - timedelta(days=self.config['thresholds']['inactive_days'])
                
                for user in users:
                    sign_in_activity = user.get('signInActivity', {})
                    last_sign_in = sign_in_activity.get('lastSignInDateTime')
                    
                    if last_sign_in:
                        last_sign_in_date = datetime.fromisoformat(last_sign_in.replace('Z', '+00:00'))
                        if last_sign_in_date < threshold_date:
                            inactive_users.append({
                                'userPrincipalName': user.get('userPrincipalName'),
                                'displayName': user.get('displayName'),
                                'lastSignIn': last_sign_in_date,
                                'daysInactive': (datetime.now() - last_sign_in_date.replace(tzinfo=None)).days
                            })
                            
        except Exception as e:
            logging.error(f"Error getting user activity: {e}")
            
        return inactive_users
