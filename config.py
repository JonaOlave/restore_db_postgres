from configparser import ConfigParser


def config(file='database.ini', seccion='postgresql'):
    parser = ConfigParser()
    parser.read(file)

    db_config = {}

    for section_name in parser.sections():
        for name, value in parser.items(section_name):
            db_config[name] = value

    return db_config
