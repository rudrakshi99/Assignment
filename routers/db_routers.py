class AppRouter:
    """
    A router to control all database operations on models in the
    product application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read user models go to postgres.
        """
        if model._meta.app_label == 'product':
            return 'postgres'
        return 'default'

    def db_for_write(self, model, **hints):
        """
        Attempts to write user models go to postgres.
        """
        if model._meta.app_label == 'product':
            return 'postgres'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the user app is involved.
        """
        if obj1._meta.app_label == 'product' or \
           obj2._meta.app_label == 'product':
           return True
        elif 'product' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True

        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'postgres'
        database.
        """
        if app_label == 'product':
            return db == 'postgres'
        return None
