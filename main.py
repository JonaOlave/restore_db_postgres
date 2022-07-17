from restoredatabase.restoring_database import ConnectionDatabase as cd
from restoredatabase.restoring_database import restore_database as rd

connect = cd()
conn = connect.connect_database()

file_restore = 'db.sql'
rd(conn, file_restore)