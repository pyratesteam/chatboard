import datetime

class User:  
    

    def __init__ (self, name):
        self._name = name
        self._comment = None
        self._can_edit = False
        self._can_delete = False
        self._is_logged_in = False
        self._last_logged_in_at = None

    @property
    def user_type(self):
        return self.__class__.__name__

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    
    def is_logged_in(self):
        return self._is_logged_in

    @property
    def last_logged_in_at(self):
        return self._last_logged_in_at

    def log_in(self):
        self._is_logged_in = True
        self._last_logged_in_at = self.datetime.datetime.now()
        print('{} has successfully logged in'.format(self._name))

    def log_out(self):
        self._is_logged_in = False
        print('{} has successfully logged out'.format(self._name))
        
    def can_edit(self, comment):
        self._comment = comment
        if self._comment.author.name == self._name:        
            self._can_edit = True
        else:
            self._can_edit = False          
        return self._can_edit

    def can_delete(self, comment):
        self._comment = comment
        self._can_delete = False
        return self._can_delete

    def __repr__(self):
        return ('{} - {}').format(self._name, self._user_type)

    def __str__(self):
        return ('{} is in user group : {}').format(self._name, self.user_type)

    def to_string(self):
        return self.__str__()

class Admin(Moderator):

    def __init__(self, name):
        super(admin, self).__init__(name)
        self._name = name

    def can_edit(self, comment):
        self._comment = comment
        self._can_edit = True
        return self._can_edit

    def can_delete(self, comment):
        self._comment = comment
        self._can_delete = True
        return self._can_delete