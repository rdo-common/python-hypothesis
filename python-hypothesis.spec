%global pkgname hypothesis

Name:           python-%{pkgname}
Version:        1.8.5
Release:        2%{?dist}
Summary:        A library for property based testing

License:        MPLv2.0
URL:            https://github.com/DRMacIver/hypothesis
Source0:        https://github.com/DRMacIver/hypothesis/archive/v%{version}.tar.gz#/hypothesis-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python3-devel
BuildRequires:  python-sphinx
# Test dependencies
BuildRequires:  pytest
BuildRequires:  python-flake8
BuildRequires:  python3-pytest
BuildRequires:  python3-flake8

%description
Hypothesis is a library for testing your Python code against a much
larger range of examples than you would ever want to write by
hand. It’s based on the Haskell library, Quickcheck, and is designed
to integrate seamlessly into your existing Python unit testing work
flow.


%package     -n python3-%{pkgname}
Summary:        A library for property based testing

%description -n python3-%{pkgname}
Hypothesis is a library for testing your Python code against a much
larger range of examples than you would ever want to write by
hand. It’s based on the Haskell library, Quickcheck, and is designed
to integrate seamlessly into your existing Python unit testing work
flow.


%prep
%setup -qc
mv %{pkgname}-%{version} python2
# remove shebang, mergedbs gets installed in sitelib
%{__sed} -i -e 1,2d python2/src/hypothesis/tools/mergedbs.py

cp -a python2 python3


%build
pushd python2
%{__python2} setup.py build
(cd docs && READTHEDOCS=True make man)
popd

pushd python3
%{__python3} setup.py build
popd


%install
rm -rf $RPM_BUILD_ROOT
# Must do the python3 install first because the scripts in /usr/bin are
# overwritten with every setup.py install (and we want the python2 version
# to be the default for now).
pushd python3
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
popd

pushd python2
%{__python2} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
%{__install} -Dp -m 644 docs/_build/man/hypothesis.1 \
             $RPM_BUILD_ROOT%{_mandir}/man1/hypothesis.1
popd


%check
pushd python2
%{__python2} setup.py test
popd

pushd python3
%{__python3} setup.py test
popd


%files
%license python2/LICENSE.txt
%doc python2/README.rst
%{python2_sitelib}/*
%{_mandir}/man1/hypothesis.1*

%files -n python3-%{pkgname}
%license python3/LICENSE.txt
%doc python3/README.rst
%{python3_sitelib}/*


%changelog
* Fri Jul 24 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.8.5-2
- Remove she-bang from tools/mergedbs.py
- Include manpage

* Fri Jul 24 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.8.5-1
- Update to 1.8.5
- Make Python3 build unconditional

* Thu Jul 23 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.8.2-1
- Initial package
