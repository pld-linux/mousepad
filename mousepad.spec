#
%define		xfce_version	4.6.0
#
Summary:	Text editor for Xfce based on Leafpad
Summary(pl.UTF-8):	Edytor tekstu dla Xfce oparty na Leafpadzie
Name:		mousepad
Version:	0.2.16
Release:	4
License:	GPL v2
Group:		X11/Applications/Editors
Source0:	http://www.xfce.org/archive/xfce-%{xfce_version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	d98854edb76d823ac20b266fdf5a64a1
Patch0:		%{name}-desktop.patch
URL:		http://www.xfce.org/projects/mousepad/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.10.6
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	libxfcegui4-devel >= %{xfce_version}
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	xfce4-dev-tools >= 4.6.0
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

mv $RPM_BUILD_ROOT%{_datadir}/locale/pt{_PT,}

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
%{_pixmapsdir}/mousepad.png
