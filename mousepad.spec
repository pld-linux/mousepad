Summary:	Mousepad - a text editor for Xfce based on Leafpad
Summary(pl):	Mousepad - edytor dla Xfce oparty na Leafpadzie
Name:		mousepad
Version:	0.2.0
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Editors
Source0:	http://erikharrison.net/software/%{name}-%{version}.tar.gz
# Source0-md5:	e554145e8fffcd5fd8d3e027575e0765
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
interfejs, obs�uga wielu zestaw�w znak�w, drukowanie przy pomocy
Xfprint i wiele wi�cej. Uruchamia si� b�yskawicznie, dzi�ki czemu
jest idealny do edycji plik�w konfiguracyjnych, pisania ma�ych
skrypt�w i pi�knego drukowania dokument�w takich jak skrypty pow�oki.

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
