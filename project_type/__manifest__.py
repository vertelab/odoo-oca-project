# Copyright 2015 ADHOC SA (http://www.adhoc.com.ar)
# Copyright 2017 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Project Types",
    'summary': "Adds project types.",
    'description': '''
Project Types
=============

    Adds project types.

    Features:

        - UI Integration: Extends 3 view(s) in the Odoo interface.
        - Extends Odoo: Builds on complete_name, parent_id, project.project, project.task.
    ''',
    "version": "18.0.1.0.0",
    "category": "Project",
    "author": "ADHOC SA," "Tecnativa, " "Onestein, " "Odoo Community Association (OCA)",
    "website": "https://vertel.se/apps/odoo-oca-project/project_type",
    "license": "AGPL-3",
    "depends": ["project"],
    "data": [
        "views/project_type_views.xml",
        "views/project_project_views.xml",
        "views/project_task_views.xml",
        "security/ir.model.access.csv",
    ],
    "installable": True,
}
