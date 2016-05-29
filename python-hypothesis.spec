%{!?__python2: %global __python2 /usr/bin/python2}
%global srcname hypothesis


Name:           python-%{srcname}
Version:        3.4.0
Release:        1%{?dist}
Summary:        A library for property based testing

License:        MPLv2.0
URL:            https://github.com/DRMacIver/hypothesis
Source0:        https://github.com/DRMacIver/hypothesis/archive/%{version}.tar.gz#/hypothesis-%{version}.tar.gz
# disable Sphinx extensions that require Internet access
Patch0:         %{srcname}-2.0.0-offline.patch

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-sphinx
BuildRequires:  python-enum34

%if 0%{?fedora}
BuildRequires:  python3-devel
%endif

%description
Hypothesis is a library for testing your Python code against a much
larger range of examples than you would ever want to write by
hand. It’s based on the Haskell library, Quickcheck, and is designed
to integrate seamlessly into your existing Python unit testing work
flow.


%package     -n python2-%{srcname}
Summary:        A library for property based testing
Obsoletes:      python-%{srcname} < 1.11.1-1
Requires:       python-enum34

%if 0%{?fedora}
%{?python_provide:%python_provide python2-%{srcname}}
Suggests:       numpy
Suggests:       pytz
%else
Provides:       python-hypothesis = %{version}-%{release}
%endif

%description -n python2-%{srcname}
Hypothesis is a library for testing your Python code against a much
larger range of examples than you would ever want to write by
hand. It’s based on the Haskell library, Quickcheck, and is designed
to integrate seamlessly into your existing Python unit testing work
flow.


%if 0%{?fedora}
%package     -n python3-%{srcname}
Summary:        A library for property based testing
%{?python_provide:%python_provide python3-%{srcname}}

Suggests:       python3-numpy
Suggests:       python3-pytz

%description -n python3-%{srcname}
Hypothesis is a library for testing your Python code against a much
larger range of examples than you would ever want to write by
hand. It’s based on the Haskell library, Quickcheck, and is designed
to integrate seamlessly into your existing Python unit testing work
flow.
%endif


%prep
%autosetup -n %{srcname}-python-%{version} -p1

# remove shebang, mergedbs gets installed in sitelib
%{__sed} -i -e 1,2d src/hypothesis/tools/mergedbs.py


%build
%if 0%{?fedora}
%py2_build
%py3_build
READTHEDOCS=True sphinx-build -b man docs docs/_build/man
%else
%{__python2} setup.py build
%endif


%install
%if 0%{?fedora}
%py2_install
%py3_install
%{__install} -Dp -m 644 docs/_build/man/hypothesis.1 \
             $RPM_BUILD_ROOT%{_mandir}/man1/hypothesis.1
%else
%{__python2} setup.py install --skip-build --prefix=%{_prefix} --root %{buildroot}
%endif


%files -n python2-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python2_sitelib}/*
%if 0%{?fedora}
%{_mandir}/man1/hypothesis.1*
%endif

%if 0%{?fedora}
%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/*
%{_mandir}/man1/hypothesis.1*
%endif

%changelog
* Sun May 29 2016 Michel Alexandre Salim <salimma@fedoraproject.org> - 3.4.0-1
- Update to 3.4.0
- Version the explicit Provides

* Wed May 04 2016 Nathaniel McCallum <npmccallum@redhat.com> - 3.1.3-1
- Update to 3.1.3
- Remove unused code
- Remove unused dependencies

* Sun Feb 14 2016 Michel Salim <salimma@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Sep 25 2015 Michel Salim <salimma@fedoraproject.org> - 1.11.2-1
- Update to 1.11.2

* Sun Sep 20 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.11.1-1
- Update to 1.11.1

* Wed Sep  2 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.11.0-1
- Update to 1.11.0

* Tue Sep  1 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.10.6-3
- Re-disable tests for now

* Tue Sep  1 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.10.6-2
- Disable Python3 tests - need debugging on ARM builders

* Mon Aug 31 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.10.6-1
- Update to 1.10.6
- Enable tests

* Fri Aug  7 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.10.0-1
- Update to 1.10

* Wed Jul 29 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.9.0-1
- Update to 1.9.0

* Fri Jul 24 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.8.5-2
- Remove she-bang from tools/mergedbs.py
- Include manpage

* Fri Jul 24 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.8.5-1
- Update to 1.8.5
- Make Python3 build unconditional

* Thu Jul 23 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.8.2-1
- Initial package
