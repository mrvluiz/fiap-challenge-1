import pandas as pd
from flask import Flask, jsonify
from flask_restx import Api, Resource

PRODUCAO = 'http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv'
PROCESS_VINIFERAS = 'http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv'
PROCESS_AMERICANAS = 'http://vitibrasil.cnpuv.embrapa.br/download/ProcessaAmericanas.csv'
PROCESS_MESA = 'http://vitibrasil.cnpuv.embrapa.br/download/ProcessaMesa.csv'
PROCESS_SEM_CLASSIFICACAO = 'http://vitibrasil.cnpuv.embrapa.br/download/ProcessaSemclass.csv'
COMERCIO = 'http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv'
IMPORTACAO_VINHOS = 'http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv'
IMPORTACAO_ESPUMANTES = 'http://vitibrasil.cnpuv.embrapa.br/download/ImpEspumantes.csv'
IMPORTACAO_UVAS_FRESCAS = 'http://vitibrasil.cnpuv.embrapa.br/download/ImpFrescas.csv'
IMPORTACAO_UVAS_PASSAS = 'http://vitibrasil.cnpuv.embrapa.br/download/ImpPassas.csv'
IMPORTACAO_SUCO_UVA = 'http://vitibrasil.cnpuv.embrapa.br/download/ImpSuco.csv'
EXPORTACAO_VINHOS_MESA = 'http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv'
EXPORTACAO_ESPUMANTES = 'http://vitibrasil.cnpuv.embrapa.br/download/ExpEspumantes.csv'
EXPORTACAO_UVAS_FRESCAS = 'http://vitibrasil.cnpuv.embrapa.br/download/ExpUva.csv'
EXPORTACAO_SUCO_UVA = 'http://vitibrasil.cnpuv.embrapa.br/download/ExpSuco.csv'

app  = Flask(__name__)
app.json.sort_keys = False
api = Api(app,
            version='1.0.0',
            title='API Embrapa Services',
            description='API para consumo e disponibilização das informações da Embrapa',
            default='Principal'
            )


@api.route("/producao/")
@api.doc(description="Retorna a Produção de vinhos, sucos e derivados do Rio Grande do Sul")
class Producao(Resource):        
        def get(self):  
                list = ReadCSV(PRODUCAO, ';', 1)
                return jsonify(list)        

@api.route("/producao/<int:id>")
@api.doc(description="Retorna a Produção de vinhos, sucos e derivados do Rio Grande do Sul de um produto específico", params={'id': 'ID do Produto '})
class ProducaoById(Resource):
        def get(self, id):
                list = ReadCSV(PRODUCAO, ';', 1)
                for produto in list:
                    if produto.get('id') == id:
                        return jsonify(produto) 

@api.route("/processamento/viniferas/")
@api.doc(description="Retorna a Quantidade de uvas processadas no Rio Grande do Sul do tipo Viníferas")
class ProcessamentoViniferas(Resource):        
        def get(self):  
                list = ReadCSV(PROCESS_VINIFERAS, '\t', 1)
                return jsonify(list)
        

@api.route("/processamento/viniferas/<int:id>")
@api.doc(description="Retorna a Quantidade de uvas processadas no Rio Grande do Sul do tipo Viníferas de um produto específico", params={'id': 'ID do Produto '})
class ProcessamentoViniferasById(Resource):
        def get(self, id):
                list = ReadCSV(PROCESS_VINIFERAS, '\t', 1)
                for produto in list:
                    if produto.get('id') == id:
                        return jsonify(produto)
                    
@api.route("/processamento/americanashibridas/")
@api.doc(description="Retorna a Quantidade de uvas processadas no Rio Grande do Sul do tipo Americanas e Híbridas")
class ProcessamentoAmericanasHibridas(Resource):        
        def get(self):  
                list = ReadCSV(PROCESS_AMERICANAS, '\t', 1)
                return jsonify(list)
        

@api.route("/processamento/americanashibridas/<int:id>")
@api.doc(description="Retorna a Quantidade de uvas processadas no Rio Grande do Sul do tipo Americanas e Híbridas de um produto específico", params={'id': 'ID do Produto '})
class ProcessamentoAmericanasHibridasById(Resource):
        def get(self, id):
                list = ReadCSV(PROCESS_AMERICANAS, '\t', 1)
                for produto in list:
                    if produto.get('id') == id:
                        return jsonify(produto)
                    

@api.route("/processamento/uvasmesa/")
@api.doc(description="Retorna a Quantidade de uvas processadas no Rio Grande do Sul do tipo Uvas de Mesa")
class ProcessamentoUvasMesa(Resource):        
        def get(self):  
                list = ReadCSV(PROCESS_MESA, '\t', 1)
                return jsonify(list)
        

@api.route("/processamento/uvasmesa/<int:id>")
@api.doc(description="Retorna a Quantidade de uvas processadas no Rio Grande do Sul do tipo Uvas de Mesa de um produto específico", params={'id': 'ID do Produto '})
class ProcessamentoUvasMesaById(Resource):
        def get(self, id):
                list = ReadCSV(PROCESS_MESA, '\t', 1)
                for produto in list:
                    if produto.get('id') == id:
                        return jsonify(produto)
                    

@api.route("/processamento/semclassificacao/")
@api.doc(description="Retorna a Quantidade de uvas processadas no Rio Grande do Sul do tipo Sem Classificação")
class ProcessamentoSemClassificacao(Resource):        
        def get(self):  
                list = ReadCSV(PROCESS_SEM_CLASSIFICACAO, '\t', 1)
                return jsonify(list)
        

@api.route("/processamento/semclassificacao/<int:id>")
@api.doc(description="Retorna a Quantidade de uvas processadas no Rio Grande do Sul do tipo Sem Classificação de um produto específico", params={'id': 'ID do Produto '})
class ProcessamentoSemClassificacaoById(Resource):
        def get(self, id):
                list = ReadCSV(PROCESS_SEM_CLASSIFICACAO, '\t', 1)
                for produto in list:
                    if produto.get('id') == id:
                        return jsonify(produto)
                    

@api.route("/comercializacao/")
@api.doc(description="Retorna a Comercialização de vinhos e derivados no Rio Grande do Sul")
class Comercializacao(Resource):        
        def get(self):  
                list = ReadCSV(COMERCIO, ';', 1)
                return jsonify(list)
        

@api.route("/comercializacao/<int:id>")
@api.doc(description="Retorna a Comercialização de vinhos e derivados no Rio Grande do Sul de um produto específico", params={'id': 'ID do Produto '})
class ComercializacaoById(Resource):
        def get(self, id):
                list = ReadCSV(COMERCIO, ';', 1)
                for produto in list:
                    if produto.get('id') == id:
                        return jsonify(produto)
                    
@api.route("/importacao/vinhosmesa/")
@api.doc(description="Retorna a Importação de derivados de uva do tipo Vinhos de mesa")
class ImportacaoVinhoMesa(Resource):        
        def get(self):  
                list = ReadCSV(IMPORTACAO_VINHOS, ';', 2)
                return jsonify(list)        

@api.route("/importacao/vinhosmesa/<int:id>")
@api.doc(description="Retorna a Importação de derivados de uva do tipo Vinhos de mesa de um produto específico", params={'id': 'ID do Produto '})
class ImportacaoVinhoMesaById(Resource):
        def get(self, id):
                list = ReadCSV(IMPORTACAO_VINHOS, ';', 2)
                for produto in list:
                    if produto.get('id') == id:
                        return jsonify(produto)
                    
@api.route("/importacao/espumantes/")
@api.doc(description="Retorna a Importação de derivados de uva do tipo Espumantes")
class ImportacaoEspumantes(Resource):        
        def get(self):  
                list = ReadCSV(IMPORTACAO_ESPUMANTES, ';', 2)
                return jsonify(list)        

@api.route("/importacao/espumantes/<int:id>")
@api.doc(description="Retorna a Importação de derivados de uva do tipo Espumantes de um produto específico", params={'id': 'ID do Produto '})
class ImportacaoEspumantesById(Resource):
        def get(self, id):
                list = ReadCSV(IMPORTACAO_ESPUMANTES, ';', 2)
                for produto in list:
                    if produto.get('id') == id:
                        return jsonify(produto)

@api.route("/importacao/uvasfrescas/")
@api.doc(description="Retorna a Importação de derivados de uva do tipo Uvas Frescas")
class ImportacaoUvasFrescas(Resource):        
        def get(self):  
                list = ReadCSV(IMPORTACAO_UVAS_FRESCAS, ';', 2)
                return jsonify(list)        

@api.route("/importacao/uvasfrescas/<int:id>")
@api.doc(description="Retorna a Importação de derivados de uva do tipo Uvas Frescas de um produto específico", params={'id': 'ID do Produto '})
class ImportacaoUvasFrescasById(Resource):
        def get(self, id):
                list = ReadCSV(IMPORTACAO_UVAS_FRESCAS, ';', 2)
                for produto in list:
                    if produto.get('id') == id:
                        return jsonify(produto)


@api.route("/importacao/uvaspassas/")
@api.doc(description="Retorna a Importação de derivados de uva do tipo Uvas Passas")
class ImportacaoUvasPassas(Resource):        
        def get(self):  
                list = ReadCSV(IMPORTACAO_UVAS_PASSAS, ';', 2)
                return jsonify(list)        

@api.route("/importacao/uvaspassas/<int:id>")
@api.doc(description="Retorna a Importação de derivados de uva do tipo Uvas Passas de um produto específico", params={'id': 'ID do Produto '})
class ImportacaoUvasPassasById(Resource):
        def get(self, id):
                list = ReadCSV(IMPORTACAO_UVAS_PASSAS, ';', 2)
                for produto in list:
                    if produto.get('id') == id:
                        return jsonify(produto)
                    

@api.route("/importacao/sucouva/")
@api.doc(description="Retorna a Importação de derivados de uva do tipo Suco de Uva")
class ImportacaoSucoUva(Resource):        
        def get(self):  
                list = ReadCSV(IMPORTACAO_SUCO_UVA, ';', 2)
                return jsonify(list)        

@api.route("/importacao/sucouva/<int:id>")
@api.doc(description="Retorna a Importação de derivados de uva do tipo Suco de Uva de um produto específico", params={'id': 'ID do Produto '})
class ImportacaoSucoUvaById(Resource):
        def get(self, id):
                list = ReadCSV(IMPORTACAO_SUCO_UVA, ';', 2)
                for produto in list:
                    if produto.get('id') == id:
                        return jsonify(produto)
                    

@api.route("/exportacao/vinhomesa/")
@api.doc(description="Retorna a Exportação de derivados de uva do tipo Vinho de Mesa")
class ExportacaoVinhoMesa(Resource):        
        def get(self):  
                list = ReadCSV(EXPORTACAO_VINHOS_MESA, ';', 2)
                return jsonify(list)        

@api.route("/exportacao/vinhomesa/<int:id>")
@api.doc(description="Retorna a Exportação de derivados de uva do tipo Vinho de Mesa de um produto específico", params={'id': 'ID do Produto '})
class ExportacaoVinhoMesaById(Resource):
        def get(self, id):
                list = ReadCSV(EXPORTACAO_VINHOS_MESA, ';', 2)
                for produto in list:
                    if produto.get('id') == id:
                        return jsonify(produto)
                    

@api.route("/exportacao/espumantes/")
@api.doc(description="Retorna a Exportação de derivados de uva do tipo Espumantes")
class ExportacaoEspumantes(Resource):        
        def get(self):  
                list = ReadCSV(EXPORTACAO_ESPUMANTES, ';', 2)
                return jsonify(list)        

@api.route("/exportacao/espumantes/<int:id>")
@api.doc(description="Retorna a Exportação de derivados de uva do tipo Espumantes de um produto específico", params={'id': 'ID do Produto '})
class ExportacaoEspumantesById(Resource):
        def get(self, id):
                list = ReadCSV(EXPORTACAO_ESPUMANTES, ';', 2)
                for produto in list:
                    if produto.get('id') == id:
                        return jsonify(produto)
                    
@api.route("/exportacao/uvasfrescas/")
@api.doc(description="Retorna a Exportação de derivados de uva do tipo Uvas Frescas")
class ExportacaoUvasFrescas(Resource):        
        def get(self):  
                list = ReadCSV(EXPORTACAO_UVAS_FRESCAS, ';', 2)
                return jsonify(list)        

@api.route("/exportacao/uvasfrescas/<int:id>")
@api.doc(description="Retorna a Exportação de derivados de uva do tipo Uvas Frescas de um produto específico", params={'id': 'ID do Produto '})
class ExportacaoUvasFrescasById(Resource):
        def get(self, id):
                list = ReadCSV(EXPORTACAO_UVAS_FRESCAS, ';', 2)
                for produto in list:
                    if produto.get('id') == id:
                        return jsonify(produto)
                    
@api.route("/exportacao/sucouva/")
@api.doc(description="Retorna a Exportação de derivados de uva do tipo Suco de Uva")
class ExportacaoSucoUva(Resource):        
        def get(self):  
                list = ReadCSV(EXPORTACAO_SUCO_UVA, ';', 2)
                return jsonify(list)        

@api.route("/exportacao/sucouva/<int:id>")
@api.doc(description="Retorna a Exportação de derivados de uva do tipo Suco de Uva de um produto específico", params={'id': 'ID do Produto '})
class ExportacaoSucoUvaById(Resource):
        def get(self, id):
                list = ReadCSV(EXPORTACAO_SUCO_UVA, ';', 2)
                for produto in list:
                    if produto.get('id') == id:
                        return jsonify(produto)

    
def ReadCSV(url, csvSep, tipo):    
        productionData = pd.read_csv(url, sep=csvSep)
        productionData.head()
        columns = []       
        producaoList = []

        for idx, colname in enumerate(productionData.columns):
            columns.append(
            {
            'index' : idx,
            'colname' : colname,       
            })      
        
        if tipo == 1:
            for values in productionData.values:             
                producaoAnual = []
                maxvalues = len(values)

                for idx, obj in enumerate(values):
                    if (idx > 2) :
                        ano= columns[idx].get('colname')              
                        quantidade=obj
                        producaoAnual.append({'ano':ano, 'quantidade': quantidade})       
            
                producaoList.append({
                            columns[0].get('colname') : values[0],
                            columns[1].get('colname') : values[1],
                            columns[2].get('colname') : values[2],    
                            'DadosAnuais' : producaoAnual 
                            })   
        else:
            if tipo == 2:
                for values in productionData.values:             
                    producaoAnual = []
                    maxvalues = len(values)

                    for idx, obj in enumerate(values):
                        if (idx > 1) :
                            ano= columns[idx].get('colname')                    
                            if( (idx+1) < maxvalues):
                                if columns[idx + 1].get('colname')  == (ano + ".1") :  #significa que podemos consolidar para o proximo, e adiantar o index
                                    quantidade= obj 
                                    valor = values[idx+1]                           

                                    producaoAnual.append({'ano':ano, 'quantidade': quantidade, 'valor' : valor})                        

                    producaoList.append({
                                columns[0].get('colname')  : values[0],
                                columns[1].get('colname')  : values[1],                      
                                'DadosAnuais' : producaoAnual 
                                })
                    
        return producaoList

if __name__ == "__main__":
    app.run(port=5000, host='localhost')