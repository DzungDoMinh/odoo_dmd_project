# -*- coding: utf-8 -*-
{
    'name': "DMD project tasks",  # Module title
    'description': """This is DMD project tasks with timeline view""",  # You can also rst format
    'author': "Do Minh Dzung, MSc.",
    'website': "http://tan-phong-ec.odoo.com",
    'category': 'Project',
    'version': '14.0.1',
    'depends': ['project', 'web_timeline', 'account'],
    'data': [
        'views/dmd_project_tasks_view.xml',
        'views/tasks_timeline_view.xml',
    ],
    'demo': [
    ],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
