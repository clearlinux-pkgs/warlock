#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : warlock
Version  : 1.3.0
Release  : 29
URL      : https://files.pythonhosted.org/packages/2d/40/9f01a5e1574dab946598793351d59c86f58209d182d229aaa545abb98894/warlock-1.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/2d/40/9f01a5e1574dab946598793351d59c86f58209d182d229aaa545abb98894/warlock-1.3.0.tar.gz
Summary  : Python object model built on JSON schema and JSON patch.
Group    : Development/Tools
License  : Apache-2.0
Requires: warlock-python3
Requires: warlock-license
Requires: warlock-python
Requires: jsonpatch
Requires: jsonschema
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : jsonpatch
BuildRequires : jsonpointer
BuildRequires : jsonschema
BuildRequires : pbr
BuildRequires : pip
BuildRequires : py
BuildRequires : pytest
BuildRequires : python-core
BuildRequires : python3-core
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools-legacypython
BuildRequires : six
BuildRequires : warlock

%description
# Warlock
[![Build Status](https://travis-ci.org/bcwaldon/warlock.svg?branch=master)](https://travis-ci.org/bcwaldon/warlock)

%package legacypython
Summary: legacypython components for the warlock package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the warlock package.


%package license
Summary: license components for the warlock package.
Group: Default

%description license
license components for the warlock package.


%package python
Summary: python components for the warlock package.
Group: Default
Requires: warlock-python3

%description python
python components for the warlock package.


%package python3
Summary: python3 components for the warlock package.
Group: Default
Requires: python3-core

%description python3
python3 components for the warlock package.


%prep
%setup -q -n warlock-1.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532377932
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 || :
%install
export SOURCE_DATE_EPOCH=1532377932
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/warlock
cp LICENSE.txt %{buildroot}/usr/share/doc/warlock/LICENSE.txt
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(-,root,root,-)
/usr/share/doc/warlock/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
