import os
from dotenv import load_dotenv

load_dotenv()

auth = {
  'account_sid': os.getenv('ACCOUNT_SID'),
  'auth_token': os.getenv('AUTH_TOKEN')
}