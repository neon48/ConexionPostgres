class Usuario:

    def __init__(self, id_usuario = None, username = None, password = None):
        self._id_usario= id_usuario
        self._username = username
        self._password = password

    def __str__(self):
        return f'Usuario:{self._id_usario}{self._username}{self._password}'

    @property
    def id_usuario(self):
        return self._id_usario
    @id_usuario.setter
    def id_usuario(self,id_usuario):
        self._id_usario=id_usuario

    @property
    def usarname(self):
        return self._usarname
    @usarname.setter
    def usarname(self,username):
        self._usarname=username

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self,password):
        self._password = password

