# encoding: utf-8
"""
HTTP Error messages
"""
API_HELP = 'http://adsabs.github.io/help/api/'

CLASSIC_AUTH_FAILED = dict(
    message='Classic ADS Authentification failed',
    code=404
)

CLASSIC_DATA_MALFORMED = dict(
    message='You passed the wrong type. See the API documentation: {0}'.format(API_HELP),
    code=400
)

CLASSIC_BAD_MIRROR = dict(
    message='You passed a mirror site that does not exist. See the API documentation: {0}'.format(API_HELP),
    code=400
)

CLASSIC_NO_COOKIE = dict(
    message='Classic ADS end point did not return a cookie',
    code=500
)

CLASSIC_UNKNOWN_ERROR = dict(
    message='An unknown error occured on ADS Classic',
    code=500
)

CLASSIC_TIMEOUT = dict(
    message='Classic ADS end point timed out before it could respond (> 30s)',
    code=504
)

NO_CLASSIC_ACCOUNT = dict(
    message='This user has not setup an ADS Classic account',
    code=400
)

MYADS_TIMEOUT = dict(
    message='ADSWS myADS end point timed out before it could respond (> 30s)',
    code=504
)

MYADS_UNKNOWN_ERROR = dict(
    message='An unknown error occured on myADS',
    code=500
)
