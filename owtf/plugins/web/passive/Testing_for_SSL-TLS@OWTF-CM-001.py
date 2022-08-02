"""
PASSIVE Plugin for Testing_for_SSL-TLS_(OWASP-CM-001)
"""
from owtf.plugin.helper import plugin_helper

DESCRIPTION = "Third party resources"


def run(PluginInfo):
    # Vuln search box to be built in core and resued in different plugins:
    resource = get_resources("PassiveSSL")
    return plugin_helper.resource_linklist("Online Resources", resource)
