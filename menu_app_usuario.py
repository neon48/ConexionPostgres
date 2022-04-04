import logging

from Usuario import Usuario
from loger_base import log

from UsuarioDao import UsuarioDao

opcion = None

while opcion != 5:
    print('Opciones:')
    print('1- Listar Usuarios')
    print('2- Agregar Usuario')
    print('3- Modificar Usuario')
    print('4- Elimiar Usuario')
    print('5- Salir')
    opcion = int(input('Escribe la opcion (1-5):'))
    if opcion == 1:
        usuarios = UsuarioDao.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    if opcion == 2:
        username_var =input("Escribe el username:")
        password_var = input("Escribe el password")
        usuario = Usuario(username=username_var,password=password_var)
        usuarios_insertados = UsuarioDao.insertar(usuario)
        log.info(f'Usuarios insertados:{usuarios_insertados}')