# -*- coding: utf-8 -*-
"""
Django settings for lubangame  project.

"""
from config import codes

# message content
from django.utils.translation import ugettext_lazy as _

# Error message
ERROR_CODE_LABEL = {
    codes.ErrorCode.FAIL.value: _('Operation failed'),
    codes.ErrorCode.SUCCESS.value: _('Operation success'),
    codes.ErrorCode.UNAUTH.value: _('Session expired, login please!'),
    codes.ErrorCode.SIGN_ERROR.value: _('Signature error'),
    codes.ErrorCode.INVALID_PARAMS.value: _('Parameters error'),
    codes.ErrorCode.UPGRADE.value: _('Your app version is too old, please upgrade'),
    codes.ErrorCode.BLOCK_USER.value: _('Your account has been locked, please contact customer service'),
}
GENDER_LABEL = (
    (codes.Gender.MALE.value, u'男'),
    (codes.Gender.FEMALE.value, u'女'),
    (codes.Gender.UNKNOWN.value, u'未知'),
)
JOB_LABEL = (
    (codes.JobType.UNKNOWN.value,u'Unknown'),
    (codes.JobType.WORKING.value,u'Working'),
    (codes.JobType.NOWORK.value,u"NoWork"),
)
CONSTRUCTION_LABEL = (
    (codes.ConstructionType.UNKNOWN.value, u'Unknown'),
    (codes.ConstructionType.UI.value, u'UI'),
    (codes.ConstructionType.PROGRAM.value, u'Program'),
)