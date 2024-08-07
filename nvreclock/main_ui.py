import gettext
import gi

from nvreclock.const import LOCALE_DIR, VERSION, APP_NAME, APP_ID

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gio

gettext.install('nvreclock', LOCALE_DIR)


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_title(APP_NAME)
        self._build_title_bar()

    def _build_content(self):
        pass

    def _build_title_bar(self):
        header = Gtk.HeaderBar()
        menu = Gio.Menu.new()
        menu.append(_("About"), "app.about")
        popover = Gtk.PopoverMenu()
        popover.set_menu_model(menu)
        hamburger = Gtk.MenuButton()
        hamburger.set_popover(popover)
        hamburger.set_icon_name("open-menu-symbolic")
        header.pack_end(hamburger)
        self.set_titlebar(header)


class NouveauReClock(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_action("about", self.build_about)
        self.connect("activate", self.on_activate)
        self.connect("shutdown", self.on_close)
        self.win = None

    def create_action(self, name, callback):
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

    def on_close(self, app):
        pass

    def build_about(self, widget, _a):
        about_ui = Adw.AboutDialog(
            application_name=APP_NAME,
            application_icon=APP_ID,
            developer_name="Z-Ray Entertainment",
            version=VERSION,
            developers=[
                "Vortex Acherontic https://github.com/VortexAcherontic",
            ],
            artists=[
                "Vortex Acherontic https://github.com/VortexAcherontic",
            ],
            translator_credits=_("translator-credits"),
            license_type=Gtk.License.MIT_X11,
            website="https://github.com/Z-Ray-Entertainment/nouveau-reclock",
            issue_url="https://github.com/Z-Ray-Entertainment/nouveau-reclock/issues",
            comments=_(
                "Nouveau Re-Clock is a graphical user interface to change the power state of a nvidia GPU "
                "using the open source nouveau driver")
        )
        about_ui.present(self.props.active_window)
