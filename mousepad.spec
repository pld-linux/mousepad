Summary:	Text editor for Xfce based on Leafpad
Summary(pl.UTF-8):	Edytor tekstu dla Xfce oparty na Leafpadzie
Name:		mousepad
Version:	0.5.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Editors
Source0:	http://archive.xfce.org/src/apps/mousepad/0.5/%{name}-%{version}.tar.bz2
# Source0-md5:	d64c0e92337e49c5bcc807e622d4db9c
Patch0:		%{name}-desktop.patch
URL:		http://www.xfce.org/projects/mousepad/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 2.52.0
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	gtksourceview3-devel >= 3.24
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	xfce4-dev-tools >= 4.14.0
Requires:	desktop-file-utils
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
%patch0 -p1

mkdir -p m4

%{__sed} -i -e 's/AM_CONFIG_HEADER/AC_CONFIG_HEADERS/' configure.ac

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{hye,ie}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hy}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_desktop_database_postun
%update_icon_cache hicolor
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/mousepad
%{_desktopdir}/mousepad.desktop
%{_datadir}/glib-2.0/schemas/org.xfce.mousepad.gschema.xml
%{_datadir}/metainfo/mousepad.appdata.xml
%{_datadir}/polkit-1/actions/org.xfce.mousepad.policy
%{_iconsdir}/hicolor/*x*/apps/org.xfce.mousepad.png
%{_iconsdir}/hicolor/scalable/apps/org.xfce.mousepad.svg
