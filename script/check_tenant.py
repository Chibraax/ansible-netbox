import sys
import json
import pynetbox


url, token = sys.argv[1], sys.argv[2]
nb: pynetbox.api = pynetbox.api(url, token)

tenants = nb.tenancy.tenants.all()
tenant_names = [t.name for t in tenants]


# Return all tenants in netbox
print(json.dumps(tenant_names))
