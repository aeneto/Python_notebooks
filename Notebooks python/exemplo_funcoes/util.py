import os
from pathlib import Path
from zipfile import ZipFile
import unicodedata


def rename_file(old_name, new_name, tmp_subdir):
    """ Function to rename a file.

    :param old_name: Automatic name or old name of the file.
    :type old_name: str
    :param new_name: New name of the file.
    :type new_name: str
    :param tmp_subdir: Directory where the file is.
    :type tmp_subdir: str
    :return: None
    """
    old_file = os.path.join(tmp_subdir, old_name)
    new_file = os.path.join(tmp_subdir, new_name)
    os.rename(old_file, new_file)


def convert_to_non_accent(string):
    """ Function to convert accent characters to non accent
    characters.

    :param string: String to be converted.
    :type string: str
    :return: str
    
    Como utilizar ?
    dataframe.columns = list(convert_to_non_accent(x)
                             for x in dataframe.columns)
    """
    return ''.join(ch for ch in unicodedata.normalize('NFKD', string)
                   if not unicodedata.combining(ch))



def formata_campo(campo):
    
    """ Funcao que elimina acentos e caracteres definidos nessa função
        Também tira os acentos e transforma espaço em _
        
        Como utilizar:
        
        dataframe.columns = list(formata_campo(x)
                             for x in data_frame.columns)
        
        
    """
    nova_string = campo
    for x in campo:
        nova_string = nova_string.strip()
        nova_string = nova_string.replace(" ", "_")
        nova_string = nova_string.replace(".", "")
        nova_string = nova_string.replace("(", "_")
        nova_string = nova_string.replace(")", "_")
        nova_string = nova_string.replace("-", "_")
        nova_string = nova_string.replace("__", "")
        nova_string = nova_string.replace("__", "")
        nova_string = nova_string.replace("'", "")
        nova_string = nova_string.lower()
        nova_string = ''.join(ch for ch in unicodedata.normalize('NFKD', nova_string)
                   if not unicodedata.combining(ch))

    return nova_string
                

    