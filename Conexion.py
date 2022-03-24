#Instalamos psycopg2 con pip install psycopg2 para poder trabajar con base de datos Postgres
import psycopg2 as bd
#se importa la clase creada loger base para guarda log de eventos
from loger_base import log
#Sys nos permite trabajar con archivos del sistema, en este caso para terminar proceso
import sys

class Conexion:
    #Variables iniciales de conexion
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _conexion = None
    _cursor = None

    #Funcion para realizar la conexion con la base de datos
    @classmethod
    def obtenerConexion(cls):
        #Si la conexion aun no ha sido creada (igual a None) la creamos
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(host = cls._HOST,
                                           user=cls._USERNAME,
                                           password=cls._PASSWORD,
                                           port = cls._DB_PORT,
                                           database = cls._DATABASE
                                           )
                log.debug(f'Conexion exitosa:{cls._conexion}')
                return cls._conexion
            except Exception as e:
                log.debug(f'Conexion fallida:{e}')
                sys.exit()
        else:
            return cls._conexion

    #Creamos el cursor y llamamos a la Funcion Conexion
    @classmethod
    def obtenerCursor(cls):
        #Si el cursor no ha sido creado lo creamos
        if cls._cursor is None:
            try:
                cls._cursor=cls.obtenerConexion().cursor()
                log.debug('Se abrio correctamente el cursor')
                return cls._cursor
            except Exception as e:
                log.error(f'Ocurrio una excepcion al obtener el cursor: {e}')
                sys.exit()
        else:
            return cls._cursor


conex = Conexion()
cursor = conex.obtenerCursor()
sentencia= 'INSERT INTO persona(nombre, apellido, email) VALUES (%s,%s,%s)'
valores=('Frailejon','Perez','asdasd@3232.com')
cursor.execute(sentencia,valores)
