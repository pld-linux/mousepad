#
%define		xfce_version	4.4.0
#
Summary:	Text editor for Xfce based on Leafpad
Summary(pl):	Edytor tekstu dla Xfce oparty na Leafpadzie
Name:		mousepad
Version:	0.2.12
Release:	1
License:	GPL v2
Group:		X11/Applications/Editors
Source0:	http://www.xfce.org/archive/xfce-%{xfce_version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	8549b2012afc761cb4548b138e2ee23c
Patch0:		%{name}-desktop.patch
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.10.6
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	libxfcegui4-devel >= %{xfce_version}
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	xfce4-dev-tools >= %{xfce_version}
#Requires:	xfprint >= 4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mousepad is a lightweight text editor for Xfce. It features a simple
interface, broad character set support, printing with Xfprint, and
more. It opens lightening quick, making it perfect for editing config
files, doing quick scripting, and pretty printing documents like shell
scripts.

%description -l pl
Mousepad jest lekkim edytorem tekstowym dla Xfce. Cechuje go prosty
interfejs, obs³uga wielu zestawów znaków, drukowanie przy pomocy
Xfprint i wiele wiêcej. Uruchamia siê b³yskawicznie, dziêki czemu jest
idealny do edycji plików konfiguracyjnych, pisania ma³ych skryptów i
piêknego drukowania dokumentów takich jak skrypty pow³oki.

%prep
%setup -q
%patch0 -p1

%build
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/mousepad
%{_desktopdir}/mousepad.desktop
%{_pixmapsdir}/mousepad.png
