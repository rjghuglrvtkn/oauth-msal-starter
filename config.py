class Config(object):
    # In a production app, store this instead in KeyVault or an environment variable
    # TODO: Enter your client secret from Azure AD below
    CLIENT_SECRET = "cLclRT~vo81~0Fs_N6_b4RZ6f6iDOYuah." 

    #AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app
    AUTHORITY = "https://login.microsoftonline.com/Merrimack College"

    # TODO: Enter your application client ID here
    CLIENT_ID = "d4928e4b-bc12-4573-8bb4-ca31ac41e1fe"

    # TODO: Enter the redirect path you want to use for OAuth requests
    #   Note that this will be the end of the URI entered back in Azure AD
    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL, 
        # which must match your app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"]

    SESSION_TYPE = "filesystem"  # So token cache will be stored in server-side session
