from Persona import Persona
from loger_base import log
from Conexion import Conexion


class PersonaDao:
    '''
    DAO (Data Access Object)
    CRUD (Create - read-update-delete)
    '''

    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre = %s, apellido=%s, email=%s WHERE id_persona= %s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona = %s'

    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerCursor() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0],registro[1],registro[2],registro[3])
                personas.append(persona)
            return personas

    @classmethod
    def insertar(cls,Persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (Persona.nombre, Persona.apellido, Persona.email)
                cursor.execute(cls._INSERTAR,valores)
                log.debug(f'Persona Insertada: {Persona}')
                return cursor.rowcount


