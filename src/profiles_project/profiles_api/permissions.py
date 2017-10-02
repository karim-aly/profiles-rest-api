from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""

        # check if request method is safe (e.g: GET)
        if request.method in permissions.SAFE_METHODS:
            return True

        # check if request made for editing is from the profile's owner
        if request.user.id == obj.id:
            return True

        return False


class PostOwnStatus(permissions.BasePermission):
    """Allow users to update only their status"""

    def has_object_permission(self, request, view, obj):
        """Checks the user is trying to update their own status"""

        # check if request method is safe (e.g: GET)
        if request.method in permissions.SAFE_METHODS:
            return True

        # check if request made for editing is from the profile's owner
        if request.user.id == obj.user_profile.id:
            return True

        return False