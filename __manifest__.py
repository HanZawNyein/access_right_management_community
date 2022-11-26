{
    "name": "Access Right Management",
    "data": [
        'security/access_right_control.xml',
        'security/ir.model.access.csv',
        'views/access_right_management.xml',
        'views/res_users.xml'
    ],
    'assets': {
        'web.assets_backend': [
            '/access_right_management/static/js/action_item.js',
        ]
    },
    'post_init_hook': 'post_install_action_dup_hook'
}
