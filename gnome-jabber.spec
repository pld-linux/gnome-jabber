Summary:	A GNOME 2 Jabber client
Summary(pl):	Klient Jabbera dla GNOME 2
Name:		gnome-jabber
Version:	0.4
%define		snap 20040105
Release:	0.%{snap}.1
License:	GPL
Group:		Applications/Communications
Source0:	%{name}-%{version}-%{snap}.tar.gz
# Source0-md5:	55a5a0eb1fe71000a827b9feb093d1f7
Source1:	%{name}.desktop
URL:		http://gnome-jabber.sf.net/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnet-devel
BuildRequires:	gtk+2-devel
BuildRequires:	intltool
BuildRequires:	libgnomeui-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRequires:	scrollkeeper
Requires(post): GConf2
Requires(post): /usr/bin/scrollkeeper-update
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An Instant Message Client for GNOME using the Jabber Protocol.

%description -l pl
Komunikator internetowy dla GNOME u¿ywaj±cy protoko³u Jabbera.

%prep
%setup -qn %{name}-%{version}-%{snap}

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
intltoolize --copy --force

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

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*
%{_sysconfdir}/gconf/schemas/*
