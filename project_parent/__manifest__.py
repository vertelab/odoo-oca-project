# © 2017-2019 Elico Corp (https://www.elico-corp.com).
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    "name": "Project Parent",
    'summary': "Adds parent projects.",
    'description': '''
Project Parent
==============

    Adds parent projects.

    Features:

        - UI Integration: Extends 1 view(s) in the Odoo interface.
        - Extends Odoo: Builds on parent_id, project.project.
    ''',
    "version": "18.0.1.0.0",
    "license": "LGPL-3",
    "category": "project",
    "author": "Therp B.V., Elico Corp, Odoo Community Association (OCA)",
    "website": "https://vertel.se/apps/odoo-oca-project/project_parent",
    "depends": ["project"],
    "data": ["views/project_parent_views.xml"],
    "demo": ["demo/project_project_demo.xml"],
}
