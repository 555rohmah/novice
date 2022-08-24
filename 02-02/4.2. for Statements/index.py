1# words = ["anggur", "apel", "jeruk"]
# for i in words:
#     print(i)


users = {'ayam': 'active', 'kambing': 'inactive', 'kerbau': 'active'}
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

active_user = {}
for user, status in users.items():
    if status == 'active':
        active_user[user] = status

print(users)
print(active_user)

a = {}
a["c"] = "d"
a["e"] = "f"
print(a)


