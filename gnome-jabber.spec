Summary:	A GNOME 2 Jabber client
Summary(pl):	Klient Jabbera dla GNOME 2
Name:		gnome-jabber
Version:	0.2
Release:	0.2
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/gnome-jabber/%{name}-%{version}.tar.gz
# Source0-md5:	ae5acf1958d61e13ead5d3f47eaf3c4e
Source1:	%{name}.desktop
URL:		http://gnome-jabber.sf.net/
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

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
	
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*
