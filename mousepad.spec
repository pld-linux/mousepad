Summary:	Mousepad - a text editor for Xfce based on Leafpad
Summary(pl):	Mousepad - edytor dla Xfce oparty na Leafpadzie
Name:		mousepad
Version:	0.2.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Editors
Source0:	http://erikharrison.net/software/%{name}-%{version}.tar.gz
# Source0-md5:	9a5bf90acc6fffd5c09334c7cb4b7054
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libxfcegui4-devel >= 4.2.0
BuildRequires:	pkgconfig  >= 1:0.9.0
Requires:	libxfcegui4 >= 4.2.0
Requires:	xfprint >= 4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mousepad is a lightweight text editor for Xfce. It features a simple
interface,  broad character set support, printing with Xfprint, and
more. It opens lightening quick, making it perfect for editing config
files, doing quick scripting, and pretty printing documents like shell
scripts.

%description -l pl
Mousepad jest lekkim edytorem tekstowym dla Xfce. Cechuje go prosty
interfejs, obs³uga wielu zestawów znaków, drukowanie przy pomocy
Xfprint i wiele wiêcej. Uruchamia siê b³yskawicznie, dziêki czemu
jest idealny do edycji plików konfiguracyjnych, pisania ma³ych
skryptów i piêknego drukowania dokumentów takich jak skrypty pow³oki.

%prep
%setup -q

%build
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
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_pixmapsdir}/*
