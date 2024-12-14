class SecurityGateway:
    def authenticate(self, api_key: str):
        return api_key == "MARS_SECURE_TOKEN_2026"