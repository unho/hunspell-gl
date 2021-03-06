# -*- coding:utf-8 -*-

import codecs, os
import common


def createFoldersIfNeeded(path):
    try:
        os.makedirs(path)
    except:
        pass

class Generator(object):

    def generateFileContent(self):
        print "Reimplement this method in your subclass!"
        return ""

    def writeToResource(self, content):
        targetPath = os.path.join(common.getModulesSourcePath(), self.resource)
        createFoldersIfNeeded(os.path.dirname(targetPath))
        with codecs.open(targetPath, u"w", u"utf-8") as fileObject:
            fileObject.write(content)

    def run(self):
        self.writeToResource(self.generateFileContent())


wordsToIgnore = (
    # Nexos comúns.
    u"a", u"A", u"as", u"As", u"o", u"O", u"os", u"Os",
    u"á", u"Á", u"ás", u"Ás", u"ao", u"Ao", u"aos", u"Aos", u"ó", u"Ó", u"ós", u"Ós",
    u"da", u"Da", u"das", u"Das", u"de", u"De", u"do", u"Do", u"dos", u"Dos",
    u"e", u"E",
    u"en", u"En",
    u"entre", u"Entre",
    u"tras", u"Tras",

    # Outros termos comúns correctos en galego.
    u"Abaixo",
    u"Aldea", u"Aldeas",
    u"Alta", u"Altas", u"Alto", u"Altos",
    u"Arquipélago", u"Arquipélagos",
    u"Arrecife", u"Arrecifes",
    u"Arriba",
    u"Atol", u"Atois",
    u"Baixa", u"Baixas", u"Baixo", u"Baixos",
    u"Barrio", u"Barrios",
    u"Basílica", u"Basílicas",
    u"Branca", u"Brancas", u"Branco", u"Brancos",
    u"Beira", u"Beiras",
    u"Cabo",
    u"Camiño", u"Camiños",
    u"Campo", u"Campos",
    u"Capela", u"Capelas",
    u"Casa", u"Casas",
    u"Castelo", u"Castelos",
    u"Castiñeiro", u"Castiñeiros",
    u"Castro", u"Castros",
    u"Catedral", u"Catedrais",
    u"Central", u"Centrais",
    u"Centro", u"Centros",
    u"Cidade", u"Cidades",
    u"Cima", u"Cimas",
    u"Colexiata", u"Colexiatas",
    u"Colonia", u"Colonias",
    u"Comarca", u"Comarcas",
    u"Concello", u"Concellos",
    u"Condado", u"Condados",
    u"Confederación", u"Confederacións",
    u"continental", u"Continental", u"continentais", u"Continentais", # «Portugal continental».
    u"Convento", u"Conventos",
    u"Coroa", u"Coroas",
    u"Costa", u"Costas",
    u"Cova", u"Covas",
    u"Cruceiro", u"Cruceiros",
    u"Cruz", u"Cruces",
    u"Democrática", u"Democráticas", u"Democrático", u"Democráticos",
    u"Distrito", u"Distritos",
    u"Ducado", u"Ducados",
    u"Ermida", u"Ermidas",
    u"Estado", u"Estados",
    u"Estreito", u"Estreitos",
    u"Estrela", u"Estrelas",
    u"Exterior", u"Exteriores",
    u"Faro", u"Faros",
    u"Federación", u"Federacións",
    u"Federada", u"Federadas", u"Federado", u"Federados",
    u"Federal", u"Federais",
    u"Feira", u"Feiras",
    u"Fonte", u"Fontes",
    u"Gran", u"Grande", u"Grandes",
    u"Igrexa", u"Igrexas",
    u"Illa", u"Illas",
    u"Imperio", u"Imperios",
    u"Insua", u"Insuas",
    u"Interior", u"Interiores",
    u"Leste",
    u"Libre", u"Libres",
    u"Litoral", u"Litorais",
    u"Lombo", u"Lombos",
    u"Lugar", u"Lugares",
    u"Madeira", u"Madeiras",
    u"Maior", u"Maiores",
    u"Menor", u"Menores",
    u"Monte", u"Montes",
    u"Mosteiro", u"Mosteiros",
    u"Nova", u"Novas", u"Novo", u"Novos",
    u"Norte",
    u"Occidental", u"Occidentais",
    u"Oeste",
    u"Oliveira", u"Oliveiras",
    u"Oriental", u"Orientais",
    u"Outeiro", u"Outeiros",
    u"País", u"Países",
    u"Parada", u"Paradas",
    u"Partido", u"Partidos",
    u"Pazo", u"Pazos",
    u"Pena", u"Penas",
    u"Península", u"Penínsulas",
    u"Pequena", u"Pequenas", u"Pequeno", u"Pequenos",
    u"Ponte", u"Pontes",
    u"Popular", u"Populares",
    u"Porta", u"Portas",
    u"Pórtico", u"Pórticos",
    u"Porto", u"Portos",
    u"Prado", u"Prados",
    u"Praia", u"Praias",
    u"Principado", u"Principados",
    u"Provincia", u"Provincias",
    u"Real", u"Reais",
    u"Regato", u"Regatos",
    u"Regueiro", u"Regueiros",
    u"Reino", u"Reinos",
    u"República", u"Repúblicas",
    u"Rexión", u"Rexións",
    u"Ribeira", u"Ribeiras",
    u"Río", u"Ríos",
    u"Rúa", u"Rúas",
    u"Ruína", u"Ruínas",
    u"San", u"Santa", u"Santas", u"Santo", u"Santos",
    u"Santuario", u"Santuarios",
    u"Señorío", u"Señoríos",
    u"Serra", u"Serras",
    u"Silva", u"Silvas",
    u"Socialista", u"Socialistas",
    u"Sol", u"Soles",
    u"Souto", u"Soutos",
    u"Subrexión", u"Subrexións",
    u"Sur",
    u"Templo", u"Templos",
    u"Torre", u"Torres",
    u"Unida", u"Unidas", u"Unido", u"Unidos",
    u"Unión", u"Unións",
    u"Val", u"Vales",
    u"Veiga", u"Veigas",
    u"Vella", u"Vellas", u"Vello", u"Vellos",
    u"Verde", u"Verdes",
    u"Vila", u"Vilas"
    u"Vilar", u"Vilares",

    # Ordinais. Por exemplo, «Cuarta República».
    u"Primeira", u"Primeiras", u"Primeiro", u"Primeiros",
    u"Segunda", u"Segundas", u"Segundo", u"Segundos",
    u"Terceira", u"Terceiras", u"Terceiro", u"Terceiros",
    u"Cuarta", u"Cuartas", u"Cuarto", u"Cuartos",
    u"Quinta", u"Quintas", u"Quinto", u"Quintos",
    u"Sexta", u"Sextas", u"Sexto", u"Sextos",
    u"Sétima", u"Sétimas", u"Sétimo", u"Sétimos",
    u"Oitava", u"Oitavas", u"Oitavo", u"Oitavos",
    u"Novena", u"Novenas", u"Noveno", u"Novenos",
    u"Décima", u"Décimas", u"Décimo", u"Décimos",
)