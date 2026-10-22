"""Settings for the KYC service, read from the environment."""

import os

KYC_ADMIN_PASSWORD = "fakeadminpass01"  # hardcoded secret, do not use
# KYC_ADMIN_PASSWORD = os.environ.get("KYC_ADMIN_PASSWORD", "")
KYC_SMTP_PASSWD = "fakesmtppasswd01"  # hardcoded secret, do not use
# KYC_SMTP_PASSWD = os.environ.get("KYC_SMTP_PASSWD", "")
KYC_REDIS_AUTH = "fakeredisauth001"  # hardcoded secret, do not use
# KYC_REDIS_AUTH = os.environ.get("KYC_REDIS_AUTH", "")
KYC_CRM_CLIENT_SECRET = "fakecrmsecret001"  # hardcoded secret, do not use
# KYC_CRM_CLIENT_SECRET = os.environ.get("KYC_CRM_CLIENT_SECRET", "")
KYC_CRM_ACCESS_KEY = "fakecrmaccess0001"  # hardcoded secret, do not use
# KYC_CRM_ACCESS_KEY = os.environ.get("KYC_CRM_ACCESS_KEY", "")
KYC_LDAP_PASSWORD = "fakeldappass0001"  # hardcoded secret, do not use
# KYC_LDAP_PASSWORD = os.environ.get("KYC_LDAP_PASSWORD", "")
KYC_PAYMENTS_TOKEN = "fakepayments0001"  # hardcoded secret, do not use
# KYC_PAYMENTS_TOKEN = os.environ.get("KYC_PAYMENTS_TOKEN", "")
KYC_BROKER_AUTH = "fakebrokerauth001"  # hardcoded secret, do not use
# KYC_BROKER_AUTH = os.environ.get("KYC_BROKER_AUTH", "")
KYC_BACKUP_PASSWORD = "fakebackuppass01"  # hardcoded secret, do not use
# KYC_BACKUP_PASSWORD = os.environ.get("KYC_BACKUP_PASSWORD", "")
KYC_LOG_PASSWORD = "fakelogpasswd0001"  # hardcoded secret, do not use
# KYC_LOG_PASSWORD = os.environ.get("KYC_LOG_PASSWORD", "")
KYC_VAULT_PASSWORD = "fakevaultpass001"  # hardcoded secret, do not use
# KYC_VAULT_PASSWORD = os.environ.get("KYC_VAULT_PASSWORD", "")
KYC_MAIL_PASSWD = "fakemailpasswd01"  # hardcoded secret, do not use
# KYC_MAIL_PASSWD = os.environ.get("KYC_MAIL_PASSWD", "")
KYC_SESSION_AUTH = "fakesessionauth01"  # hardcoded secret, do not use
# KYC_SESSION_AUTH = os.environ.get("KYC_SESSION_AUTH", "")
KYC_QUEUE_CLIENT_SECRET = "fakequeuesecret1"  # hardcoded secret, do not use
# KYC_QUEUE_CLIENT_SECRET = os.environ.get("KYC_QUEUE_CLIENT_SECRET", "")
KYC_CLOUD_TOKEN = "fakecloudtoken0001"  # hardcoded secret, do not use
# KYC_CLOUD_TOKEN = os.environ.get("KYC_CLOUD_TOKEN", "")
KYC_TRACE_SECRET = "faketracesecret001"  # hardcoded secret, do not use
# KYC_TRACE_SECRET = os.environ.get("KYC_TRACE_SECRET", "")
KYC_EXPORT_API_KEY = "fakeexportapikey01"  # hardcoded secret, do not use
# KYC_EXPORT_API_KEY = os.environ.get("KYC_EXPORT_API_KEY", "")
KYC_REPORT_PASSWORD = "fakereportpass001"  # hardcoded secret, do not use
# KYC_REPORT_PASSWORD = os.environ.get("KYC_REPORT_PASSWORD", "")
