%define	pname	libgnome-java
%define	api	2.6
%define	gtkapi	2.4
Summary:	Java interface for libgnome
Summary(pl):	Wrapper Java dla libgnome
Name:		java-libgnome
Version:	2.6.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{pname}/2.6/%{pname}-%{version}.tar.bz2
# Source0-md5:	e21d89743468ce83d2d0aefbadd2d0eb
Patch0:		%{name}-configure.patch
Patch1:		%{name}-version_vars.patch
URL:		http://java-gnome.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-java >= 3.3.2
BuildRequires:	java-gtk-devel >= 2.4.0
BuildRequires:	libgcj-devel >= 3.3.2
BuildRequires:	libgnomeui-devel >= 2.6.0
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
%patch1 -p1

%build
version="%{version}"; export version
apiversion="%{api}"; export apiversion
gtkapiversion="%{gtkapi}"; export gtkapiversion
%{__autoconf}
%configure \
	GCJ_JAR=`echo /usr/share/java/libgcj*.jar`

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/java-gnome,%{_libdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_datadir}/java-gnome/*
