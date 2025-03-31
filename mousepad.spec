Summary:	Text editor for Xfce based on Leafpad
Summary(pl.UTF-8):	Edytor tekstu dla Xfce oparty na Leafpadzie
Name:		mousepad
Version:	0.6.5
Release:	1
License:	GPL v2+
Group:		X11/Applications/Editors
Source0:	https://archive.xfce.org/src/apps/mousepad/0.6/%{name}-%{version}.tar.xz
# Source0-md5:	53a9ddeb8481ed8cd17d795c3881599b
Patch0:		%{name}-desktop.patch
URL:		https://www.xfce.org/projects/mousepad/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.56.2
BuildRequires:	gspell-devel >= 1.6.0
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	gtksourceview4-devel >= 4.0.0
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel >= 4.18
BuildRequires:	meson >= 0.57.0
BuildRequires:	ninja
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	polkit-devel >= 0.102
BuildRequires:	xfce4-dev-tools >= 4.18.0
Requires(post,postun):	desktop-file-utils
Requires:	glib2 >= 1:2.56.2
Requires:	gspell >= 1.6.0
Requires:	gtk+3 >= 3.22
Requires:	libxfce4ui >= 4.18
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mousepad is a lightweight text editor for Xfce. It features a simple
interface, broad character set support, printing with Xfprint, and
more. It opens lightening quick, making it perfect for editing config
files, doing quick scripting, and pretty printing documents like shell
scripts.

%description -l pl.UTF-8
Mousepad jest lekkim edytorem tekstowym dla Xfce. Cechuje go prosty
interfejs, obsługa wielu zestawów znaków, drukowanie przy pomocy
Xfprint i wiele więcej. Uruchamia się błyskawicznie, dzięki czemu jest
idealny do edycji plików konfiguracyjnych, pisania małych skryptów i
pięknego drukowania dokumentów takich jak skrypty powłoki.

%prep
%setup -q
%patch -P 0 -p1

mkdir -p m4

%{__sed} -i -e 's/AM_CONFIG_HEADER/AC_CONFIG_HEADERS/' configure.ac

%build
%meson
%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{hye,ie}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{fa_IR,fa}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hy}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libmousepad.a
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libmousepad.so

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_desktop_database_post
%update_icon_cache hicolor
%glib_compile_schemas

%postun
/sbin/ldconfig
%update_desktop_database_postun
%update_icon_cache hicolor
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS
%attr(755,root,root) %{_bindir}/mousepad
%attr(755,root,root) %{_libdir}/libmousepad.so.*.*.*
%attr(755,root,root) %{_libdir}/libmousepad.so.0
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/plugins/libmousepad-plugin-gspell.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/libmousepad-plugin-shortcuts.so
%{_desktopdir}/org.xfce.mousepad.desktop
%{_desktopdir}/org.xfce.mousepad-settings.desktop
%{_datadir}/glib-2.0/schemas/org.xfce.mousepad.gschema.xml
%{_datadir}/glib-2.0/schemas/org.xfce.mousepad.plugins.gspell.gschema.xml
%{_datadir}/metainfo/org.xfce.mousepad.appdata.xml
%{_datadir}/polkit-1/actions/org.xfce.mousepad.policy
%{_iconsdir}/hicolor/*x*/apps/org.xfce.mousepad.png
%{_iconsdir}/hicolor/scalable/apps/org.xfce.mousepad.svg
