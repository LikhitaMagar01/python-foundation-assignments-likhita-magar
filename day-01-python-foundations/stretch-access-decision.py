def authorize(role, is_active=True, requested_data=''):
  allowed_roles = ["analyst", "scientist", "engineer"]
  restricted_jobs = ["salary_data", "personal_data"]

  if role.lower() == 'super_admin':
    print("Access granted")
    return

  if not is_active:
    print("Access denied because the user is inactive.")
    return

  if not (role.lower() in allowed_roles):
    print("Access denied because the role is not allowed.")
    return

  if not (requested_data.lower() in restricted_jobs):
    print("Access denied because the dataset is restricted.")
    return

  print("Access granted")


authorize('analyst', False, 'salary_data')
authorize('designer', True, 'salary_data')
authorize('analyst', True, 'profile')
authorize('super_admin', True, 'salary_data')

