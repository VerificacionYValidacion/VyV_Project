from django.contrib.auth.models import User
user = User.objects.create_user('Bryan', 'bryan@epn.edu.ec', 'bryan123')

# At this point, user is a User object that has already been saved
# to the database. You can continue to change its attributes
# if you want to change other fields.
user.last_name = 'Lennon'
user.save()