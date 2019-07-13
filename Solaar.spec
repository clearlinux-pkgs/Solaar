#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Solaar
Version  : 0.9.2
Release  : 2
URL      : https://github.com/pwr/Solaar/archive/0.9.2.tar.gz
Source0  : https://github.com/pwr/Solaar/archive/0.9.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: Solaar-bin = %{version}-%{release}
Requires: Solaar-data = %{version}-%{release}
Requires: Solaar-license = %{version}-%{release}
Requires: Solaar-python = %{version}-%{release}
Requires: Solaar-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
**Solaar** is a Linux device manager for Logitech's [Unifying Receiver][unifying]
peripherals. It is able to pair/unpair devices to the receiver, and for most
devices read battery status.

%package bin
Summary: bin components for the Solaar package.
Group: Binaries
Requires: Solaar-data = %{version}-%{release}
Requires: Solaar-license = %{version}-%{release}

%description bin
bin components for the Solaar package.


%package data
Summary: data components for the Solaar package.
Group: Data

%description data
data components for the Solaar package.


%package extras
Summary: extras components for the Solaar package.
Group: Default

%description extras
extras components for the Solaar package.


%package license
Summary: license components for the Solaar package.
Group: Default

%description license
license components for the Solaar package.


%package python
Summary: python components for the Solaar package.
Group: Default
Requires: Solaar-python3 = %{version}-%{release}
Provides: solaar-python

%description python
python components for the Solaar package.


%package python3
Summary: python3 components for the Solaar package.
Group: Default
Requires: python3-core

%description python3
python3 components for the Solaar package.


%prep
%setup -q -n Solaar-0.9.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1547769061
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Solaar
cp COPYING %{buildroot}/usr/share/package-licenses/Solaar/COPYING
cp packaging/debian/copyright %{buildroot}/usr/share/package-licenses/Solaar/packaging_debian_copyright
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
install -Dm0644 rules.d/42-logitech-unify-permissions.rules %{buildroot}%/usr/lib/udev/rules.d/42-logitech-unify-permissions.rules
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/solaar
/usr/bin/solaar-cli

%files data
%defattr(-,root,root,-)
%exclude /usr/share/applications/solaar.desktop
%exclude /usr/share/icons/hicolor/scalable/apps/solaar.svg
%exclude /usr/share/solaar/icons/light_000.png
%exclude /usr/share/solaar/icons/light_020.png
%exclude /usr/share/solaar/icons/light_040.png
%exclude /usr/share/solaar/icons/light_060.png
%exclude /usr/share/solaar/icons/light_080.png
%exclude /usr/share/solaar/icons/light_100.png
%exclude /usr/share/solaar/icons/light_unknown.png
%exclude /usr/share/solaar/icons/solaar-attention.svg
%exclude /usr/share/solaar/icons/solaar-init.svg
%exclude /usr/share/solaar/icons/solaar.svg

%files extras
%defattr(-,root,root,-)
/usr/bin/solaar
/usr/lib/python3.7/site-packages/solaar/__pycache__/gtk.cpython-37.pyc
/usr/lib/python3.7/site-packages/solaar/ui/__init__.py
/usr/lib/python3.7/site-packages/solaar/ui/__pycache__/about.cpython-37.pyc
/usr/lib/python3.7/site-packages/solaar/ui/__pycache__/action.cpython-37.pyc
/usr/lib/python3.7/site-packages/solaar/ui/__pycache__/icons.cpython-37.pyc
/usr/lib/python3.7/site-packages/solaar/ui/__pycache__/notify.cpython-37.pyc
/usr/lib/python3.7/site-packages/solaar/ui/__pycache__/pair_window.cpython-37.pyc
/usr/lib/python3.7/site-packages/solaar/ui/__pycache__/tray.cpython-37.pyc
/usr/lib/python3.7/site-packages/solaar/ui/about.py
/usr/lib/python3.7/site-packages/solaar/ui/action.py
/usr/lib/python3.7/site-packages/solaar/ui/config_panel.py
/usr/lib/python3.7/site-packages/solaar/ui/icons.py
/usr/lib/python3.7/site-packages/solaar/ui/notify.py
/usr/lib/python3.7/site-packages/solaar/ui/pair_window.py
/usr/lib/python3.7/site-packages/solaar/ui/tray.py
/usr/lib/python3.7/site-packages/solaar/ui/window.py
/usr/share/applications/solaar.desktop
/usr/share/icons/hicolor/scalable/apps/solaar.svg
/usr/share/solaar/icons/light_000.png
/usr/share/solaar/icons/light_020.png
/usr/share/solaar/icons/light_040.png
/usr/share/solaar/icons/light_060.png
/usr/share/solaar/icons/light_080.png
/usr/share/solaar/icons/light_100.png
/usr/share/solaar/icons/light_unknown.png
/usr/share/solaar/icons/solaar-attention.svg
/usr/share/solaar/icons/solaar-init.svg
/usr/share/solaar/icons/solaar.svg

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Solaar/COPYING
/usr/share/package-licenses/Solaar/packaging_debian_copyright

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
%exclude /usr/lib/python3.7/site-packages/solaar/__pycache__/gtk.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/solaar/ui/__init__.py
%exclude /usr/lib/python3.7/site-packages/solaar/ui/__pycache__/about.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/solaar/ui/__pycache__/action.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/solaar/ui/__pycache__/icons.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/solaar/ui/__pycache__/notify.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/solaar/ui/__pycache__/pair_window.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/solaar/ui/__pycache__/tray.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/solaar/ui/about.py
%exclude /usr/lib/python3.7/site-packages/solaar/ui/action.py
%exclude /usr/lib/python3.7/site-packages/solaar/ui/config_panel.py
%exclude /usr/lib/python3.7/site-packages/solaar/ui/icons.py
%exclude /usr/lib/python3.7/site-packages/solaar/ui/notify.py
%exclude /usr/lib/python3.7/site-packages/solaar/ui/pair_window.py
%exclude /usr/lib/python3.7/site-packages/solaar/ui/tray.py
%exclude /usr/lib/python3.7/site-packages/solaar/ui/window.py
/usr/lib/python3*/*
