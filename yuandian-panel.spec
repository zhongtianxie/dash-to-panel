%global pkg_prefix gnome-shell-extension
Name:           dash-to-panel
Version:        3.26.2
Release:        3%{?dist}
Summary:        Modify and extend GNOME Shell functionality and behavior

Group:          User Interface/Desktops
# The entire source code is GPLv2+ except lib/convenience.js which is BSD
License:        GPLv2+ and BSD
URL:            http://wiki.gnome.org/Projects/GnomeShell/Extensions
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{major_version}/%{name}-%{version}.tar.xz
# BuildRequires:  gnome-common
BuildRequires:  autoconf automake
BuildRequires:  gettext >= 0.19.6
BuildRequires:  git
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(libgtop-2.0)
Requires:       gnome-shell >= %{min_gs_version}
BuildArch:      noarch

%description
GNOME Shell Extensions is a collection of extensions providing additional and
optional functionality to GNOME Shell.


%package -n %{pkg_prefix}-dash-to-panel
Summary:        Show the dash outside the activities overview
Group:          User Interface/Desktops
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-dash-to-panel
This GNOME Shell extension makes the dash available outside the activities overview.

%prep
%setup -q


%build
make %{?_smp_mflags}
# In case we build from a Git checkout

%install
%make_install

%files -n %{pkg_prefix}-dash-to-panel
%{_datadir}/gnome-shell/extensions/dash-to-panel*/

%postun -n %{pkg_prefix}-dash-to-panel
if [ $1 -eq 0 ]; then
  /usr/bin/glib-compile-schemas %{_datadir}/gnome-shell/extensions/dash-to-panel*/schemas/ &>/dev/null || :
fi

%posttrans -n %{pkg_prefix}-dash-to-panel
/usr/bin/glib-compile-schemas %{_datadir}/gnome-shell/extensions/dash-to-panel*/schemas/ &>/dev/null || :

%changelog

* Fri Jun 21 2019 Xie Zhongtian <zhongtianemail@gmail.com> - gitfe1593e
- Panel build
