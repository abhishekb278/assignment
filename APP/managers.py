from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _



class UserManager(BaseUserManager):
    """
    Custom user model manager where username is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, username, password,**extra_fields):
        """
        Create and save a User with the given username and password.
        """
        if not username:
            raise ValueError(_('The username must be set'))
        
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password,**extra_fields):
        """
        Create and save a SuperUser with the given username and password.
        """
        if password is None:
            raise TypeError('password is must')
        if username is None:
            raise TypeError('username is must')
        '''if username is None:
            username='None'
            print('HERE')'''
        
        user = self.create_user(username,password)
        user.is_superuser=True
        user.is_staff=True
        user.save()
        return user
