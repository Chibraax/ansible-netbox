import sys, json, pynetbox

all_tenants: list = ["StudyP", "My Tenant", "salut"]
url, token, name = sys.argv[1], sys.argv[2], sys.argv[3]
nb: pynetbox.api = pynetbox.api(url, token)

for x in all_tenants:
    tenant = nb.tenancy.tenants.get(name=x)
    print(json.dumps({"exists": tenant is not None}))
    print(tenant)
