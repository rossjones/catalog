"""
Loads all of the actions from the action module in every file it can find
"""

ACTIONS = {}

def load_actions():
    for module_name in ['package', 'resource']:
        module_path = 'catalog.api.actions.' + module_name
        module = __import__(module_path)
        for part in module_path.split('.')[1:]:
            module = getattr(module, part)
        for k, v in module.__dict__.items():
            if not k.startswith('_'):
                ACTIONS[k] = v

def get_action(name):
    if not ACTIONS:
        load_actions()

    return ACTIONS.get(name)




"""
['package_show',
'current_package_list_with_resources',
'group_follower_count',
'harvest_source_index_clear',
'group_list_authz',
'recently_changed_packages_activity_list'
'member_delete'
'organization_revision_list'
'group_follower_list'
'site_read'
'group_member_delete'
'user_followee_list'
'unfollow_user'
'vocabulary_list'
'related_create'
'harvest_source_update'
'group_revision_list'
'package_activity_list'
'group_create',
'user_follower_count',
'activity_detail_list'
'organization_followee_list'
'dataset_followee_list'
'package_relationship_create_rest'
'am_following_user'
'member_roles_list'
'datastore_search_sql'
'revision_show'
'dataset_purge'
'follow_dataset'
'package_revision_list'
'resource_patch'
'organization_member_create'
'user_delete'
'user_followee_count'
'resource_create'
'resource_view_delete'
'dashboard_new_activities_count'
'tag_search'
'am_following_group'
'package_show_rest'
'resource_status_show'
'recently_changed_packages_activity_list_html'
'group_patch'
'group_list'
'datastore_delete',
'resource_search',
'package_autocomplete',
'resource_view_create',
'organization_update',
'vocabulary_create',
'user_update',
'follow_group',
'organization_purge',
'package_update',
'unfollow_dataset',
'tag_show_rest',
'member_list',
'group_followee_list',
'term_translation_update',
'format_autocomplete',
'tag_show',
'group_show',
'resource_view_clear',
'package_relationship_delete',
'revision_list',
'package_relationship_update_rest',
'am_following_dataset',
'harvesters_info_show',
'dashboard_mark_activities_old',
'dataset_followee_count',
'organization_show',
'group_update_rest',
'vocabulary_show',
'config_option_list',
'organization_autocomplete',
'user_show',
'follow_user',
'term_translation_update_many',
'group_purge',
'tag_autocomplete',
'organization_activity_list',
'bulk_update_public',
'group_update',
'datastore_make_private',
'group_show_rest',
'resource_view_reorder',
'tag_list',
'resource_delete',
'datastore_search',
'resource_view_list',
'config_option_update',
'vocabulary_delete',
'resource_create_default_resource_views',
'datastore_upsert',
'package_relationships_list',
'package_create_default_resource_views',
'task_status_update_many',
'package_patch',
'tag_create',
'package_search',
'package_resource_reorder',
'dataset_follower_list',
'organization_activity_list_html',
'dashboard_activity_list_html',
'datastore_info',
'get_site_user',
'task_status_delete',
'user_activity_list',
'user_invite',
'resource_update',
'send_email_notifications',
'harvest_source_delete',
'vocabulary_update',
'license_list',
'group_delete',
'task_status_show',
'bulk_update_private',
'package_delete',
'rating_create',
'organization_list_for_user',
'member_create',
'config_option_show',
'datastore_make_public',
'followee_count',
'package_relationship_update',
'group_member_create',
'harvest_source_clear',
'harvest_sources_reindex',
'harvest_job_create',
'harvest_source_show',
'package_relationship_delete_rest',
'resource_view_update',
'user_generate_apikey',
'status_show',
'tag_delete',
'user_activity_list_html',
'followee_list',
'datastore_create',
'package_owner_org_update',
'harvest_object_show',
'package_relationship_create',
'resource_view_show',
'harvest_source_show_status',
'group_activity_list',
'organization_delete',
'bulk_update_delete',
'unfollow_group',
'resource_show',
'package_create_rest',
'organization_patch',
'organization_list',
'related_list',
'organization_member_delete',
'dataset_follower_count',
'package_list',
'group_activity_list_html',
'package_activity_list_html',
'dashboard_activity_list',
'group_followee_count',
'help_show',
'harvest_jobs_run',
'user_create',
'organization_create',
'user_autocomplete',
'organization_follower_list',
'group_create_rest',
'term_translation_show',
'package_create',
'task_status_update',
'organization_follower_count',
'group_package_show',
'activity_create',
'package_update_rest',
'user_follower_list',
'user_list']

"""