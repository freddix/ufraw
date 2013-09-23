Summary:	RAW photo loader
Name:		ufraw
Version:	0.19.2
Release:	1
License:	GPL v2
Group:		Applications/Graphics
Source0:	http://downloads.sourceforge.net/ufraw/%{name}-%{version}.tar.gz
# Source0-md5:	71ba19bbf2a4d7f3a17e5cc3d3efa3d4
URL:		http://ufraw.sourceforge.net/
BuildRequires:	exiv2-devel
BuildRequires:	gimp-devel
BuildRequires:	gtkimageview-devel
BuildRequires:	lcms-devel
BuildRequires:	lensfun-devel >= 0.2.7
BuildRequires:	libexif-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	pkg-config
Requires(post,postun):	desktop-file-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         plugindir      %(gimptool --gimpplugindir)/plug-ins

%description
UFRaw is a utility to read and manipulate raw images from digital
cameras. It can be used by itself or as a GIMP plug-in. It reads raw
images using Dave Coffin's raw conversion utility DCRaw. And it
supports basic color management using Little CMS, allowing the user to
apply color profiles.

%package -n gimp-plugin-ufraw
Summary:	RAW photo loader GIMP plugin
Group:		Applications/Graphics

%description -n gimp-plugin-ufraw
RAW photo loader GIMP plugin.

%package batch
Summary:	RAW photo loader batch software
Group:		Applications/Graphics

%description batch
RAW photo loader batch software.

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

install ufraw.desktop $RPM_BUILD_ROOT%{_desktopdir}

#mv $RPM_BUILD_ROOT%{_datadir}/locale/{no,nb}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/ufraw
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_mandir}/man1/ufraw*

%files -n gimp-plugin-ufraw
%defattr(644,root,root,755)
%attr(755,root,root) %{plugindir}/ufraw-gimp

%files batch
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ufraw-batch

