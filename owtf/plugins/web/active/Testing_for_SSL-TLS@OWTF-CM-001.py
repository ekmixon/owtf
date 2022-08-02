"""
ACTIVE Plugin for Testing for SSL-TLS (OWASP-CM-001)
"""
from owtf.managers.resource import get_resources
from owtf.plugin.helper import plugin_helper

DESCRIPTION = "Active probing for SSL configuration"


def run(PluginInfo):
    resource = get_resources("ActiveSSLCmds")
    return plugin_helper.CommandDump(
        "Test Command", "Output", resource, PluginInfo, []
    )
