Summary:	Mousepad is a text editor for Xfce based on Leafpad
Summary(pl):	Mousepad jest edytorem dla Xfce opartym na Leafpad
Name:		mousepad
Version:	0.2.0
Release:	0.1
License:	GPLv2
Group:		X11/Applications/Editors
Source0:	http://erikharrison.net/software/%{name}-%{version}.tar.gz
# Source0-md5:	e554145e8fffcd5fd8d3e027575e0765
#URL:		none_at_the_moment_I_think
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	libxfcegui4-devel
BuildRequires:	libxfce4util-devel
Requires:	libxfcegui4
Requires:	libxfce4util
Requires:	xfprint >= 4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mousepad is a text editor for Xfce based on Leafpad.

%description -l pl
Mousepad jest edytorem dla Xfce opartym na Leafpad.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_datadir}/locale/*/LC_MESSAGES/*.mo
