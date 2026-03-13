import configparser

parser = configparser.ConfigParser()

parser.read('config.cfg')

print(parser.defaults())