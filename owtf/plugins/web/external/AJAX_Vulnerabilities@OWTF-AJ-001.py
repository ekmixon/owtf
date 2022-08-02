"""
AJAX testing
"""
from owtf.plugin.helper import plugin_helper

DESCRIPTION = "Plugin to assist manual testing"


def run(PluginInfo):
    return plugin_helper.HtmlString("Intended to show helpful info in the future")
