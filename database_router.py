class DatabaseRouter:
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Prevent SQL migrations from affecting MongoDB
        return False
