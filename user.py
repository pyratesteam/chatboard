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

<<<<<<< HEAD
class Comment:

   def __init__(self, author, message, replied_to = None):
       self.author = author # object
       self.message = message        
       self.replied_to = replied_to # object
       self.created_at = author.datetime.datetime.now()

   def __repr__(self):
       return ('{} - {}').format(self.message, self.author.name)

   def __str__(self):
       if self.replied_to is None:
           return ('{} by {}').format(self.message, self.author.name)
       else:
           return ('{} by {} (replied to {})').format(self.message, self.author.name, self.replied_to.author.name)

   def to_string(self):
       return self.__str__()

=======
<<<<<<< HEAD
class Moderator(User):

    def __init__(self, name):
        super(moderator, self).__init__(name)
        self._name = name

    def can_edit(self, comment):
        if comment.author == self.name: return True
        return False

    def can_delete(self, comment):
        self._comment = comment
        self._can_delete = True
        return self._can_delete


=======
class Admin(Moderator):

    def __init__(self, name):
        super(admin, self).__init__(name)
        self._name = name

    def can_edit(self, comment):
        self._comment = comment
        self._can_edit = True
        return self._can_edit
>>>>>>> bbc087c3f9a0ea25a2e0c4ace02e713413ff0864

    def can_delete(self, comment):
        self._comment = comment
        self._can_delete = True
<<<<<<< HEAD
        return self._can_delete

=======
        return self._can_delete
>>>>>>> bbc087c3f9a0ea25a2e0c4ace02e713413ff0864
>>>>>>> 2fcec146a4c7b6348644bece363f429327d12226
