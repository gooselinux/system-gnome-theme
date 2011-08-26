Summary: System GNOME theme
Name: system-gnome-theme
Version: 60.0.2
Release: 1%{?dist}
BuildArch: noarch
License: GPLv2+
Group: User Interface/Desktops
# There is no upstream
Source0: %{name}-%{version}.tar.bz2
URL: http://www.redhat.com
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires: system-icon-theme
Requires: dmz-cursor-themes

# we require XML::Parser for our in-tree intltool
BuildRequires: perl(XML::Parser)
BuildRequires: intltool

Obsoletes: redhat-artwork
Obsoletes: fedora-gnome-theme

%description
This package contains the system GNOME meta theme.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# These are empty
rm -f ChangeLog NEWS README

# The upstream packages may gain po files at some point in the near future
%find_lang %{name} || touch %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS COPYING
%{_sysconfdir}/gtk-2.0/gtkrc
%{_datadir}/themes/System

%changelog
* Tue Jul 20 2010 Ray Strode <rstrode@redhat.com> 60.0.2-1
- Update gtkrc to use Slider too
  Resolves: #611864

* Tue Jul 13 2010 Jon McCann <jmccann@redhat.com> 60.0.1-1
- Use Slider theme by default
  Resolves: #611864

* Tue May 04 2010 Ray Strode <rstrode@redhat.com> 60.0.0-2
- Add Obsoletes to ease upgrade path
  Resolves: #566368

* Tue May 04 2010 Ray Strode <rstrode@redhat.com> 60.0.0-1
- New system-gnome-theme
