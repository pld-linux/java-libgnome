%define	pname	libgnome-java
Summary:	Java interface for libgnome
Summary(pl):	Wrapper Java dla libgnome
Name:		java-libgnome
Version:	2.8.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{pname}/2.8/%{pname}-%{version}.tar.bz2
# Source0-md5:	52a5d0e2f9f2ced48ae22e0ab02ee959
URL:		http://java-gnome.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-java >= 5:3.3.2
BuildRequires:	java-gtk-devel >= 2.4.5
BuildRequires:	libgcj-devel >= 5:3.3.2
BuildRequires:	libgnomeui-devel >= 2.8.0
BuildRequires:	pkgconfig
Obsoletes:	java-gnome
Obsoletes:	libgnome-java
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Java interface for libgnome.

%description -l pl
Wrapper Java dla libgnome.

%package devel
Summary:	Header files for java-libgnome library
Summary(pl):	Pliki nag³ówkowe biblioteki java-libgnome
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libgnome-java-devel

%description devel
Header files for java-libgnome library.

%description devel -l pl
Pliki nag³ówkowe biblioteki java-libgnome.

%prep
%setup -q -n %{pname}-%{version}

%build
%{__aclocal} -I `pkg-config --variable macro_dir gtk2-java`
%{__autoconf}
%configure \
	GCJ_JAR=`echo /usr/share/java/libgcj*.jar`

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_libdir},%{_pkgconfigdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_javadir}/*
%{_pkgconfigdir}/*.pc
