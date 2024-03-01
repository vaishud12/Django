from rest_framework import permissions

BLACKLISTED_IPS=['127.0.0.1']

# BLACKLISTED_IPS=[]
class CustomerPermission(permissions.BasePermission):
    message="you are now allowed to view this api since your ip and is blocked"
    def has_permission(self, request, view ):
        ip_addr=request.META['REMOTE_ADDR']
        # print(ip_addr)
        # return True
        if ip_addr in BLACKLISTED_IPS:
            return False
        return True