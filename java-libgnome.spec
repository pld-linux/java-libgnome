%define	pname	libgnome-java
Summary:	Java interface for libgnome
Summary(pl):	Wrapper Java dla libgnome
Name:		java-libgnome
Version:	2.7.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{pname}/2.7/%{pname}-%{version}.tar.bz2
# Source0-md5:	a6b58dc3da3d9547cf5753fc4e4bf195
Patch0:		%{name}-DESTDIR.patch
URL:		http://java-gnome.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-java >= 3.3.2
BuildRequires:	java-gtk-devel >= 2.4.3
BuildRequires:	libgcj-devel >= 3.3.2
BuildRequires:	libgnomeui-devel >= 2.7.2
BuildRequires:	slocate
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
%patch0 -p1

%build
%{__autoconf}
%configure \
	GCJ_JAR=`echo /usr/share/java/libgcj*.jar`

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/java,%{_libdir},%{_pkgconfigdir}}

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
%{_datadir}/java/*
%{_pkgconfigdir}/*.pc
