Summary:	A GNOME 2 Jabber client
Summary(pl):	Klient Jabbera dla GNOME 2
Name:		gnome-jabber
Version:	0.1.0
Release:	0.2
License:	GPL
Group:		Applications/Communications
Source0:	http://gnome-jabber.sourceforge.net/download/%{name}-%{version}.tar.bz2
# Source0-md5:	0551e2e90cc3d6f066b7009b9479994a
Source1:	%{name}.desktop
Patch0:		%{name}-DESTDIR.patch
URL:		http://gnome-jabber.sf.net
BuildRequires:	gnet-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libxml2-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An Instant Message Client for GNOME using the Jabber Protocol.

%description -l pl
Komunikator internetowy dla GNOME u¿ywaj±cy protoko³u Jabbera.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
cp images/jsf.png $RPM_BUILD_ROOT%{_pixmapsdir}
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*
