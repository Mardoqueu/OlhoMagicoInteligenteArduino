# coding=utf-8
# Script para importar imagens para o Dropbox

# Importa a bibliotecas
import base64
import sys
from temboo.core.session import TembooSession
from temboo.Library.Dropbox.FilesAndMetadata import UploadFile

print str(sys.argv[1])

# Codificação da imagem
with open(str(sys.argv[1]), "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

# Declara a sessão Temboo e Choero para envio de arquivos.
session = TembooSession('yourSession', 'yourApp', 'yourKey')
uploadFileChoreo = UploadFile(session)

# Obtem um conjunto de objetos de entrada para o Choreo
uploadFileInputs = uploadFileChoreo.new_input_set()

# Configuração das entradas
uploadFileInputs.set_AppSecret("yourAppSecret")
uploadFileInputs.set_AccessToken("yourAccessToken")
uploadFileInputs.set_FileName(str(sys.argv[1]))
uploadFileInputs.set_AccessTokenSecret("yourTokenSecret")
uploadFileInputs.set_AppKey("yourAppKey")
uploadFileInputs.set_FileContents(encoded_string)
uploadFileInputs.set_Root("sandbox")

# Executa choreo
uploadFileResults = uploadFileChoreo.execute_with_results(uploadFileInputs)
