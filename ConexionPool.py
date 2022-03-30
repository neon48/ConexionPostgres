#Instalamos psycopg2 con pip install psycopg2 para poder trabajar con base de datos Postgres
from psycopg2 import pool
#se importa la clase creada loger base para guarda log de eventos
from loger_base import log
#Sys nos permite trabajar con archivos del sistema, en este caso para terminar proceso
import sys

class PoolConexion:
    #Variables iniciales de conexion
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool == None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      host = cls._HOST,
                                                      user = cls._USERNAME,
                                                      password = cls._PASSWORD,
                                                      port = cls._DB_PORT,
                                                      database = cls._DATABASE)
                log.debug(f'Creacion de pool exitosa:{cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error al obtnere el pool{e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexion Obtenida del pool: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls,conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos el pool de conexion: {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()
        log.debug(f'se cerraron todas las conexiones')
