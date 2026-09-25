# Copyright 2024 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Project Tag Security",
    'summary': "Adds access rules to project tags.",
    'description': '''
Project Tag Security
====================

    Adds access rules to project tags.

    Features:

        - UI Integration: Extends 1 view(s) in the Odoo interface.
        - Extends Odoo: Builds on project.project, project.tags, project.task.
    ''',
    "version": "18.0.1.0.0",
    "category": "Project Management",
    "website": "https://vertel.se/apps/odoo-oca-project/project_tag_security",
    "author": "Tecnativa, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": ["project"],
    "installable": True,
    "auto_install": True,
    "data": [
        "views/project_tags_views.xml",
    ],
    "maintainers": ["victoralmau"],
}
