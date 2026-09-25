# Copyright 2024 Tecnativa - Carolina Fernandez
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Pivot view for projects",
    'summary': "Adds a pivot view for projects.",
    'description': '''
Pivot view for projects
=======================

    Adds a pivot view for projects.

    Features:

        - UI Integration: Extends 1 view(s) in the Odoo interface.
    ''',
    "version": "18.0.1.0.0",
    "category": "Project",
    "website": "https://vertel.se/apps/odoo-oca-project/project_pivot",
    "author": "Tecnativa, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "installable": True,
    "application": False,
    "depends": ["project"],
    "data": ["views/project_project.xml"],
    "maintainers": ["victoralmau"],
}
