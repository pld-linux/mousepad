Summary:	Text editor for Xfce based on Leafpad
Summary(pl.UTF-8):	Edytor tekstu dla Xfce oparty na Leafpadzie
Name:		mousepad
Version:	0.4.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Editors
Source0:	http://archive.xfce.org/src/apps/mousepad/0.4/%{name}-%{version}.tar.bz2
# Source0-md5:	98d908842d4a93c35756a67d681c08fe
Patch0:		%{name}-desktop.patch
URL:		http://www.xfce.org/projects/mousepad/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gtk+2-devel >= 2:2.24.0
BuildRequires:	gtksourceview3-devel
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

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hy}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/mousepad
%{_desktopdir}/mousepad.desktop
%{_datadir}/glib-2.0/schemas/org.xfce.mousepad.gschema.xml
%{_datadir}/polkit-1/actions/org.xfce.mousepad.policy
