from rest_framework.throttling import UserRateThrottle


class PremiumThrottle(UserRateThrottle):
    def __init__(self):
        pass
    
    def allow_request(self, request, view):
        premium_scope = getattr(view, 'premium_scope', None)
        light_scope = getattr(view, 'light_scope', None)

        if request.user.profile.is_premium_user:
            if not premium_scope:
                return True
            self.scope = premium_scope
        else:
            if not light_scope:
                return True
            self.scope = light_scope
        
        self.rate = self.get_rate()
        self.num_requests, self.duration = self.parse_rate(self.rate)

        return super().allow_request(request, view)
