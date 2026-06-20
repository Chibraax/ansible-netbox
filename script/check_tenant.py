import sys, json, pynetbox

all_tenants: list = ["StudyP", "My Tenant", "salut"]

url, token = sys.argv[1], sys.argv[2]
nb: pynetbox.api = pynetbox.api(url, token)

tenants = nb.tenancy.tenants.all()
tenant_names = [t.name for t in tenants]
print(json.dumps(tenant_names))
