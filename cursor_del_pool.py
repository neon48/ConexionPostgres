from loger_base import log
from ConexionPool import PoolConexion
class CursorDelPool:

    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug(f'Inicion del metodo with __enter__')
        self._conexion = PoolConexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipo_excepcion, valor_excepcion, detalle):
        log.debug(f'se ejecuta metodo __exit__')
        if valor_excepcion:
            self._conexion.rollback()
            log.error(f'Ocurrion una excepcion: {valor_excepcion}, {detalle}')
        else:
            self._conexion.commit()
            log.debug('commit de la transaccion')
        self._cursor.close()
        PoolConexion.liberarConexion(self._conexion)
