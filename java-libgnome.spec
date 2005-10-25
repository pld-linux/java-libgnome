%define		pname	libgnome-java
Summary:	Java interface for libgnome
Summary(pl):	Wrapper Java dla libgnome
Name:		java-libgnome
Version:	2.12.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://research.operationaldynamics.com/linux/java-gnome/dist/%{pname}-%{version}.tar.gz
# Source0-md5:	cbabafc971d49784aab879a6bc75be1c
URL:		http://java-gnome.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-utils
BuildRequires:	gcc-java >= 5:3.3.2
BuildRequires:	java-cairo-devel >= 1.0.0
BuildRequires:	java-glib-devel >= 0.2.0
BuildRequires:	java-gtk-devel >= 2.8.0
BuildRequires:	libgcj-devel >= 5:3.3.2
BuildRequires:	libgnomeui-devel >= 2.8.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
Obsoletes:	java-gnome
Obsoletes:	libgnome-java
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		macros  %{_datadir}/glib-java/macros

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

%package doc
Summary:        Tutorial and examples for java-libgnome
Summary(pl):    Tutorial i przyk³ady dla java-libgnome
Group:          Documentation

%description doc
Tutorial and examples for java-libgnome.

%description doc -l pl
Tutorial i przyk³ady dla java-libgnome.

%prep
%setup -q -n %{pname}-%{version}

%build
%{__libtoolize}
%{__aclocal} -I `pkg-config --variable macro_dir gtk2-java` -I %{macros}
%{__automake}
%{__autoconf}
%configure \
	GCJ_JAR=`echo %{_datadir}/java/libgcj*.jar` \
	--without-javadocs

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_libdir},%{_pkgconfigdir}} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
	
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_docdir}/%{pname}-%{version}/examples \
        $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -f $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/examples/*.in
rm -f $RPM_BUILD_ROOT%{_docdir}/%{pname}-%{version}/{AUTHORS,COPYING,NEWS,README}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*-2.12.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnomejava.so
%attr(755,root,root) %{_libdir}/libgnomejni.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_javadir}/*
%{_pkgconfigdir}/*.pc

%files doc
%defattr(644,root,root,755)
%dir %{_docdir}/%{pname}-%{version}
%doc %{_docdir}/%{pname}-%{version}/tutorial
%{_examplesdir}/%{name}-%{version}
