from django.contrib.auth.tokens import PasswordResetTokenGenerator #generates passwords for users in encrypted form
from django.utils import six #It is intended to support codebases 2,3 without modifications

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
  def _make_hash_value(self, user, timestamp):
    return (six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.profile.email_confirmed))

account_activation_token = AccountActivationTokenGenerator()

#make up a DatetimeIndex(timestamp)