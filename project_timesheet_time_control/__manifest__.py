# Copyright 2016 Tecnativa - Antonio Espinosa
# Copyright 2016 Tecnativa - Sergio Teruel
# Copyright 2016-2018 Tecnativa - Pedro M. Baeza
# Copyright 2018 Tecnativa - Ernesto Tejeda
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Project timesheet time control",
    'summary': "Adds time control to project timesheets.",
    'description': '''
Project timesheet time control
==============================

    Adds time control to project timesheets.

    Features:

        - Guided Wizards: Step-by-step dialogs for data entry.
        - UI Integration: Extends 3 view(s) in the Odoo interface.
        - Extends Odoo: Builds on account.analytic.line, hr.timesheet.time_control.mixin, project.project, project.task.
    ''',
    "version": "18.0.1.0.3",
    "category": "Project",
    "author": "Tecnativa," "Odoo Community Association (OCA)",
    "maintainers": ["ernestotejeda"],
    "website": "https://vertel.se/apps/odoo-oca-project/project_timesheet_time_control",
    "depends": [
        "hr_timesheet",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/account_analytic_line_view.xml",
        "views/project_project_view.xml",
        "views/project_task_view.xml",
        "wizards/hr_timesheet_switch_view.xml",
    ],
    "license": "AGPL-3",
    "installable": True,
    "post_init_hook": "post_init_hook",
}
