from dao.db_config import get_connection

class TurmaDAO:
    sqlSelect = 'SELECT id, semestre,professor_id FROM turma'

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        conn.close()
        return lista