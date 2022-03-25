{
    'name': "Modulo Prueba",
    'version': '15.0.1',
    'depends': ['base'],
    'author': "Qualsys Consulting",
    'sumary': "Primer modulo",
    'category': 'customizations',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/vista_escuelas_view.xml',
        'views/vista_materias_view.xml',
        'views/vista_alumno_view.xml',
        
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        #'demo/demo_data.xml',
    ],
    'license': 'LGPL-3'
}
