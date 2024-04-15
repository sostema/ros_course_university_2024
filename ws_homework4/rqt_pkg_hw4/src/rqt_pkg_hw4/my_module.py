import os
import rospy
import rospkg
from argparse import ArgumentParser

from qt_gui.plugin import Plugin
from python_qt_binding import loadUi
from python_qt_binding.QtWidgets import QWidget


class PluginSostema(Plugin):

    def __init__(self, context):
        super(PluginSostema, self).__init__(context)
        # Give QObjects reasonable names
        self.setObjectName('PluginSostema')

        # Process standalone plugin command-line arguments
        parser = ArgumentParser()
        # Add argument(s) to the parser.
        parser.add_argument("-q", "--quiet", action="store_true",
                      dest="quiet",
                      help="Put plugin in silent mode")
        args, unknowns = parser.parse_known_args(context.argv())
        if not args.quiet:
            print(f'arguments: {args}')
            print(f'unknowns: {unknowns}')

        # Create QWidget
        self._widget = QWidget()
        ui_file = os.path.join(rospkg.RosPack().get_path('rqt_pkg_hw4'), 'resource', 'PluginSostema.ui')
        loadUi(ui_file, self._widget)
        self._widget.setObjectName('PluginSostemaUi')

        if context.serial_number() > 1:
            self._widget.setWindowTitle(
                f"{self._widget.windowTitle()} ({context.serial_number()})"
                )

        context.add_widget(self._widget)

    def shutdown_plugin(self):
        self._widget.close()

    def save_settings(self, plugin_settings, instance_settings):
        pass

    def restore_settings(self, plugin_settings, instance_settings):
        pass